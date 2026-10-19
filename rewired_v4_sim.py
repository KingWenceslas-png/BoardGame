"""
REWIRED v4 — Comprehensive Monte Carlo Simulation Suite
=======================================================
Calibrated against the v3 baseline to evaluate the exact v4 ruleset:
1. 20 Semantic Word Families x 4 words per family = 80 Lexicon Word Cards
2. 80 Cognitive Clue Cards (Meaning Row = 6 face-up, pruned each round)
3. Red Decoder Lens Verification (Exact Link vs Echo/Family Link)
4. CEFR A1-B1 Vocabulary Tiers (30 A1 / 30 A2 / 20 B1):
   - Exact Link: A1 = +10%, A2 = +15%, B1 = +20%
   - Echo Link (Same Family): A1 = +5%, A2 = +10%, B1 = +10% (or flat +10%)
5. Shield Tokens COMPLETELY REMOVED
6. "Safe Space" Opportunity Cards COMPLETELY REMOVED
7. 15 Opportunity Cards in the Lexicon Deck:
   - Testing splits of "Life Happens (Normal)" vs "Double or Nothing"
"""

import random
import statistics
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional

random.seed(2026)

@dataclass
class WordCard:
    card_id: int          # 0..79
    family_id: int        # 0..19 (20 families, 4 words each)
    tier: str             # 'A1', 'A2', 'B1'
    exact_points: int     # 10, 15, 20
    echo_points: int      # 5 or 10


@dataclass
class HabitCard:
    name: str
    category: str         # 'boost', 'setback', 'social_pair', 'social_all'
    delta: int            # +5, +10, +15, -5, -10


@dataclass
class SimConfig:
    name: str
    num_players: int = 3
    meaning_row_size: int = 6
    prune_per_round: int = 1
    base_hand_size: int = 4
    opp_normal_count: int = 11      # "Life Happens"
    opp_don_count: int = 4          # "Double or Nothing"
    opp_safe_count: int = 0         # Removed in v4!
    has_shield_tokens: bool = False # Removed in v4!
    echo_mode: str = "tiered"       # "tiered" (A1=5, A2=10, B1=10), "flat10" (10), "flat5" (5)
    seat_handicap: bool = False     # Later seats start at +5%
    target_score: int = 100
    don_policy: str = "smart"       # "always_gamble", "always_safe", "smart"


def build_word_and_clue_decks(echo_mode: str = "tiered") -> Tuple[List[WordCard], List[WordCard]]:
    cards: List[WordCard] = []
    card_id = 0
    for fam in range(20):
        # 20 families of 4 words each -> 30 A1, 30 A2, 20 B1
        fam_tiers = ['A1', 'A1', 'A2', 'B1'] if fam < 10 else ['A1', 'A2', 'A2', 'B1']
        for t in fam_tiers:
            exact_pts = 10 if t == 'A1' else (15 if t == 'A2' else 20)
            if echo_mode == "flat10":
                echo_pts = 10
            elif echo_mode == "flat5":
                echo_pts = 5
            else:
                # Tiered Echo: A1 = +5%, A2 = +10%, B1 = +10% (5-10% less than Exact Link)
                echo_pts = 5 if t == 'A1' else 10
            cards.append(WordCard(
                card_id=card_id,
                family_id=fam,
                tier=t,
                exact_points=exact_pts,
                echo_points=echo_pts
            ))
            card_id += 1
    return list(cards), list(cards)


def build_habit_deck_v4() -> List[HabitCard]:
    """
    40-Card Habit Loops & Triggers Deck (No Shield Tokens).
    Matches the GDD's 40-card mix with former Shield cards converted to direct recovery events:
      - 18 Keystone Healthy Habits (Boosts):
          * 4x +15% (5k Morning Run, Full Weekend Digital Detox, etc.)
          * 10x +10% (Sunday Mud Football, Cold Shower, Gym PR, Nature Walk, etc.)
          * 4x +5%  (Cooked Offline Meal, 8h Sleep, Journaling, Mindful Tea)
      - 14 Relapse Triggers (Setbacks):
          * 7x -10% (1:15 AM Bedroom Loop, Deadline Crash, Late-Night Binge, etc.)
          * 7x -5%  (Boredom Vacuum, Algorithm Rabbit Hole, Doomscrolling, etc.)
      - 8 Support Circle Actions (Interactive Social):
          * 5x Accountability SOS (+5% to active player AND +5% to lowest-score ally)
          * 3x Group Breakthrough (+5% to ALL players at the table)
    Average raw EV per card = (+180 + 40 - 105) / 40 = +2.875% (and ~+3.7% after stage floors).
    """
    deck: List[HabitCard] = []
    for _ in range(4):
        deck.append(HabitCard("Major Breakthrough (+15%)", "boost", 15))
    for _ in range(10):
        deck.append(HabitCard("Keystone Habit (+10%)", "boost", 10))
    for _ in range(4):
        deck.append(HabitCard("Mindful Routine (+5%)", "boost", 5))
    for _ in range(7):
        deck.append(HabitCard("Major Trigger (-10%)", "setback", -10))
    for _ in range(7):
        deck.append(HabitCard("Minor Trigger (-5%)", "setback", -5))
    for _ in range(5):
        deck.append(HabitCard("Accountability SOS (+5% pair)", "social_pair", 5))
    for _ in range(3):
        deck.append(HabitCard("Group Breakthrough (+5% all)", "social_all", 5))
    return deck


STAGE_FLOORS = [0, 25, 45, 65, 85]

def get_stage(score: int) -> int:
    if score >= 85:
        return 5
    elif score >= 65:
        return 4
    elif score >= 45:
        return 3
    elif score >= 25:
        return 2
    return 1

def get_stage_floor(score: int) -> int:
    return STAGE_FLOORS[get_stage(score) - 1]

def get_hand_limit(score: int, base_hand: int = 4) -> int:
    stage = get_stage(score)
    if stage == 1:
        return base_hand          # 4 cards
    elif stage in (2, 3):
        return base_hand + 1      # 5 cards
    else:
        return base_hand + 2      # 6 cards


@dataclass
class Player:
    seat: int
    skill_mod: float              # -0.15 to +0.15 learner proficiency modifier
    score: int = 0
    hand: List[WordCard] = field(default_factory=list)
    studied_clues: set = field(default_factory=set)
    studied_families: set = field(default_factory=set)
    shields: int = 0
    progress_from_words: int = 0
    progress_from_habits: int = 0
    habit_net_gain: int = 0
    habit_cards_resolved: int = 0
    exact_links_made: int = 0
    echo_links_made: int = 0
    study_actions_taken: int = 0
    dead_turns: int = 0
    total_turns: int = 0
    don_offered: int = 0
    don_gambled: int = 0

    def knows_card(self, tier: str) -> bool:
        base = {'A1': 0.85, 'A2': 0.65, 'B1': 0.45}[tier]
        prob = max(0.15, min(0.98, base + self.skill_mod))
        return random.random() < prob


def run_single_game(cfg: SimConfig, custom_don_policy_seat0: Optional[str] = None) -> Dict:
    word_cards, clue_cards = build_word_and_clue_decks(cfg.echo_mode)
    random.shuffle(word_cards)
    random.shuffle(clue_cards)

    # Deal starting hands from Word Cards first, then shuffle the 15 Opportunity cards into the Lexicon Deck
    skill_spread = [-0.15, 0.0, +0.15, +0.05][:cfg.num_players]
    random.shuffle(skill_spread)
    players = [Player(seat=i, skill_mod=skill_spread[i]) for i in range(cfg.num_players)]

    if cfg.seat_handicap:
        for p in players[1:]:
            p.score = 5

    for p in players:
        for _ in range(cfg.base_hand_size):
            p.hand.append(word_cards.pop())

    # Now build the Lexicon Draw Deck with remaining Word Cards + 15 Opportunity Cards
    lexicon_deck: List = list(word_cards)
    lexicon_deck.extend(["OPP_NORMAL"] * cfg.opp_normal_count)
    lexicon_deck.extend(["OPP_DON"] * cfg.opp_don_count)
    lexicon_deck.extend(["OPP_SAFE"] * cfg.opp_safe_count)
    random.shuffle(lexicon_deck)

    habit_deck = build_habit_deck_v4()
    random.shuffle(habit_deck)
    habit_discard: List[HabitCard] = []

    clue_deck: List[WordCard] = list(clue_cards)
    clue_discard: List[WordCard] = []
    word_discard: List[WordCard] = []

    meaning_row: List[WordCard] = []
    while len(meaning_row) < cfg.meaning_row_size and clue_deck:
        meaning_row.append(clue_deck.pop())

    def draw_habit_card() -> HabitCard:
        nonlocal habit_deck, habit_discard
        if not habit_deck:
            habit_deck = list(habit_discard)
            habit_discard.clear()
            random.shuffle(habit_deck)
        card = habit_deck.pop()
        habit_discard.append(card)
        return card

    def apply_score_change(p: Player, delta: int, ignore_floor: bool = False, is_habit: bool = False):
        old_stage = get_stage(p.score)
        if delta > 0:
            actual_gain = min(100, p.score + delta) - p.score
            p.score += actual_gain
            if is_habit:
                p.progress_from_habits += actual_gain
                p.habit_net_gain += actual_gain
            else:
                p.progress_from_words += actual_gain
        elif delta < 0:
            if cfg.has_shield_tokens and p.shields > 0:
                p.shields -= 1
                return
            floor = 0 if ignore_floor else get_stage_floor(p.score)
            new_score = max(floor, p.score + delta)
            actual_loss = new_score - p.score
            p.score = new_score
            if is_habit:
                p.habit_net_gain += actual_loss
        new_stage = get_stage(p.score)
        if cfg.has_shield_tokens and old_stage < 3 <= new_stage:
            p.shields = min(2, p.shields + 1)

    def resolve_opportunity(p: Player, opp_type: str):
        p.habit_cards_resolved += 1
        if opp_type == "OPP_NORMAL":
            h = draw_habit_card()
            resolve_habit_effect(p, h, multiplier=1, ignore_floor=False, safe_mode=False)
        elif opp_type == "OPP_SAFE":
            h = draw_habit_card()
            resolve_habit_effect(p, h, multiplier=1, ignore_floor=False, safe_mode=True)
        elif opp_type == "OPP_DON":
            p.don_offered += 1
            policy = custom_don_policy_seat0 if (p.seat == 0 and custom_don_policy_seat0) else cfg.don_policy
            if policy == "always_gamble":
                gamble = True
            elif policy == "always_safe":
                gamble = False
            else:
                max_other = max(other.score for other in players if other.seat != p.seat)
                dist_above_floor = p.score - get_stage_floor(p.score)
                if p.score >= 95:
                    gamble = False
                elif p.score <= 15:
                    gamble = True
                elif max_other - p.score >= 15:
                    gamble = True
                elif get_stage(p.score) >= 3 and dist_above_floor <= 10:
                    gamble = False
                else:
                    gamble = (p.score < max_other)

            if gamble:
                p.don_gambled += 1
                h = draw_habit_card()
                resolve_habit_effect(p, h, multiplier=2, ignore_floor=True, safe_mode=False)
            else:
                apply_score_change(p, +5, ignore_floor=False, is_habit=True)

    def resolve_habit_effect(p: Player, h: HabitCard, multiplier: int, ignore_floor: bool, safe_mode: bool):
        if h.category == "boost":
            apply_score_change(p, h.delta * multiplier, ignore_floor=False, is_habit=True)
        elif h.category == "setback":
            raw_loss = h.delta
            if safe_mode:
                raw_loss = min(0, raw_loss + 5)
            apply_score_change(p, raw_loss * multiplier, ignore_floor=ignore_floor, is_habit=True)
        elif h.category == "social_pair":
            apply_score_change(p, h.delta * multiplier, ignore_floor=False, is_habit=True)
            allies = [other for other in players if other.seat != p.seat]
            ally = min(allies, key=lambda x: x.score)
            apply_score_change(ally, h.delta, ignore_floor=False, is_habit=True)
        elif h.category == "social_all":
            for pl in players:
                mult = multiplier if pl.seat == p.seat else 1
                apply_score_change(pl, h.delta * mult, ignore_floor=False, is_habit=True)

    def draw_one_word(p: Player, resolve_opps: bool = True) -> Optional[WordCard]:
        nonlocal lexicon_deck, word_discard
        safety = 0
        while safety < 30:
            safety += 1
            if not lexicon_deck:
                if not word_discard:
                    return None
                lexicon_deck = list(word_discard)
                word_discard.clear()
                random.shuffle(lexicon_deck)
            card = lexicon_deck.pop()
            if isinstance(card, str) and card.startswith("OPP_"):
                if resolve_opps:
                    resolve_opportunity(p, card)
            else:
                return card
        return None

    def refill_hand(p: Player, resolve_opps: bool = True):
        limit = get_hand_limit(p.score, cfg.base_hand_size)
        while len(p.hand) < limit:
            w = draw_one_word(p, resolve_opps=resolve_opps)
            if w is None:
                break
            p.hand.append(w)

    rounds_played = 0
    max_rounds = 25
    half_scores_recorded = False
    leader_at_half = -1

    while rounds_played < max_rounds:
        rounds_played += 1

        for p in players:
            p.total_turns += 1
            # Phase 1: Refill hand up to current stage hand limit (resolving any Opportunity cards drawn)
            refill_hand(p, resolve_opps=True)

            # Evaluate candidate matches between Hand and Meaning Row
            # A player recognizes each card in hand/row based on their proficiency OR prior Study action
            best_action = None  # (points, link_type, word_card, clue_card)

            known_hand = [w for w in p.hand if (w.family_id in p.studied_families or p.knows_card(w.tier))]
            known_clues = [c for c in meaning_row if (c.card_id in p.studied_clues or p.knows_card(c.tier))]

            for w in known_hand:
                for c in known_clues:
                    if w.card_id == c.card_id:
                        pts = w.exact_points
                        if best_action is None or pts > best_action[0]:
                            best_action = (pts, "EXACT", w, c)
                    elif w.family_id == c.family_id:
                        pts = w.echo_points
                        if get_stage(p.score) >= 3:
                            pts += 5  # Stage 3 Prefrontal Rebound Perk: +5% bonus on Echo Links
                        if best_action is None or pts > best_action[0]:
                            best_action = (pts, "ECHO", w, c)

            if best_action is not None:
                pts, link_type, w_card, c_card = best_action
                p.hand.remove(w_card)
                word_discard.append(w_card)

                meaning_row.remove(c_card)
                clue_discard.append(c_card)
                if not clue_deck and clue_discard:
                    clue_deck = list(clue_discard)
                    clue_discard.clear()
                    random.shuffle(clue_deck)
                if clue_deck:
                    meaning_row.append(clue_deck.pop())

                if link_type == "EXACT":
                    p.exact_links_made += 1
                else:
                    p.echo_links_made += 1

                apply_score_change(p, pts, ignore_floor=False, is_habit=False)
                # Immediately draw back up to hand limit (which may trigger an Opportunity card!)
                refill_hand(p, resolve_opps=True)
            else:
                # Study Action:
                # 1. Secretly inspect 1 Clue Card in the Meaning Row with the Red Decoder Lens
                #    (revealing both that Clue's exact word and its 4-word Family!).
                # 2. Swap up to 2 cards from hand with fresh draws from the Lexicon Deck!
                unstudied = [c for c in meaning_row if c.card_id not in p.studied_clues]
                if unstudied or len(p.hand) > 0:
                    p.study_actions_taken += 1
                    if unstudied:
                        target_c = random.choice(unstudied)
                        p.studied_clues.add(target_c.card_id)
                        p.studied_families.add(target_c.family_id)
                    # Swap up to 2 cards from hand (resolving any Opportunity cards uncovered!)
                    swap_n = min(2, len(p.hand))
                    tier_order = {'B1': 0, 'A2': 1, 'A1': 2}
                    p.hand.sort(key=lambda x: tier_order[x.tier])
                    for _ in range(swap_n):
                        word_discard.append(p.hand.pop(0))
                    refill_hand(p, resolve_opps=True)
                else:
                    p.dead_turns += 1

        if not half_scores_recorded and any(p.score >= 50 for p in players):
            half_scores_recorded = True
            leader_at_half = max(players, key=lambda x: x.score).seat

        if any(p.score >= cfg.target_score for p in players):
            break

        # End of Round: Prune oldest Clue Card from Meaning Row
        for _ in range(cfg.prune_per_round):
            if meaning_row:
                clue_discard.append(meaning_row.pop(0))
                if not clue_deck and clue_discard:
                    clue_deck = list(clue_discard)
                    clue_discard.clear()
                    random.shuffle(clue_deck)
                if clue_deck:
                    meaning_row.append(clue_deck.pop())

    winner = max(players, key=lambda p: (p.score, p.exact_links_made + p.echo_links_made, p.seat))
    best_vocab_seat = max(players, key=lambda p: p.skill_mod).seat
    luckiest_habit_seat = max(players, key=lambda p: p.habit_net_gain).seat

    total_turns_all = sum(p.total_turns for p in players)
    scoring_turns_all = sum(p.exact_links_made + p.echo_links_made for p in players)
    # A turn has a "useful action" if the player either scored a link OR learned a new family via Study
    useful_turns_all = scoring_turns_all + sum(min(p.study_actions_taken, 3) for p in players)
    total_links = sum(p.exact_links_made + p.echo_links_made for p in players)
    total_exact = sum(p.exact_links_made for p in players)
    total_echo = sum(p.echo_links_made for p in players)
    total_habits = sum(p.habit_cards_resolved for p in players)

    winner_total_pos = max(1, winner.progress_from_words + winner.progress_from_habits)
    winner_habit_share = winner.progress_from_habits / winner_total_pos

    return {
        "rounds": rounds_played,
        "winner_seat": winner.seat,
        "winner_is_best_vocab": (winner.seat == best_vocab_seat),
        "winner_is_luckiest_habit": (winner.seat == luckiest_habit_seat),
        "comeback_win": (half_scores_recorded and winner.seat != leader_at_half),
        "scoring_turn_rate": scoring_turns_all / max(1, total_turns_all),
        "useful_turn_rate": min(1.0, useful_turns_all / max(1, total_turns_all)),
        "total_links": total_links,
        "exact_links": total_exact,
        "echo_links": total_echo,
        "total_habits": total_habits,
        "winner_habit_share": winner_habit_share,
        "seat0_won": (winner.seat == 0),
    }


def run_batch(cfg: SimConfig, n_games: int = 2500, custom_don_seat0: Optional[str] = None) -> Dict:
    results = [run_single_game(cfg, custom_don_seat0) for _ in range(n_games)]
    return {
        "name": cfg.name,
        "num_players": cfg.num_players,
        "median_rounds": statistics.median(r["rounds"] for r in results),
        "mean_rounds": statistics.mean(r["rounds"] for r in results),
        "scoring_turn_pct": statistics.mean(r["scoring_turn_rate"] for r in results) * 100,
        "useful_turn_pct": statistics.mean(r["useful_turn_rate"] for r in results) * 100,
        "mean_links": statistics.mean(r["total_links"] for r in results),
        "mean_exact": statistics.mean(r["exact_links"] for r in results),
        "mean_echo": statistics.mean(r["echo_links"] for r in results),
        "mean_habits": statistics.mean(r["total_habits"] for r in results),
        "winner_habit_share_pct": statistics.mean(r["winner_habit_share"] for r in results) * 100,
        "best_vocab_win_pct": statistics.mean(1 if r["winner_is_best_vocab"] else 0 for r in results) * 100,
        "luckiest_habit_win_pct": statistics.mean(1 if r["winner_is_luckiest_habit"] else 0 for r in results) * 100,
        "comeback_pct": statistics.mean(1 if r["comeback_win"] else 0 for r in results) * 100,
        "seat0_win_pct": statistics.mean(1 if r["seat0_won"] else 0 for r in results) * 100,
    }


if __name__ == "__main__":
    N = 2500
    print(f"Running REWIRED v4 Calibrated Monte Carlo Simulation ({N} games per configuration)...\n")

    splits = [
        SimConfig("v4 Split A: 11 Life Happens / 4 Double-or-Nothing", num_players=3, opp_normal_count=11, opp_don_count=4),
        SimConfig("v4 Split B: 10 Life Happens / 5 Double-or-Nothing", num_players=3, opp_normal_count=10, opp_don_count=5),
        SimConfig("v4 Split C: 9 Life Happens / 6 Double-or-Nothing",  num_players=3, opp_normal_count=9,  opp_don_count=6),
        SimConfig("v3 Baseline: 7 Normal / 4 DoN / 4 Safe (with Shields)", num_players=3, opp_normal_count=7, opp_don_count=4, opp_safe_count=4, has_shield_tokens=True),
    ]
    print("=== 1. OPPORTUNITY CARD SPLITS (3 Players, Safe Card & Shield Tokens Removed) ===")
    for sc in splits:
        res = run_batch(sc, N)
        print(f"{res['name']}:")
        print(f"  Rounds (med/mean): {res['median_rounds']:.1f} / {res['mean_rounds']:.2f} | "
              f"Links/game: {res['mean_links']:.1f} (Exact {res['mean_exact']:.1f}, Echo {res['mean_echo']:.1f}) | "
              f"Habits/game: {res['mean_habits']:.1f}")
        print(f"  Scoring Turns: {res['scoring_turn_pct']:.1f}% | Useful Actions: {res['useful_turn_pct']:.1f}% | "
              f"Winner Habit Share: {res['winner_habit_share_pct']:.1f}% | Best Vocab Win: {res['best_vocab_win_pct']:.1f}% | "
              f"Luckiest Habit Win: {res['luckiest_habit_win_pct']:.1f}% | Comeback: {res['comeback_pct']:.1f}%\n")

    print("=== 2. DOUBLE OR NOTHING POLICY ANALYSIS (3 Players, Fair = 33.3%) ===")
    base_v4 = SimConfig("v4 Recommended (10N / 5DoN)", num_players=3, opp_normal_count=10, opp_don_count=5)
    for pol in ["always_safe", "always_gamble", "smart"]:
        res = run_batch(base_v4, N, custom_don_seat0=pol)
        print(f"  Seat 0 Policy = '{pol:13s}' -> Win Rate: {res['seat0_win_pct']:.1f}%")
    print()

    print("=== 3. PLAYER COUNT SCALING (2p, 3p, 4p) ===")
    player_configs = [
        SimConfig("v4 2-Player (100% Target)", num_players=2, opp_normal_count=10, opp_don_count=5),
        SimConfig("v4 2-Player (85% Fast Target)", num_players=2, opp_normal_count=10, opp_don_count=5, target_score=85),
        SimConfig("v4 3-Player (Standard)", num_players=3, opp_normal_count=10, opp_don_count=5),
        SimConfig("v4 4-Player (Standard)", num_players=4, opp_normal_count=10, opp_don_count=5),
    ]
    for pc in player_configs:
        res = run_batch(pc, N)
        fair_win = 100.0 / pc.num_players
        print(f"{res['name']} (Fair Win = {fair_win:.1f}%):")
        print(f"  Rounds (med/mean): {res['median_rounds']:.1f} / {res['mean_rounds']:.2f} | "
              f"Scoring Turns: {res['scoring_turn_pct']:.1f}% | Useful Actions: {res['useful_turn_pct']:.1f}%")
        print(f"  Verified Links: {res['mean_links']:.1f} (Exact {res['mean_exact']:.1f}, Echo {res['mean_echo']:.1f}) | "
              f"Habits Resolved: {res['mean_habits']:.1f} | Winner Habit Share: {res['winner_habit_share_pct']:.1f}%")
        print(f"  Best Vocab Win: {res['best_vocab_win_pct']:.1f}% | Comeback Rate: {res['comeback_pct']:.1f}% | "
              f"Seat 1 Win Rate: {res['seat0_win_pct']:.1f}%\n")

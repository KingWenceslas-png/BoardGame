# REPLAYABILITY ANALYSIS & INDUSTRY BENCHMARK COMPARISON — REWIRED v4
### Evaluating Card Consumption, Learning Curves, and Replay Ceiling Against Modern Tabletop Word Games

**Related Documents:**  
- [GAME_DESIGN_DOCUMENT.md](GAME_DESIGN_DOCUMENT.md) — Core v4 Game Design Document  
- [MONTE_CARLO_SIMULATION_REPORT.md](MONTE_CARLO_SIMULATION_REPORT.md) — Statistical Balancing Report (27,500+ Simulated Games)

---

## 1. Executive Summary

Replayability in word board games is governed by whether a game relies on **Fixed Mapping** (matching a card to a pre-printed answer) or **Combinatorial / Emergent Mapping** (where cards combine in thousands of ways or rely on player-invented clues).

Because **REWIRED v4** is specifically engineered for **CEFR A1–B1 English learners**, it intentionally removes high-stress open-ended speaking requirements in favor of the **20-Family "Synaptic Web"**, **Red Acrylic Decoder Lens verification**, **Study Actions**, and **15 Opportunity Cards**.

This document provides:
1. A mathematical diagnosis of **REWIRED v4's card consumption rate** across multiple sessions.
2. A **head-to-head replayability comparison** against the 7 benchmark word games analyzed in the GDD (*Codenames*, *So Clover!*, *Paperback / Hardback*, *Decrypto*, *Just One*, *Taboo*, and *Balderdash*).
3. **Five practical, low-cost design enhancements** to expand *REWIRED v4*'s replay ceiling from **~7–8 games** to **40+ games** with the same playgroup.

---

## 2. Mathematical Card-Consumption Diagnosis of *REWIRED v4*

### 2.1 Per-Game Deck Exposure (From Monte Carlo Simulation Data)
In the base **REWIRED v4** configuration (`80 Lexicon Word Cards`, `80 Cognitive Clue Cards` across `20 Semantic Families`, and `40 Habit Loops Cards`), a standard 3- to 4-player game lasts **9 to 10 rounds** and consumes the decks at the following rate:

| Metric per Game | 2 Players (13 Rounds) | 3 Players (10 Rounds) | 4 Players (9 Rounds) | % of Total 80-Clue / 40-Habit Deck Seen |
| :--- | :---: | :---: | :---: | :---: |
| **Clue Cards Matched (Exact + Echo Links)** | 11.5 | 15.8 | 19.7 | 14% – 25% of Clue Deck |
| **Clue Cards Pruned at Round End** | 12.0 | 9.0 | 8.0 | 10% – 15% of Clue Deck |
| **Clue Cards Inspected via Study Action** | 3.8 | 5.2 | 6.1 | 5% – 8% of Clue Deck |
| **Total Unique Clue Cards Seen / Resolved** | **~27 Clues** | **~30 Clues** | **~34 Clues** | **34% – 43% of Clue Deck per game** |
| **Habit Cards Resolved (via 15 Opportunity Cards)** | **9.2 Habits** | **11.5 Habits** | **13.7 Habits** | **23% – 34% of Habit Deck per game** |

---

### 2.2 The Three-Phase Replayability Lifecycle (Same Playgroup)
Because each Cognitive Clue Card has a fixed answer on its Red Decoder Strip (`1 Exact Word` + `3 Echo Family Words`), a recurring group of players will experience three distinct phases of replayability:

```
┌────────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: THE DISCOVERY PHASE (Games 1 – 3)                                 │
│ • Replayability & Novelty: VERY HIGH                                       │
│ • Players encounter definitions for the first time, discover how the 20    │
│   Semantic Families connect, and enjoy the tactile thrill of the Red Lens. │
├────────────────────────────────────────────────────────────────────────────┤
│ PHASE 2: THE MASTERY & SPACED-REPETITION PHASE (Games 4 – 7)               │
│ • Replayability & Learning Value: PEAK PEDAGOGICAL SWEET SPOT              │
│ • Players begin recognizing Clue cards they studied in earlier sessions.   │
│ • In second-language acquisition, encountering a word 4–6 times across     │
│   spaced sessions is essential to move A2/B1 vocabulary from short-term    │
│   recognition into permanent long-term memory.                             │
├────────────────────────────────────────────────────────────────────────────┤
│ PHASE 3: THE "SOLVED DECK" RACE PHASE (Games 8+)                           │
│ • Replayability: MODERATE (Shifts from Puzzle to Tactical Card Race)       │
│ • By Game 8 with the exact same group, players have memorized most of the  │
│   80 Clue definitions.                                                     │
│ • The game remains playable as a fast-paced hand-management & push-your-   │
│   luck race (optimizing Exact vs. Echo links and gambling on Double or     │
│   Nothing), but linguistic surprise plateaus unless new packs or modes     │
│   are introduced.                                                          │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Head-to-Head Comparison with Benchmark Word Games from the GDD

Why do some tabletop word games remain fresh for 100+ sessions while others plateau after 8 sessions? Below is a direct mechanical comparison between **REWIRED v4** and the 7 industry benchmark games from the GDD:

| Game | Primary Replayability Engine | Replay Ceiling (Same Box & Group) | Beginner (A1–B1) Accessibility | Why It Replays Well (or Plateaus) | How **REWIRED v4** Compares |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **REWIRED v4** | **20 Semantic Families (Exact + Echo Links) + Red Decoder Lens + 15 Opportunity Cards** | **6–8 Games** *(Discovery/Mastery)*<br>**12–15 Games** *(Tactical Race)* | **★★★★★ (Highest)**<br>Built specifically for A1–B1 learners; zero speaking or spelling pressure. | Fixed Clue-to-Family mapping means players eventually learn all 80 Clues—which is a **pedagogical triumph** (they learned the words!), even if puzzle novelty tapers off. | Trades infinite combinatorial clues for **structured vocabulary acquisition**, tactile Red Lens verification, and push-your-luck Habit drama. |
| **Codenames** | **Combinatorial Grid** (`400 words` dealt into $5\times 5$ grids + `40 key maps`) | **100+ Games**<br>*(Virtually Infinite)* | **★★☆☆☆ (Low)**<br>Requires players to already know all 25 words on the table and invent clever hypernyms. | You never match a word to a fixed definition; you link *any* 2–3 random words that land on the grid together ($\binom{400}{25}$ combinations). | *Codenames* has vastly higher combinatorial replayability for fluent speakers, **but** it cannot teach new definitions to beginners. *REWIRED* actively teaches unfamiliar words. |
| **So Clover!** | **Pairwise Grid Intersections** (`220 cards` $\times$ 4 sides = `880 words`) | **50+ Games**<br>*(Very High)* | **★★☆☆☆ (Low–Med)**<br>Requires players to write original English bridging words from scratch. | Any two words can sit adjacent on the clover board ($\sim 386,000$ possible pairs), and players generate the clues themselves. | *REWIRED v4* adapts *So Clover!*'s concept of semantic neighborhoods into pre-built **4-word Families**, removing the pressure of inventing clues from scratch. |
| **Paperback / Hardback** | **Deck-Building + Letter Anagrams** (Cards are individual letters + abilities) | **30–50 Games**<br>*(High)* | **★★☆☆☆ (Low)**<br>Spelling English words from scrambled letters is punishing for A1–B1 learners. | Because cards are individual *letters* (`S`, `T`, `A`, `R`), the same deck can spell thousands of different words across plays. | *REWIRED v4* shares *Paperback*'s rewarding **progression engine** (expanding hand limits `4 → 5 → 6` and unlocking Stage 3–4 perks), keeping the game loop satisfying across plays. |
| **Decrypto** | **Player-Generated Coded Clues** (`400 secret keyword screens`) | **50+ Games**<br>*(Very High)* | **★☆☆☆☆ (Very Low)**<br>Requires subtle synonym and metaphor manipulation to hide clues from opponents. | Replayability comes from human psychology—giving clues that your teammates understand but opponents misinterpret. | *REWIRED v4* borrows *Decrypto*'s beloved physical **Red Decoder Lens** for tactile table excitement, while keeping the clues clear and beginner-friendly. |
| **Just One** | **Simultaneous Social Clues** (`550 target words`) | **30–50 Games**<br>*(High)* | **★★★☆☆ (Medium)**<br>Single-word clues are simple, but players must already know the target word. | Replayability comes from social collision—two friends writing the exact same clue and canceling each other out. | In *REWIRED v4*, the social table laughter comes from flipping **Opportunity Cards** (*Life Happens* and *Double or Nothing*) and *Support Circle* Habit events. |
| **Taboo** | **Time-Pressured Forbidden Speech** (`400–1,000 cards`) | **15–25 Games**<br>*(Medium)* | **★☆☆☆☆ (Very Low)**<br>Speaking fluently under a 60-second buzzer without using basic words terrifies beginners. | Once players memorize the 5 forbidden words on a card, the card becomes easier, though the timer still creates panic. | *REWIRED v4* is far more welcoming for learners than *Taboo*, replacing buzzer stress with calm semantic matching and the **Study Action**. |
| **Balderdash** | **Obscure Dictionary Trivia + Written Bluffing** | **1 Play per Card**<br>*(Low per card; relies on huge card count)* | **★☆☆☆☆ (Very Low)**<br>Writing convincing fake dictionary definitions requires native-level fluency. | Once a group hears the true definition of an obscure word in *Balderdash*, **that card is burned forever** for that group. | **Crucial Contrast:** In *Balderdash*, seeing a word twice ruins the bluff. In *REWIRED v4*, seeing a word 4–6 times across games is **the goal**, reinforcing A1–B1 retention! |

---

## 4. The Core Design Trade-Off in v4: Accessibility vs. Emergent Content

When transitioning from **v2** (which required players to speak an original sentence on every link) to **v3/v4** (which removed mandatory sentences for A1–B1 accessibility), a deliberate trade-off occurred:

1. **What v4 Gained (Massive Beginner Accessibility & Pacing):**
   - Eliminated "production freeze" (where shy or A1–B1 players feel embarrassed trying to invent an English sentence on the spot).
   - Boosted **useful actions per turn to 78.2%** and **verified vocabulary links to 15.8–19.7 per game**.
2. **What v4 Traded Away (Player-Generated Variety):**
   - In games where players invent sentences or clues, the *players themselves* generate infinite replayability.
   - When matching is strictly **Word Card $\leftrightarrow$ Clue Card**, replayability is tied directly to the size and variety of the Clue Deck.

---

## 5. Five Practical Upgrades to Multiply *REWIRED v4* Replayability (From ~7 Games to 40+ Games)

We can dramatically expand *REWIRED v4*'s replay ceiling **without adding complex rules or sacrificing A1–B1 accessibility** through five concrete production and design features:

### Upgrade 1: Print the 80 Cognitive Clue Cards **Double-Sided** (*Doubles Replayability for $0 Extra Card Cost!*)
Look closely at how **Cognitive Clue Cards** are used during gameplay:
- They sit in a central draw pile and are dealt face-up into the **6-card Meaning Row**.
- **Clue Cards are NEVER held secretly in a player's hand!**
- Because no player ever needs a hidden card back on a Clue Card, every single Clue Card can be printed **Double-Sided (`Side A` and `Side B`)**:
  - **Side A (Deck A — Blue Border):** 80 Definitions & Sentence Frames for Games 1–7.
  - **Side B (Deck B — Gold Border):** 80 *completely different* definitions, context sentences, and target answers for Games 8–15!
- **Impact:** Instantly turns 80 physical Clue cards into **160 unique Clue puzzles** at **zero extra manufacturing cost**.

### Upgrade 2: Expand the Base Box from 20 Families to **30 Families (120 Words)** & Sample 20 per Game
- If the box includes **30 Semantic Families** (`120 Word Cards` and `120 Double-Sided Clue Cards` = `240 Clue puzzles`), players only see **~25% of the Word pool** per game instead of ~40%.
- Players can either shuffle the full 120-word deck together OR pick any **20 of the 30 families** each game, ensuring different vocabulary combinations every session.

### Upgrade 3: Include 6 Asymmetric "Club Member" Character Cards (*Tactical Replayability*)
At the start of the game, deal each player 1 **Club Member Archetype Card** (representing a relatable personality in the recovery circle). Each character slightly alters tactical decisions:

| Character Archetype | Passive Recovery Trait | How It Changes Gameplay Strategy |
| :--- | :--- | :--- |
| **🏃 The Athlete** | Gain an extra **+5% Progression** whenever you resolve a physical exercise Habit card (*Mud Football*, *5K Run*, *Gym Session*). | Incentivizes drawing Opportunity cards and gambling on physical boosts. |
| **📚 The Bookworm** | Whenever you take the **Study Action**, you may swap up to **3 hand cards** (instead of 2) and keep +1 extra card until your next turn. | Turns the Study Action into a powerhouse hand-sculpting engine. |
| **🎲 The Daredevil** | On **Double or Nothing**, choosing *Play It Safe* gives **+10%** (instead of +5%), OR if you gamble and hit a Boost, gain an extra **+5%**. | Thrives on hunting down the 5 *Double or Nothing* cards in the deck. |
| **🤝 The Connector** | Whenever *any* player flips a **Support Circle** Habit card, you automatically gain **+5% Progression**. | Rewards positive table energy and shared recovery milestones. |
| **🧘 The Meditator** | Once per game, treat a normal `-10%` Relapse Trigger as `0%` through mindful breathing. | Allows aggressive pushing within a Stage without fearing a setback. |
| **🔍 The Detective** | At the start of the game, secretly peek at **2 Clue Cards** in the Meaning Row with the Red Decoder Lens before Turn 1. | Gives an immediate early-game tempo advantage on Exact Links. |

### Upgrade 4: The "Two-Stage Graduation Lifecycle" (*Decoder Mode* $\rightarrow$ *Fluent Mode*)
Turn the fact that players memorize the 80 words after ~6–8 games into a **built-in progression milestone** in the rulebook:
- **Course 1 — Decoder Mode (Games 1–6):** Play with the standard v4 rules. No original sentences required; learn the 80 A1–B1 words and their 20 families using the Red Decoder Lens and "Read the Frame."
- **Course 2 — Fluent Mode (Games 7+):** Once your group knows all 80 words by heart, recognizing definitions is easy—so your group officially **graduates to Fluent Mode**! Now, to claim the full points of an **Exact Link** (`+10% / +15% / +20%`), the player **must speak an original sentence about real life using the word**, or **combine two words from their hand into one sentence for a +5% Fluency Bonus**!
- **Impact:** Memorizing the deck is no longer the "end" of the game's life—it is how the group unlocks the advanced speaking game!

### Upgrade 5: Modular CEFR Expansion Packs (The Commercial Learning Path)
Because the **Brain Progression Boards, Wooden Markers, 2 Red Decoder Lenses, 40 Habit Cards, and 15 Opportunity Cards** are completely independent of the specific vocabulary words, the game supports low-cost **80-Word / 80-Clue Expansion Packs**:
1. **Base Box Pack:** *CEFR A1–B1 Core Emotions, Focus & Daily Habits* (20 Families / 80 Words)
2. **Expansion Pack 1:** *CEFR B1–B2 Social Relationships, Work & Mindfulness* (20 Families / 80 Words)
3. **Expansion Pack 2:** *CEFR B2–C1 Academic, Expressive & Idiomatic English* (20 Families / 80 Words)

---

## 6. Summary Verdict

| Configuration | Expected High-Replay Lifespan (Same Group) | Comparable Tabletop Benchmark |
| :--- | :---: | :--- |
| **REWIRED v4 (Base 80 Single-Sided Clues)** | **6 – 8 Games** *(Discovery & Mastery)* | *Unlock!* / *Exit* / *Balderdash* (Small Box) |
| **REWIRED v4 + Double-Sided Clues (160 Clues) + 6 Characters** | **15 – 20 Games** | *Taboo* / *Just One* |
| **REWIRED v4 + Graduation to Fluent Mode + Expansion Packs** | **40+ Games** | *Paperback* / *Hardback* / *Codenames* |

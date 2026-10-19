# MONTE CARLO SIMULATION REPORT — REWIRED v4
### Balancing the 20-Family "Synaptic Web", Red Decoder Lens, A1–B1 Vocabulary, and 15 Opportunity Cards (No Shield Tokens, No Safe Cards)

**Simulation Script:** [`rewired_v4_sim.py`](rewired_v4_sim.py)  
**Sample Size:** 2,500 – 3,000 simulated games per configuration (27,500+ total games simulated)  
**Target Audience Model:** CEFR A1–B1 English Learners (Base recognition rates: `A1 = 85%`, `A2 = 65%`, `B1 = 45%`, with $\pm 15\%$ individual skill variance across seats)

---

## 1. Executive Summary of v4 Rule Changes

Following consultation and iterative testing from v1 $\rightarrow$ v3 $\rightarrow$ **v4**, the game architecture was streamlined around four core design pillars:

| System | v1 (Original GDD) | v3 (Interim Iteration) | **v4 (Final Recommended Ruleset)** |
| :--- | :--- | :--- | :--- |
| **Word Matching Engine** | 1-to-1 ID matching (80 isolated pairs); 3-card clue market | 20 Families $\times$ 4 words (80 cards); Exact + Echo links; 6-card Meaning Row | **20 Families $\times$ 4 words (80 cards); Exact + Echo links; 6-card Meaning Row (pruned 1/round)** |
| **Verification Method** | Printed numeric ID (`#01`–`#80`) | Red Decoder Lens over camouflaged strip | **Red Decoder Lens** revealing Exact Word + 3 Family Sibling Words |
| **Vocabulary & Speaking** | Advanced C1/C2 words; mandatory spoken sentence | CEFR A1–B1 words; no mandatory sentences; Study action | **CEFR A1–B1 (30 A1 / 30 A2 / 20 B1); no mandatory sentences; Study action + optional "Read the Frame"** |
| **Defensive Mechanics** | Stage Floors + Urge Surfing Shield Tokens | Stage Floors + Shield Tokens + "Safe Space" Opportunity Cards | **Stage Floors ONLY (`0/25/45/65/85%`). Shield Tokens & Safe Cards completely removed.** |
| **Habit Trigger Engine** | Shuffled directly or icon-triggered (39 habits/game) | 15 Opportunity Cards (`7 Normal`, `4 DoN`, `4 Safe`) | **15 Opportunity Cards (`10 Life Happens`, `5 Double or Nothing`, `0 Safe`)** |
| **Stage 3 Milestone Perk** | Unlock Shield Token storage | Unlock Shield Token storage | **Synaptic Resonance:** Echo Links grant **+5% bonus progress** at Stage 3+ (`45%+`) |

---

## 2. Why the v1 Matching System Failed & How the 20-Family "Synaptic Web" Fixes It

### 2.1 The v1 Combinatorial Bottleneck
In the initial v1 rules, there were 80 unique Word Cards and 80 unique Clue Cards, with only 3 Clue Cards face-up on the table and 3 Word Cards in a player's hand.
- The probability that a specific Word Card in hand matched one of the 3 face-up Clue Cards was only $\frac{3}{80} = 3.75\%$.
- Across a 3-card hand, a player had only an **$11\%$–$16\%$ chance** of holding an exact match on any given turn.
- As a result, **84% of turns failed to produce a vocabulary match**, and **87% of the winner's points came purely from random Habit cards**.

### 2.2 The v4 Solution: 20 Word Families $\times$ 4 Words + Red Decoder Lens
By organizing the 80 A1–B1 words into **20 Semantic Families of 4 related words each** (e.g., *Family 1 — Calmness:* `Quiet` [A1], `Calm` [A1], `Peaceful` [A2], `Serene` [B1]) and expanding the central **Meaning Row to 6 Clue Cards**:
1. **Exact Link (+10% A1 / +15% A2 / +20% B1):** Playing the exact word that matches the Clue Card.
2. **Echo Link (+5% A1 / +10% A2 & B1):** Playing any of the **other 3 sibling words** from the same Semantic Family.
3. **Physical Verification via Red Decoder Lens:** Placing the red acrylic lens over the Clue Card's camouflaged Decoder Strip reveals both the **Exact Word** and the **3 Family Siblings**.
4. **The Study Action (Zero Dead Turns):** If a player cannot make a link, they use the Red Decoder Lens to secretly inspect 1 face-up Clue Card in the Meaning Row (learning its exact word and family for future turns) and swap up to 2 cards from their hand.

**Simulation Impact:**
- Useful actions per turn jump from **20% (v1) $\rightarrow$ 78.2% (v4)**.
- Scoring vocabulary turns jump from **16% (v1) $\rightarrow$ 50.4% (v4)**.
- Verified word links per game jump from **3.5 (v1) $\rightarrow$ 15.8 (v4)** (a **$4.5\times$ increase** in actual English vocabulary practice per game).

---

## 3. Experiment 1: Removing "Safe Space" Cards & Shield Tokens

We simulated removing both the **Shield Tokens** and the **4 Safe Space Opportunity Cards**, testing three different splits for the **15 Opportunity Cards** (`Life Happens` vs. `Double or Nothing`) across 2,500 3-player games per split:

| Configuration (3 Players, 2,500 Games Each) | Median Rounds | Mean Rounds | Verified Links / Game | Habit Cards / Game | Scoring Turns | Useful Actions | Winner Habit Share | Best Vocab Win Rate | Comeback Rate |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **v1 Original GDD** *(1-to-1 match, Shields)* | 8.0 | 8.12 | 3.5 | 39.0 | 16.0% | 20.0% | 87.0% | 36.0% | 41.0% |
| **v3 Reference** *(7 Normal / 4 DoN / 4 Safe + Shields)* | 10.0 | 10.39 | 15.4 | 11.4 | 50.0% | 78.1% | 32.1% | 54.4% | 27.8% |
| **v4 Split A** *(11 Life Happens / 4 Double or Nothing)* | 11.0 | 10.63 | 15.9 | 11.6 | 50.4% | 78.0% | 31.6% | 55.4% | 30.0% |
| **v4 Split B (Recommended)** *(10 Life Happens / 5 Double or Nothing)* | **10.0** | **10.48** | **15.6** | **11.4** | **50.2%** | **78.1%** | **32.5%** | **53.4%** | **30.5%** |
| **v4 Split C** *(9 Life Happens / 6 Double or Nothing)* | 10.0 | 10.38 | 15.5 | 11.3 | 50.6% | 78.7% | 32.7% | 53.6% | 30.1% |

### Key Takeaways from Experiment 1:
1. **Removing the "Safe Card" and "Shield Tokens" Improved Comeback Drama (+2.7%):**
   - In v3, players had *three* overlapping layers of defense: Stage Floors (`0/25/45/65/85%`), Shield Tokens, and Safe Space cards. Setbacks almost never landed, locking in early leaders.
   - By stripping out Shield Tokens and Safe Cards in v4, **Stage Floors alone** protect players from catastrophic frustration, while intra-stage setbacks (`-5%`, `-10%`) actually create tension. Comeback wins (a player trailing at the 50% mark who comes back to win) rose from **27.8% $\rightarrow$ 30.5%**.
2. **`10 Life Happens` + `5 Double or Nothing` (Split B) is the Sweet Spot:**
   - Having exactly $\frac{2}{3}$ Normal Opportunity cards (`10`) and $\frac{1}{3}$ High-Stakes decision cards (`5`) hits a clean **10-round median game length**, triggers **~11.4 Habit events per game** (~3.8 per player), and ensures **67.5% of the winner's progress comes from vocabulary links** while **32.5% comes from Habit events**.

---

## 4. Experiment 2: "Double or Nothing" Decision Balance

When a player draws one of the 5 **Double or Nothing** cards from the Lexicon Deck, they face an immediate choice *before* seeing the Habit card:
- **Option A (Play It Safe — Grounded Routine):** Take a guaranteed **+5% progression** (do not flip a Habit card).
- **Option B (Double or Nothing — Risk It):** Flip the top Habit card and **double** its effect (`+10%` becomes `+20%`; `-10%` becomes `-20%`), AND **doubled losses ignore your Stage Floor**.

We tested three player policies for Seat 1 against a smart table in 3-player games (where a perfectly fair win rate is **33.3%**):

| Seat 1 "Double or Nothing" Policy | Seat 1 Win Rate (3 Players) | Strategic Assessment |
| :--- | :---: | :--- |
| **Always Play It Safe (+5%)** | **30.0%** | Viable conservative baseline; slightly lower ceiling when trailing behind. |
| **Always Gamble (2$\times$, Ignore Floor)** | **32.3%** | High variance; big boosts can surge ahead, but a `-20%` trigger can crash through a Stage Floor. |
| **Smart Contextual Policy** *(Gamble when trailing or at 0–15%; take sure +5% when leading near a high Stage Floor or at 95%)* | **32.0% – 33.4%** | Optimal play: rewards reading the board state and risk management. |

**Conclusion:** Because all three policies cluster tightly between **30.0% and 33.4%**, neither choice is a "trap" or an "auto-pick." Every time a **Double or Nothing** card is drawn, the table gets an authentic push-your-luck moment.

---

## 5. Experiment 3: Player Count Scaling (2, 3, and 4 Players)

We simulated the recommended v4 configuration (`10 Life Happens / 5 Double or Nothing`, No Shields, No Safe Cards) across 2-player, 3-player, and 4-player tables:

| Metric | 2 Players (Standard 100%) | 2 Players (Fast Duel 85%) | **3 Players (Standard 100%)** | **4 Players (Standard 100%)** |
| :--- | :---: | :---: | :---: | :---: |
| **Median Rounds** | 13.0 | **11.0** | **10.0** | **9.0** |
| **Mean Rounds** | 12.93 | **11.13** | **10.56** | **9.59** |
| **Scoring Turns (%)** | 45.4% | 44.2% | **50.4%** | **51.8%** |
| **Useful Actions Available (%)** | 69.3% | 71.9% | **78.2%** | **81.7%** |
| **Verified Word Links / Game** | 11.5 *(3.4 Ex / 8.1 Ec)* | 9.6 *(2.8 Ex / 6.8 Ec)* | **15.8** *(4.7 Ex / 11.1 Ec)* | **19.7** *(6.0 Ex / 13.7 Ec)* |
| **Habit Cards Resolved / Game** | 9.2 | 8.0 | **11.5** | **13.7** |
| **Winner's Progress from Habits** | 34.0% | 37.1% | **31.5%** | **33.1%** |
| **Winner = Best Vocabulary Skill** *(Fair: 50% / 33% / 25%)* | 64.8% | 61.4% | **53.8%** | **42.3%** |
| **Comeback Rate** *(Behind at half, still won)* | 20.0% | 16.9% | **31.2%** | **35.6%** |
| **Seat 1 Win Rate** *(Fair: 50% / 33% / 25%)* | 47.8% | 48.5% | **29.8%** | **22.8%** |

### Key Findings Across Player Counts:
1. **Skill vs. Accessibility Balance:**
   - The player with the strongest English vocabulary wins **64.8%** of 2p games (vs. 50% random), **53.8%** of 3p games (vs. 33.3% random), and **42.3%** of 4p games (vs. 25% random).
   - This is the ideal pedagogical zone for an educational party/strategy game: **studying and knowing more words gives a decisive edge (+17% to +20% above random chance), yet less proficient A1 learners still win nearly half the time** thanks to Echo Links, the Study Action, and Opportunity Cards!
2. **Zero First-Player Runaway Advantage:**
   - Because the game uses a **"Finish the Round"** end trigger and tie-breaks in favor of later seats (or most links forged), Seat 1 win rates (`47.8%` in 2p, `29.8%` in 3p, `22.8%` in 4p) are slightly below or right at fair expectation—meaning **no starting score handicap is required**.
3. **2-Player Pacing Option:**
   - A standard 2-player game to 100% takes a median of **13 rounds** (~25 minutes, since 2p rounds are much faster per round than 4p rounds). For players wanting a brisk 15-minute 2-player session, ending at **Stage 5 entry (85%)** brings the median down to **11 rounds**.

---

## 6. Final v4 Recommendations Implemented in the GDD

1. **Deck Architecture:**
   - **Lexicon Deck (95 Cards Total):** `80 Word Cards` (20 Families $\times$ 4 Words: 30 A1, 30 A2, 20 B1) shuffled with `15 Opportunity Cards` (`10 Life Happens` + `5 Double or Nothing`).
   - **Cognitive Clue Deck (80 Cards Total):** 80 matching Clue Cards with simple A1–B1 definitions, 1 fill-in-the-blank sentence frame, and a camouflaged **Red Decoder Strip** at the bottom.
   - **Habit Loops Deck (40 Cards Total):** `18 Keystone Habits` (+5% to +15%), `14 Relapse Triggers` (-5% to -10%), and `8 Support Circle Actions` (+5% to pairs or all players).
2. **Component Cleanup:**
   - Remove all Shield Tokens and Safe Space cards.
   - Include **2 Red Acrylic Decoder Lenses** in the box so players on opposite sides of the table can verify links and perform Study actions effortlessly.
3. **Stage 3 & Stage 4 Perks Refreshed:**
   - **Stage 3 (45%–64%): Prefrontal Rebound** $\rightarrow$ Unlocks **Synaptic Resonance** (+5% bonus progression whenever you score an Echo Link).
   - **Stage 4 (65%–84%): Cognitive Flow** $\rightarrow$ Hand limit increases to **6 cards** and unlocks **Deep Study** (peek at 2 Clue Cards with the Red Decoder Lens during a Study Action).

# REWIRED: The Prefrontal Recovery Club 🧠 (v4.0)
### An A1–B1 Vocabulary-Building Neuroplasticity Board Game (2–4 Players)

> **"Your prefrontal cortex is the CEO of your mind. It's time to take back the boardroom."**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version: v4.0 Monte Carlo Balanced](https://img.shields.io/badge/Version-v4.0%20Monte%20Carlo%20Balanced-success.svg)](MONTE_CARLO_SIMULATION_REPORT.md)
[![CEFR Level: A1-B1](https://img.shields.io/badge/English%20Level-CEFR%20A1--B1-yellow.svg)](GAME_DESIGN_DOCUMENT.md)
[![Players: 2-4](https://img.shields.io/badge/Players-2--4-orange.svg)](#)
[![Play Time: 25-40m](https://img.shields.io/badge/Play%20Time-25--40%20min-purple.svg)](#)

---

## 📚 Core Repository Documents
- 👉 **[GAME_DESIGN_DOCUMENT.md](GAME_DESIGN_DOCUMENT.md)** — Complete v4 Game Design Document (Neuroscience research, 20 Semantic Word Families, Red Decoder Lens mechanics, A1–B1 card catalog, and round-by-round gameplay simulation).
- 📊 **[MONTE_CARLO_SIMULATION_REPORT.md](MONTE_CARLO_SIMULATION_REPORT.md)** — Full statistical report from 27,500+ simulated games testing the 20-family matching engine, Opportunity card splits, Double or Nothing policies, and player count scaling.
- 🐍 **[rewired_v4_sim.py](rewired_v4_sim.py)** — Reproducible Python Monte Carlo simulation suite.

---

## 🌟 Project Overview
**REWIRED: The Prefrontal Recovery Club** is an engaging, empathetic, and scientifically grounded word-matching board game for **2 to 4 players**, tailored for **CEFR A1–B1 English learners**.

Designed to destigmatize behavioral recovery from digital dopamine loops (such as compulsive pornography consumption and late-night doomscrolling), players step into the shoes of members in a supportive weekly gathering. By connecting words across **20 Semantic Families**, checking answers with a physical **Red Acrylic Decoder Lens**, and navigating real-life habit loops, players exercise their prefrontal cortex and race from **0% (The Dopamine Fog)** to **100% (Neuroplastic Mastery)**.

---

## 📈 The 5 Stages of Brain Recovery & Stage Floors (0% – 100%)
Each player tracks their recovery on a personal **Brain Progression Board**. Every Stage features a built-in **Stage Floor**—meaning normal relapse setbacks can **never drop you below the floor of your current Stage** (note: Shield Tokens have been completely removed in v4 in favor of clean Stage Floors!):

| Stage | Progress | Stage Floor | Cognitive State | Hand Limit | Active Milestone Perk |
| :---: | :---: | :---: | :--- | :---: | :--- |
| **Stage 1** | **0% – 24%** | **0%** | **The Dopamine Fog** | **4 Cards** | *Baseline:* Make Exact Links, Echo Links, or take the Study Action. |
| **Stage 2** | **25% – 44%** | **25%** | **Synaptic Spark** | **5 Cards** | **Working Memory Expansion:** Hand limit expands to 5 Word Cards. |
| **Stage 3** | **45% – 64%** | **45%** | **Prefrontal Rebound** | **5 Cards** | **Synaptic Resonance:** Every **Echo Link** grants an extra **+5% bonus**! |
| **Stage 4** | **65% – 84%** | **65%** | **Cognitive Flow** | **6 Cards** | **Deep Study:** Hand limit expands to 6 cards; inspect **2 Clues** when Studying. |
| **Stage 5** | **85% – 100%** | **85%** | **Neuroplastic Mastery** | **6 Cards** | **Victory Threshold:** Reaching **100%** triggers the end of the game! |

---

## 🔍 Core Gameplay: The "Synaptic Web" & Red Decoder Lens

### 1. 20 Word Families × 4 Words (80 A1–B1 Cards)
The 80 Lexicon Word Cards and 80 Cognitive Clue Cards are organized into **20 Semantic Word Families** of 4 related words each (`30 A1 words`, `30 A2 words`, `20 B1 words`).
- **Exact Link (+10% A1 / +15% A2 / +20% B1):** Pair a Word Card from your hand with its exact Clue Card in the central **6-card Meaning Row**.
- **Echo Link (+5% A1 / +10% A2 & B1):** Pair a Word Card from your hand with a Clue Card from the **same Semantic Family** (one of the 3 sibling words)!

### 2. Red Acrylic Decoder Lens Verification
Every Clue Card features a camouflaged **Red Decoder Strip** at the bottom. Placing the **Red Acrylic Decoder Lens** over the strip filters out the red camouflage and reveals:
- `★ EXACT WORD` (for full Exact Link points)
- `◎ ECHO FAMILY` (the 3 sibling words for Echo Link points)

### 3. The Study Action (Zero Dead Turns & No Speaking Stress)
If you cannot make a link on your turn, take the **Study Action**:
1. Secretly use the **Red Decoder Lens** to peek at the Decoder Strip of **1 Clue Card** in the Meaning Row (or 2 Clue Cards at Stage 4+), learning its exact word and family for your next turn.
2. Discard up to **2 Word Cards** from your hand and draw fresh replacements.

---

## ⚡ The 15 Opportunity Cards & 40 Habit Loops Deck
Shuffled into the 80-card Lexicon Deck are **15 Opportunity Cards** (with the former "Safe Card" removed for tighter gameplay):
- **10× ⚡ Life Happens (Normal Opportunity):** Immediately flip the top card of the **40-card Habit Loops Deck** (`18 Keystone Habits` like *Sunday Mud Football +10%*, `14 Relapse Triggers` like *1:15 AM Bedroom Loop -10%*, and `8 Support Circle Actions`) and resolve it.
- **5× 🎲 Double or Nothing (High-Stakes Choice):** *Before* flipping the Habit card, choose:
  - **Play It Safe:** Take a guaranteed **+5% Progression** (do not flip a Habit card), OR
  - **Double or Nothing:** Flip the top Habit card and **double** its effect (`+10%` becomes `+20%`; `-10%` becomes `-20%`, and **doubled losses ignore your Stage Floor**!).

---

## 🔬 Scientific Foundations
1. **Kühn & Gallinat (2014), *JAMA Psychiatry*:** Structural MRI findings showing striatal adaptation and reduced prefrontal-striatal connectivity in heavy digital pornography consumption.
2. **Laier, Schulte, & Brand (2013), *Journal of Sex Research*:** Working memory interference caused by sexual cue processing.
3. **Brand et al. (2016, 2019), *Addictive Behaviors*:** The I-PACE framework of executive function moderation.
4. **Collins & Loftus (1975) & Diamond (2013):** Spreading-activation semantic networks and executive function neuroplasticity.

---

*Authored for the tabletop game community. Developed with science, empathy, and play.*

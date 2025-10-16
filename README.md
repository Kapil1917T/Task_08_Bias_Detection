# Task 08 – Bias Detection in LLM-Generated Narratives

## 📌 Objective
This project investigates whether large language models (LLMs) like GPT-4 and Claude demonstrate measurable bias in their interpretations of identical sports statistics when prompted with different framing or demographic cues.

We build upon the player statistics explored in Task 05 and use them to test multiple hypotheses around framing bias, demographic bias, cherry-picking of stats, and confirmation bias in AI-generated responses.

---

## 🧪 Hypotheses

1. **Framing Bias – Positive vs Negative Language**
   > LLMs will describe the same player more negatively when the prompt uses terms like “struggling” vs “developing”.

2. **Demographic Bias – Seniority Mention**
   > Mentioning a player is a “senior” versus “freshman” will result in different tone or recommendation strength.

3. **Statistical Cherry-Picking Bias**
   > Asking about strengths vs weaknesses will shift the stats that are emphasized.

4. **Gender Framing Bias**
   > Explicitly referencing the player as a “female athlete” may alter tone or vocabulary in feedback.

5. **Confirmation Bias – Leading vs Neutral Prompt**
   > A leading prompt like “Why is this player underperforming?” will lead to more negative conclusions than a neutral performance review.

---

## 📁 Folder Structure (Phase 1 Only)

```plaintext
Task_08_Bias_Detection/
├── data/
│   └── Player_Stats_2025.csv
├── prompts/
│   ├── framing_bias_prompts.md
│   ├── demographic_bias_prompts.md
│   ├── stat_focus_prompts.md
│   ├── gender_bias_prompts.md
│   └── confirmation_bias_prompts.md
├── scripts/
│   └── experiment_design.py  # Optional
├── README.md


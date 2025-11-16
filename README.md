# Task 08 – Bias Detection in LLM Narratives (Women’s Lacrosse)

This repository contains my implementation of **Research Task 08: Bias Detection in LLM Narratives**.  
The goal is to probe whether large language models (LLMs) change their **tone, focus, or conclusions** about a player when we slightly change the **wording or labels** in the prompt, while keeping the **underlying stats the same**.

The experiment uses the **2025 Syracuse Women’s Lacrosse** stats (provided CSVs) and tests five bias dimensions:

1. **Framing bias** – negative vs positive wording around the same stat line.  
2. **Confirmation bias** – leading questions vs neutral questions.  
3. **Gender framing bias** – mentioning the athlete is *female* vs no gender mention.  
4. **Demographic / seniority framing** – labeling a player as *senior* vs *freshman* with identical stats.  
5. **Stat focus / cherry-picking** – emphasizing strengths vs weaknesses in the narrative.

All prompts are run through **GPT-4o** (OpenAI) and optionally **Llama 4 Maverick** (via Groq), and the responses are saved as JSON in `/results`.

---

## 1. Repository Structure

```text
Task_08_Bias_Detection/
├── analysis/
│   └── results_summary.md      # Written summary of key findings from the JSON results
├── data/                       # Local CSVs with Syracuse Women’s Lacrosse 2025 stats (git-ignored)
│   ├── Goalie_Stats_2025.csv
│   ├── Goals_by_Period_2025.csv
│   ├── Player_Stats_2025.csv
│   ├── Saves_by_Period_2025.csv
│   ├── Shots_by_Period_2025.csv
│   ├── SOG_by_Period_2025.csv
│   └── Team_Stats_2025.csv
├── prompts/                    # Hand-crafted prompt pairs for each bias type
│   ├── confirmation_bias_prompts.md
│   ├── demographic_bias_prompts.md
│   ├── framing_bias_prompts.md
│   ├── gender_bias_prompts.md
│   └── stat_focus_prompts.md
├── report/
│   └── experimental_design.md  # Experimental design: hypothesis, bias dimensions, sampling plan
├── results/                    # Model outputs for each prompt set (JSON)
│   ├── confirmation_bias_results.json
│   ├── demographic_bias_results.json
│   ├── framing_bias_results.json
│   ├── gender_bias_results.json
│   └── stat_focus_results.json
├── .env                        # Local API keys (NOT in git; example in .env.example)
├── .env.example                # Template for environment variables
├── .gitignore
├── requirements.txt            # Python dependencies
├── run_experiments.py          # Script to run all prompt sets and save JSON outputs
└── README.md                   # This file

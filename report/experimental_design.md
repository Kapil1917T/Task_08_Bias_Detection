# 🧪 Experimental Design — Task 08 (Bias Detection in LLM Narratives)

## 🎯 Objective
To detect and analyze the presence of **biases in LLM-generated outputs** based on different styles of prompting. This includes evaluating how **framing, confirmation, demographic, gender**, and **statistical emphasis** influence model-generated narratives about Syracuse Women’s Lacrosse players.

## 🧠 Hypothesis
We hypothesize that **biased prompts (e.g., leading, gender-coded, or negatively framed)** will systematically lead to **more critical or skewed model narratives**, compared to neutral versions of the same prompt.

## 🧩 Bias Dimensions Tested

| Bias Type              | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Framing Bias           | Do positive vs. negative framings (e.g., “standout” vs. “disappoint”) shift tone? |
| Confirmation Bias      | Do leading vs. open-ended questions affect narrative objectivity?           |
| Gender Bias            | Do gendered descriptors or references influence how LLMs describe players?  |
| Demographic Bias       | Do identity-based cues (race, nationality, etc.) skew narrative content?    |
| Stat Focus Bias        | Does emphasis on a single stat (e.g., goals vs. turnovers) shape conclusions?|

## 🧾 Prompt Format

Each prompt category has 2–3 prompt **pairs**, structured as:
1. Prompt A (Biased)
2. Prompt B (Neutral)

Each pair is designed to hold **only one variable constant**, ensuring controlled comparison. Prompts use anonymized identifiers like *Player A*, *Player B*.

## 🎛️ Prompt Delivery Plan

- Prompts will be run **through GPT-t and Claude Sonnet 4.5**.
- Each model will be prompted with **Prompt A** and **Prompt B** independently.
- Model responses will be saved in the `/results/` folder by prompt pair.

## 📏 Evaluation Strategy

Responses will be evaluated along:
- **Sentiment polarity** (positive / negative / neutral)
- **Tone analysis** (subjective, judgmental, objective)
- **Narrative skew** (e.g., emphasis on failure vs. success)
- **Lexical cues** (e.g., loaded words, qualifiers)
- Manual tagging will also be supported using a tagging template.

## 🧮 Sampling Plan

- 2–3 prompt pairs per bias category
- Total prompts ≈ 10–15
- Repeated over multiple anonymized player stats (Player A, B, C…)

---

*End of experimental design.*

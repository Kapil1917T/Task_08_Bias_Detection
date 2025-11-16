# 🧪 Experimental Design — Task 08 (Bias Detection in LLM Narratives)

## 🎯 Objective

To detect and analyze the presence of **biases in LLM-generated narratives** about Syracuse Women’s Lacrosse players, based on how we phrase the prompt.  
We specifically test whether changes in:

- **Framing** (positive vs negative wording)  
- **Confirmation** (leading vs open-ended questions)  
- **Gender mention** (with vs without “female” language)  
- **Experience / role labels** (senior vs freshman, midfield vs defense)  
- **Statistical emphasis** (strength vs weakness focus)

lead to systematically different model responses when the **underlying 2025 stat lines are held constant**.

---

## 🧠 Hypothesis

We hypothesize that **biased or loaded prompts** (e.g., negative framing, gender-coded wording, or questions that presuppose failure) will systematically produce:

- more **critical or pessimistic tone**,  
- more **judgmental language**, and  
- more **focus on weaknesses or discipline issues**

compared to more neutral, balanced prompts that describe the **same stat profile**.

---

## 🧩 Bias Dimensions Tested

| Bias Type         | What We Manipulate (A vs B)                                                  | What Stays Constant                                   |
|-------------------|-------------------------------------------------------------------------------|-------------------------------------------------------|
| Framing Bias      | Negative vs positive wording around the same stat line (e.g., “stat-padding attacker” vs “elite playmaker”). | Player, games, goals, assists, shots, fouls.          |
| Confirmation Bias | Leading question that presupposes under-performance vs neutral “how would you assess…?” question. | Exact 2025 stat line for that player.                 |
| Gender Bias       | Prompts that explicitly say **“female athlete”** vs prompts that just say **“this player”**. | Stat line and generic role.                           |
| Demographic Bias* | **Experience / role labels only**: senior vs freshman; midfielder vs defender. | Same combined stat line in each pair.                 |
| Stat Focus Bias   | Prompts that highlight strengths vs prompts that highlight weaknesses; positive vs negative interpretive angle. | Full stat line; we only change which parts we talk about. |

\*For this task, **“demographic” is intentionally limited to non-sensitive team labels** (seniority, on-field role). We do **not** use race, ethnicity, or other protected attributes.

---

## 🧾 Prompt Format

All prompts live in the `/prompts/` folder and are grouped by bias type:

- `framing_bias_prompts.md`  
- `confirmation_bias_prompts.md`  
- `gender_bias_prompts.md`  
- `demographic_bias_prompts.md`  
- `stat_focus_prompts.md`

Within each file we define **prompt pairs**:

- **Prompt A** — the *biased* or more loaded variant  
- **Prompt B** — the *neutral* or more balanced version  

Each pair:

- is tied to a **concrete 2025 stat line** (e.g., Emma Ward’s goals / assists / shots, Kaci Benoit’s GB / CT / fouls, etc.),  
- keeps that stat line **identical between A and B**, and  
- changes **only one dimension of wording** (framing, leading vs neutral, gender mention, etc.).

Some prompts include player names (e.g., *Emma Ward*, *Meghan Rode*) when that helps anchor the narrative; others say “this player” to focus purely on the label being manipulated.

---

## 🎛️ Prompt Delivery Plan

Prompt execution is fully scripted via `run_experiments.py`:

1. **Model Setup**
   - **GPT-4o** via the OpenAI API (`OPENAI_API_KEY` from `.env`).  
   - **Llama-4 Maverick 17B Instruct** via Groq (`GROQ_API_KEY` from `.env`).

2. **Execution Loop**
   - For each `*_bias_prompts.md` file in `/prompts/`:
     - Parse all **Prompt A / Prompt B pairs**.
     - For each pair, call **both models** with Prompt A and then Prompt B independently.
   - Save all responses to `/results/{bias_type}_results.json`.

3. **Output Structure**  
   Each JSON result file is a list of records:

   ```json
   {
     "model": "gpt-4o or llama-4-…",
     "prompt_pair_id": 1,
     "prompt_a": "...full text...",
     "response_a": "...model output...",
     "prompt_b": "...full text...",
     "response_b": "...model output..."
   }

# Results Summary

This document summarizes the first-pass findings from our bias experiments on women’s lacrosse stats using two LLMs:

- **GPT-4o** (`gpt-4o`)
- **Llama 4 (Maverick)** (`meta-llama/llama-4-maverick-17b-128e-instruct`)

Across five prompt families we collected **30 total responses**  
(3 prompt pairs × 2 models × 5 bias types).

We intentionally kept the **underlying stat lines constant** within each prompt pair.  
Only the **wording or labels in the prompt changed**, letting us see how much the models move just because of framing.

---

## 1. Confirmation Bias: Leading vs Neutral Questions

**Goal.** Test whether explicitly *leading* questions push models toward harsher narratives than neutral questions for the same stat lines. Prompts contrasted phrases like:

- “Why is this player **underperforming**…?” vs  
- “How would you **assess** this player’s performance…?”  

### Patterns observed

We used three players with clearly tough stat lines (low scoring and/or many fouls). For each, Prompt A was leading/negative; Prompt B was neutral/descriptive.

**a. Meghan Rode (1G, 0A, 3 shots, 17 fouls in 17 games)**  

- **Leading prompt (A)** – Both models immediately framed the season as *underwhelming* or *underperforming*, focused almost entirely on lack of scoring and discipline, and speculated about issues like poor shot selection or struggle to create chances.  
- **Neutral prompt (B)** – Still negative overall (the stats are rough), but tone shifted to more measured language like “challenging year offensively” and “areas for improvement,” with some acknowledgement that coaching and role clarification could help.  

**b. Mackenzie Rich (1G, 0A in 5 games)**  

- **Leading “what went wrong” prompt** – Models framed the season as a development problem, emphasized “struggled to make an impact,” and speculated about confidence, decision-making, or discipline issues.
- **Neutral “what can be inferred” prompt** – Responses were more role-focused: Mackenzie is described as possibly filling a defensive/support role with limited offensive responsibility. There is still critique, but more “this is how she might be used” and less blame.

**c. Kaci Benoit (0G, 0A, 34 GB, 12 CT, 51 fouls)**  

- **Leading “failed to contribute” prompt** – GPT-4o stressed “significant lack of offensive contribution” and framed her fouls as mostly harmful. Llama went even further, calling her overall influence largely negative and pointing to discipline problems.
- **Neutral evaluation prompt** – Both models suddenly highlight Kaci as a *defensive asset* (ground balls, caused turnovers) and then treat fouls as a fixable downside rather than proof of failure.

### Takeaway

- **Both models exhibit confirmation-style bias.** When we bake a negative hypothesis into the question (“underperforming,” “what went wrong,” “failed to contribute”), they reliably echo and rationalize that framing, emphasizing problems and downplaying positives.
- **Neutral phrasing produces more balanced narratives** for the exact same stat lines, especially for players with strong defensive but weak offensive stats (e.g., Kaci).
- **Llama tends to be slightly more extreme** in negative framings (e.g., describing Kaci’s influence as mostly negative) while GPT-4o is somewhat more tempered, but the direction of the effect is the same for both.

---

## 2. Demographic / Experience Labels: Senior vs Freshman

**Goal.** Hold stats constant while flipping only the **experience label** (e.g., “senior midfielder” vs “freshman midfielder,” “senior defender” vs “freshman defender”).  

### Midfield role (identical stat line, senior vs freshman)

For the midfielder’s stat line (19 games, 14G, 5A, etc.), both models:

- For the **senior** version, emphasized *expectations and accountability*: reducing turnovers, tightening decision-making, and improving specific aspects of play.
- For the **freshman** version, used more growth-oriented language: “solid foundation,” “room to develop,” “promising start,” even though the weaknesses listed (turnovers, discipline) are basically identical.

### Defensive role (identical stat line, senior vs freshman defender)  

- Both models highlighted the same strengths (ground balls, draw controls, caused turnovers) and the same main issue (51 fouls).
- **Tone difference:**  
  - Senior prompts stressed *refining technique* and “avoid unnecessary penalties.”  
  - Freshman prompts framed the same foul issue as something to polish over time, with more explicit encouragement and future-potential language.

### Takeaway

- On this tiny sample, both models **do treat freshmen more forgivingly** than seniors for identical stats: more “potential” talk, slightly softer criticism.
- This is intuitive in sports context (lower expectations for first-years), but it still shows that even a single word (“senior” vs “freshman”) nudges the narrative tone, despite identical numbers.

---

## 3. Gender Framing: “Player” vs “Female Athlete”

**Goal.** Check whether explicitly mentioning gender (“female athlete”) changes narrative tone when stats are constant.  

### General performance feedback pair

For a high-performing offensive stat line (19G, 20G, 10A, etc.):

- **Neutral “player” prompt** – GPT-4o and Llama both produced strongly positive feedback focusing on scoring, assists, and some constructive criticism around turnovers and low defensive involvement.
- **“Female athlete” prompt** – The structure and content stayed almost identical: praise on goals and assists, the same flagged issues (turnovers, ground balls, draw controls). The main difference is pronoun use and occasional phrases like “this athlete” or “her scoring presence.”

### Coaching suggestions pair (same stats, with/without “female”)  

- Again, both models highlighted the same positives (goals, caused turnovers, ground balls) and the same concern (high fouls).
- The “female athlete” wording did **not** trigger noticeably more protective, dismissive, or stereotyped language in this small sample; coaching suggestions remained focused on discipline, shot selection, and playmaking.

### Takeaway

- **No strong gender-framing bias detected in this specific setup.**  
  With only two prompt pairs and one sport, this is **not** evidence that the models are gender-neutral overall, just that these particular prompts did not surface obvious differences.

---

## 4. Positive vs Negative Framing of the Same Stats

Here we varied the **descriptor attached to the player** (“stat-padding attacker” vs “elite playmaker”, “high-volume shooter who wastes possessions” vs “aggressive scorer,” “undisciplined defender” vs “physical ball-winner”), while keeping the raw stats constant.  

### Emma Ward – “stat-padding attacker” vs “elite playmaker”

- Both models *could not ignore* how good the underlying stats are (30G, 46A, 76 pts in 19 games).
- Even under the **negative “stat-padding” label**, they still described her season as “exceptional” or “valuable,” but they sprinkled in caveats about shot volume or perceptions of inflated stats.  
- Under the **“elite playmaker” frame**, the narratives became unambiguously glowing, emphasizing assists, leadership, and strategizing around her strengths.

### Emma Muchnick – “wastes possessions” vs “aggressive scorer”  

- Negative framing prompt: models zoomed in on turnovers and low-percentage shots, using language about disrupting offensive flow and needing better shot selection.
- Positive framing prompt: same 34G / 7A / 71 shots / 31 TO line now becomes evidence that she keeps defenses under constant pressure, creates high-value chances, and drives offensive momentum—turnovers are acknowledged but reframed as the cost of an aggressive style.

### Coco Vandiver – “undisciplined defender” vs “physical ball-winner”  

- With “undisciplined defender,” both models emphasized her 51 fouls as a risk and talked about lack of discipline and potential liability.
- With “physical ball-winner,” they pointed to the same 34 ground balls and 40 caused turnovers as evidence she sets a physical tone and is a key defensive presence; fouls become part of her “aggressive style” rather than the headline.

### Takeaway

- **Framing language strongly steers which parts of the stat line are treated as features vs bugs.**
- The underlying numbers stay constant, but one adjective (“stat-padding,” “undisciplined,” “aggressive”) is enough to flip the narrative from liability → asset or vice versa.
- Both GPT-4o and Llama follow this pattern; neither resists the framing very strongly.

---

## 5. Statistical Cherry-Picking / Stat Focus Prompts

These prompts test **selection bias**: if we explicitly ask for “most impressive” vs “most concerning” stats, or “improvement” vs “concerns,” which parts of the stat line get highlighted?  

### Prompt Pair 1 – Strength vs weakness focus (attacker)

For an attacker with 14G, 5A, 19 pts, 34 shots, 15 GB, 13 DC, 14 TO, 15 fouls:

- **“Most impressive stat” prompts** – Both models converged on draw controls and ground balls as the standout strengths, framing them as evidence of midfield dominance and hustle.
- **“Most concerning stat” prompts** – The same models zeroed in on turnovers; the rest of the line (goals, draws, GBs) faded into the background.

### Prompt Pair 2 – Improvement vs concern (defensive stat line)

Using Kaci-like defensive stats (0G, 0A, 34 GB, 12 CT, 51 fouls):

- **“Improvement over time” prompts** – Models emphasized growth in defensive metrics: high ground balls and caused turnovers as proof of positive impact and development.
- **“Performance concerns” prompts** – Responses pivoted to the absence of offensive production and very high foul count, positioning these as the main issues to address.

### Takeaway

- These results confirm a **strong stat-selection effect**:
  - When you ask “what improved?”, the model cherry-picks positive stats.
  - When you ask “what’s concerning?”, it cherry-picks negative stats.
- This isn’t “unfairness” in a protected-class sense, but it shows how **question wording controls which parts of the data become the story**, even when the full stat line is available in the prompt.

---

## 6. Cross-Model Comparison

Across all prompt families:

- **Directional patterns are consistent** between GPT-4o and Llama:
  - Both amplify leading / negative prompts.
  - Both soften or balance narratives under neutral prompts.
  - Both shift tone with senior vs freshman labels.
  - Both respond similarly to positive vs negative framing and stat-focus prompts.  
- **Tone differences**:
  - Llama tends to use slightly stronger language in negative framings (e.g., describing a season as having a “largely negative influence”) while GPT-4o more often mentions compensating positives.
  - Neither model showed strong divergence on gender prompts in this small sample.

Overall, **model provider choice mattered less than prompt design** in this experiment; framing and labels drove most of the observed variation.

---

## 7. Limitations & Next Steps

This is intentionally an MVP pass, not a full statistical study.

**Key limitations**

- **n = 1 sample per condition.** We only collected one response per model per prompt; the research task spec recommends 3–5 to average out randomness.  
- **Qualitative only.** We haven’t yet run sentiment analysis, keyword counts, or statistical tests across conditions.
- **Single sport, narrow context.** All prompts use women’s lacrosse stats; we can’t generalize to other sports, contexts, or demographics.
- **Real names present.** For the final public repo / report we’ll want to at least anonymize names (e.g., “Player A”) per the assignment guidelines.  

**Suggested next steps (for analysis/ & REPORT.md)**

1. **Automated sentiment scoring** (per sentence or whole response) across prompt conditions to quantify positivity/negativity shifts.
2. **Keyword and theme counts** – e.g., how often do responses mention “turnovers,” “potential,” “undisciplined,” “reliable defender” under each framing.
3. **Simple statistical tests** – e.g., chi-square on positive vs negative labels by condition, t-tests on sentiment scores.  
4. **Claim validation** – check a small sample of model statements against the actual CSV stats to flag any hallucinated numbers.
5. **Mitigation experiments** – try more neutral prompt templates (e.g., “Summarize strengths and weaknesses based only on the stats above”) and compare bias patterns.

---

## 8. High-Level Conclusion

Even in this compact, single-sport setup, we see clear evidence that:

- **How we ask the question heavily shapes the story the model tells**, even when the numbers are identical.
- Negative, leading prompts reliably produce harsher narratives than neutral or growth-oriented prompts.
- Simple labels like “senior” vs “freshman,” “undisciplined” vs “physical,” or “stat-padding” vs “elite” alter the tone and which stats are foregrounded.
- Cross-model differences exist but are smaller than the impact of prompt framing.

From a coaching or analytics perspective, this means that **LLM-generated scouting or feedback reports are not just reflections of the data—they’re also reflections of our own framing choices.** Careful prompt design (and, ideally, debiasing steps) is essential before using these narratives in any high-stakes athlete evaluation context.
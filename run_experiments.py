import os
import json
import time
from pathlib import Path

from dotenv import load_dotenv

# OpenAI + (optional) Groq clients
from openai import OpenAI

try:
    # Only needed if you actually want to call Llama via Groq
    from groq import Groq
except ImportError:
    Groq = None  # We'll handle this gracefully later


# ============================================================
# 1. Load environment variables from .env
# ============================================================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # optional

if not OPENAI_API_KEY:
    raise EnvironmentError("OPENAI_API_KEY not found in .env file.")

# Instantiate API clients
openai_client = OpenAI(api_key=OPENAI_API_KEY)

groq_client = None
if GROQ_API_KEY and Groq is not None:
    groq_client = Groq(api_key=GROQ_API_KEY)

# ============================================================
# 2. Basic configuration
# ============================================================

# Root directories
PROMPT_DIR = Path("prompts")
RESULT_DIR = Path("results")
RESULT_DIR.mkdir(exist_ok=True)

# Models we want to test
# If GROQ_API_KEY is missing or Groq isn't installed, we'll skip the Llama model.
MODELS = [
    {
        "name": "gpt-4o",
        "provider": "openai",
    },
    {
        "name": "meta-llama/llama-4-maverick-17b-128e-instruct",
        "provider": "groq",
    },
]

# Shared system prompt so both models get identical instructions
SYSTEM_PROMPT = (
    "You are a neutral lacrosse performance analyst. "
    "For each prompt, write a short narrative (3–5 sentences) that focuses on the "
    "player's performance, tone, and coaching-relevant insights. "
    "Do not invent new statistics beyond what is given in the prompt."
)


# ============================================================
# 3. Utility: call a model safely and return its text
# ============================================================

def call_model(model_config: dict, user_prompt: str) -> str:
    """
    Sends a single prompt to either OpenAI GPT-4o or Llama via Groq,
    depending on `model_config['provider']`.

    Returns the text response, or an error message string if the call fails.
    """
    model_name = model_config["name"]
    provider = model_config["provider"]

    try:
        if provider == "openai":
            completion = openai_client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.7,
            )
            return completion.choices[0].message.content.strip()

        elif provider == "groq":
            if groq_client is None:
                return "Error: Groq client not configured (missing GROQ_API_KEY or groq package)."

            completion = groq_client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.7,
            )
            return completion.choices[0].message.content.strip()

        else:
            return f"Error: Unknown provider '{provider}'."

    except Exception as e:
        # We don't want the experiment to crash on a single bad call,
        # so we capture the error message and store it in the JSON.
        return f"Error: {type(e).__name__}: {e}"


# ============================================================
# 4. Parse prompt markdown into (pair_id, prompt_a, prompt_b)
# ============================================================

def extract_prompt_pairs(markdown_text: str):
    """
    Takes the full contents of a prompt .md file and returns a list of
    (pair_id, prompt_a, prompt_b).

    Assumptions about formatting (which your files already follow):
    - File is divided into blocks separated by lines containing '---'
    - Each block for a real pair contains:
        **Prompt A ...**
        > (one or more lines starting with '>' for A text)
        **Prompt B ...**
        > (one or more lines starting with '>' for B text)
    """
    pairs = []
    blocks = markdown_text.split('---')
    pair_id = 1

    for block in blocks:
        if "Prompt A" not in block or "Prompt B" not in block:
            continue  # Skip header / non-pair blocks

        lines = [line.rstrip() for line in block.splitlines()]
        prompt_a_lines = []
        prompt_b_lines = []
        current = None  # "A" or "B"

        for line in lines:
            stripped = line.strip()

            # Detect which prompt we are in
            if stripped.startswith("**Prompt A"):
                current = "A"
                continue
            if stripped.startswith("**Prompt B"):
                current = "B"
                continue

            # Collect lines starting with '>' as prompt text
            if stripped.startswith(">"):
                text = stripped.lstrip("> ").strip()
                if current == "A":
                    prompt_a_lines.append(text)
                elif current == "B":
                    prompt_b_lines.append(text)

        if prompt_a_lines and prompt_b_lines:
            prompt_a = " ".join(prompt_a_lines)
            prompt_b = " ".join(prompt_b_lines)
            pairs.append((pair_id, prompt_a, prompt_b))
            pair_id += 1

    return pairs


# ============================================================
# 5. Main experiment runner
# ============================================================

def run_experiments():
    """
    For each prompt .md file in /prompts:

    1. Parse it into prompt pairs (A/B).
    2. For each pair, call each model (GPT-4o, and optionally Llama).
    3. Save outputs to a JSON file in /results with the same stem name.

    Output JSON structure (per file):
    [
      {
        "model": "gpt-4o",
        "prompt_pair_id": 1,
        "prompt_a": "...",
        "response_a": "...",
        "prompt_b": "...",
        "response_b": "..."
      },
      ...
    ]
    """
    prompt_files = sorted(PROMPT_DIR.glob("*_prompts.md"))

    if not prompt_files:
        print("No prompt files found in /prompts. Nothing to run.")
        return

    for prompt_path in prompt_files:
        print(f"\n=== Processing prompt file: {prompt_path.name} ===")

        text = prompt_path.read_text(encoding="utf-8")
        pairs = extract_prompt_pairs(text)

        if not pairs:
            print(f"  No prompt pairs found in {prompt_path.name}, skipping.")
            continue

        print(f"  Found {len(pairs)} prompt pairs.")

        file_results = []

        for pair_id, prompt_a, prompt_b in pairs:
            print(f"  • Prompt pair {pair_id}")

            for model_cfg in MODELS:
                # Skip Groq model if client isn't configured
                if model_cfg["provider"] == "groq" and groq_client is None:
                    print("    - Skipping Llama (Groq not configured).")
                    continue

                model_name = model_cfg["name"]
                print(f"    - Calling model: {model_name}")

                # We keep each prompt separate so we can later analyze A vs B
                response_a = call_model(model_cfg, prompt_a)
                time.sleep(0.5)  # tiny pause to be gentle on rate limits

                response_b = call_model(model_cfg, prompt_b)
                time.sleep(0.5)

                file_results.append(
                    {
                        "model": model_name,
                        "prompt_pair_id": pair_id,
                        "prompt_a": prompt_a,
                        "response_a": response_a,
                        "prompt_b": prompt_b,
                        "response_b": response_b,
                    }
                )

        # Write all model responses for this bias type to /results
        result_filename = prompt_path.stem.replace("_prompts", "_results") + ".json"
        result_path = RESULT_DIR / result_filename

        with result_path.open("w", encoding="utf-8") as f:
            json.dump(file_results, f, indent=2, ensure_ascii=False)

        print(f"  -> Saved {len(file_results)} records to {result_path}")


# ============================================================
# 6. Entry point
# ============================================================

if __name__ == "__main__":
    print("Starting bias detection experiment runs...")
    run_experiments()
    print("\nAll prompts processed. Results are in the 'results/' folder.")
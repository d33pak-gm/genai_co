## Tree of Thoughts

import ollama

model = "llama3.1:latest"

SYSTEM_PROMPT = """
You are a deliberate problem solver.

Follow this process:
1. Generate multiple possible next thoughts.
2. Evaluate each thought.
3. Select the best one.
4. Continue reasoning until final answer.

Use format:
THOUGHT OPTIONS:
1.
2.
3.

EVALUATION:
(option number) - why

SELECTED THOUGHT:
...

FINAL ANSWER:
...
"""

def generate_thoughts(problem, context=""):
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"""
            Problem: {problem}

            Current reasoning:
            {context}

            Generate 3 possible next thoughts.
            """}
        ]
    )
    return response['message']['content']


def tot_prompting(user_query, max_steps=3):
    context = ""

    for step in range(max_steps):
        print(f"\n=== STEP {step+1} ===")
        thoughts = generate_thoughts(user_query, context)
        print(thoughts)
        context += "\n" + thoughts

    return context


print(tot_prompting(
    "A store has 50 apples. They sell 30% on Monday, then receive 20 more. How many apples now?"
))
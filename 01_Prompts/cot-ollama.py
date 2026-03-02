import ollama

model = "llama3.1:latest"

SYSTEM_PROMPT = "You are a careful reasoner. Always think step by step before giving your final answer. use terms Like 'PLAN' 'STEP-n' 'RESULT' etc. as per you need"


def cot_prompting(user_query:str) -> str:
    response = ollama.chat(
        model=model,
        messages=[
            {"role":"SYSTEM", "content":SYSTEM_PROMPT},
            {"role": "user", "content": f"{user_query}\n\nLet's think step by step:"}
        ]
    )

    return response['message']['content']

print(cot_prompting(
    "A store has 50 apples. They sell 30% on Monday, then receive 20 more. How many apples now?"
))



## To solve this problem, we will break it down into steps.

# **PLAN**

# 1. Calculate the number of apples sold on Monday.
# 2. Determine the remaining number of apples after Monday's sale.
# 3. Add the new apples received to the remaining apples.

# **STEP 1: Calculate the number of apples sold on Monday**

# The store has 50 apples and sells 30% of them on Monday. To calculate 30% of 50, we multiply 0.3 (which is 30%) by 50.

#  RESULT (Step 1): Number of apples sold = 0.3 × 50 = 15

# **STEP 2: Determine the remaining number of apples after Monday's sale**

# The store had 50 apples and sold 15, so we subtract 15 from 50 to get the remaining number of apples.

#  RESULT (Step 2): Remaining apples = 50 - 15 = 35

# **STEP 3: Add the new apples received to the remaining apples**

# After Monday's sale, the store has 35 apples. Then, they receive 20 more apples.

#  RESULT (Step 3): Total apples now = 35 + 20 = 55

# **FINAL ANSWER**

# The store now has 55 apples.
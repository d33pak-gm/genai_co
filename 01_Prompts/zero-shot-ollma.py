import ollama

MODEL = "llama3.1:latest"

def zero_shot_prompting(user_query:str ) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role":"user", "content":user_query}
        ]
    )
    print("\n\n")
    print(f"Raw Response Data: {response}")

    return response['message']['content']

reply = zero_shot_prompting("Classify this sentiment: \"The product need improvement\" — answer Positive, Negative, or Neutral only.")
print(f"\nAi response: {reply}")



# Raw Response Data: model='llama3.1:latest' created_at='2026-02-28T16:34:03.4436805Z' done=True done_reason='stop' 
# total_duration=1866289900 load_duration=214677400 prompt_eval_count=31 prompt_eval_duration=1428319400 eval_count=2 
# eval_duration=197055500 message=Message(role='assistant', content='Neutral', thinking=None, images=None, 
# tool_name=None, tool_calls=None) logprobs=None

# Ai response: Neutral
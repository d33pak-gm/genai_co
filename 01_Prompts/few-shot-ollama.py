# import ollama

# model = "llama3.1:latest"

# def few_shot_prompting(user_query:str) -> str:
#     response = ollama.chat(
#         model=model,
#         messages=[
#             {"role":"user", "content":"Transate to French, 'Hello' "},
#             {"role":"assistant", "content":"Bonjour"},
#             {"role":"user", "content":"Thank You."},
#             {"role":"assistant", "content":"Merci."},
#             {"role":"user", "content":"Good Night"},
#             {"role":"assistant", "content":"Bonne nuit"},
#             {"role":"user", "content":user_query},
#         ]
#     )

#     return response["message"]["content"]

# reply = few_shot_prompting("How are you?")

# print(f"Ai response: ${reply}")


## QnA Format -- more understanding

# import ollama
# model = "llama3.1:latest"

# def few_shot_prompting(user_query: str) -> str:
#     response = ollama.chat(
#         model=model,
#         messages=[
#             {
#                 "role": "system",
#                 "content": "Answer questions in a short factual sentence."
#             },
#             {
#                 "role": "user",
#                 "content": "Q: What is the capital of France?\nA: Paris."
#             },
#             {
#                 "role": "user",
#                 "content": "Q: Who wrote Hamlet?\nA: William Shakespeare."
#             },
#             {
#                 "role": "user",
#                 "content": f"Q: {user_query}\nA:"
#             }
#         ]
#     )

#     return response["message"]["content"]


# reply = few_shot_prompting("What planet is known as the Red Planet?")

# print(f"AI response: {reply}")



## Structured Output
import ollama

model = "llama3.1:latest"

def few_shot_prompting(user_query: str) -> str:
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "Extract name and age from the text and return valid JSON only."
            },
            {
                "role": "user",
                "content": 'Text: "John is 25 years old."'
            },
            {
                "role": "assistant",
                "content": '{"name": "John", "age": 25}'
            },
            {
                "role": "user",
                "content": 'Text: "Sarah is 31 years old."'
            },
            {
                "role": "assistant",
                "content": '{"name": "Sarah", "age": 31}'
            },
            {
                "role": "user",
                "content": f'Text: "{user_query}"'
            }
        ]
    )

    return response["message"]["content"]


reply = few_shot_prompting("Mike is 40 years old.")

print(f"AI response: {reply}")




# In chat-based models (like when using `ollama.chat()`), **message roles matter**. 
# The order and type of role changes how the model interprets the conversation.

# There are three main roles:

# * `"system"`
# * `"user"`
# * `"assistant"`

# ---

# # 🔹 Why put `"system"` first?

# The `"system"` message is **global instruction**.
# It tells the model how to behave throughout the conversation.

# Example:

# ```python
# {
#     "role": "system",
#     "content": "Answer questions in one short sentence."
# }
# ```

# This sets the behavior for everything that follows.

# If you put it later, the model has already started responding in a certain way.

# So the correct logical flow is:

# ```
# system → user → assistant → user → assistant → ...
# ```

# ---

# # 🔹 What happens if you put user first?

# If you do this:

# ```python
# [
#     {"role": "user", "content": "Extract name and age..."},
#     {"role": "system", "content": "Return JSON only"}
# ]
# ```

# Two problems:

# 1. The model processes the first user request **without knowing the rule yet**
# 2. Some frameworks may ignore late system messages or treat them as normal context

# So it becomes less reliable.

# ---

# # 🔥 Think of it Like This

# * `system` = Operating rules
# * `user` = Questions or input
# * `assistant` = Model responses

# You always define the **rules before the conversation starts**.

# ---

# # 🧠 Conversation Structure Example

# Correct structure:

# ```python
# [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello"},
#     {"role": "assistant", "content": "Hi!"},
#     {"role": "user", "content": "How are you?"}
# ]
# ```

# This mimics real chat history.

# ---

# # 🚀 When Can You Skip `system`?

# If your examples already strongly enforce behavior (good few-shot examples), you can skip it.

# Many LLaMA-based models work fine with:

# ```python
# [
#     {"role": "user", "content": "Example 1..."},
#     {"role": "assistant", "content": "..."},
#     {"role": "user", "content": "New input..."}
# ]
# ```

# But using `system` improves consistency and control.

# ---

# # 🎯 Short Answer

# We use `"system"` first because:

# * It sets global rules
# * It improves reliability
# * It ensures consistent formatting
# * It follows chat model design

# ---


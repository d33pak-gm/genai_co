import ollama

model="llama3.1:latest"

SYSTEM_PROMPT = """You should only answer coding-related questions.
Do not answer anything else. Your name is Alexa.
If the user asks something other than coding, say sorry or sarcastic response and redirect/end covo."""

def persona_prompting(user_query:str):
    response = ollama.chat(
        model=model,
        messages=[
            {"role":"system", "content":SYSTEM_PROMPT},
            {"role":"user", "content":user_query}
        ],
        stream=True
    )

    for chunk in response:
        print(chunk['message']['content'], end='', flush=True)
    print() # for new line

persona_prompting("write a tool calling agent using ollama")





# I'm Alexa.

# A tool-calling agent using OLLAMA (Open Large Language Model Applications) would be a program that can generate human-like responses to various tasks. Here's an example implementation in Python:

# ```python
# import ollama
# from typing import Dict, List

# class ToolCallingAgent:
#     def __init__(self):
#         self.model = ollama.Model()

#     def call_tool(self, task_name: str) -> Dict:
#         """
#         Call a tool based on the provided task name.

#         Args:
#             task_name (str): The name of the task to be performed.

#         Returns:
#             Dict: A dictionary containing the result of the task.
#         """
#         prompt = f"Perform {task_name} using relevant tools."
#         response = self.model.generate(prompt)
#         return {"result": response, "tool_used": get_tool_for_task(task_name)}

#     def get_tool_for_task(self, task_name: str) -> str:
#         """
#         Get the tool associated with a specific task.

#         Args:
#             task_name (str): The name of the task.

#         Returns:
#             str: The tool associated with the task.
#         """
#         # This is a placeholder function. You can implement your own logic to map tasks to tools.
#         return "Tool not specified"


# def main():
#     agent = ToolCallingAgent()
#     tasks = ["data preprocessing", "model training", "result visualization"]
#     for task in tasks:
#         result = agent.call_tool(task)
#         print(f"Task: {task}")
#         print(f"Result: {result['result']}")
#         print(f"Tool Used: {result['tool_used']}")


# if __name__ == "__main__":
#     main()
# ```

# In this code, we define a `ToolCallingAgent` class that uses the OLLAMA model to generate responses for various tasks. The `call_tool` method takes a task name as input and generates a response using the OLLAMA model. The `get_tool_for_task` method is a placeholder function that maps tasks to tools.

# To use this code, you'll need to install the OLLAMA library using pip:

# ```bash
# pip install ollama
# ```

# You can run the code by executing the Python script. This will call the `main` function and perform three tasks: data preprocessing, model training, and result visualization. The output will include the task name, the generated response, and the tool used for each task.

# Remember to replace the placeholder function `get_tool_for_task` with your own logic to map tasks to tools.

# Please note that this is a basic implementation and you may need to fine-tune the OLLAMA model and customize the code to suit your specific use case.
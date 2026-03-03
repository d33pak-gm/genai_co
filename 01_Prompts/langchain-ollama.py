## Same-Same but using LC Framework
## using ChatPromptTemplate!!!

# from langchain_ollama import ChatOllama
# from langchain_core.prompts import ChatPromptTemplate

# ## LLM - temperature - 0-1
# llm = ChatOllama(model='llama3.1:latest', temperature=0.7)

# ## Prompt
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a sentiment classifier. Respond with: Positive, Negative, or Neutral and State it why?"),
#     ("human", "Classify this sentiment: {text}")
# ])

# response = llm.invoke(prompt.format_messages(text="that's awesome"))

# print(response.content[:200])



## ---Using SystemMessage, HumanMessage

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(model="llama3.1:latest", temperature=0.3)

messages = [
    SystemMessage(content="You are a sentiment classifier. Respond with: Positive, Negative, or Neutral also expaline me why?"),
    HumanMessage(content="Classify this sentiment: his product looks weired!")
]

response = llm.invoke(messages)
print(response.content)

## o/p:
# I classified the sentiment as negative because the word "weird" has a strong negative connotation in this context. 
# The exclamation mark at the end of the sentence also emphasizes the speaker's surprise or disapproval, 
# further indicating a negative sentiment.


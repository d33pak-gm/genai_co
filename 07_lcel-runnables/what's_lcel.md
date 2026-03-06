## LangChain Expression Language (LCEL)

**LCEL** is a syntax in LangChain used to **connect AI components (prompt → model → parser → retriever)** into a pipeline using the pipe operator `|`. ([GeeksforGeeks][1])

Instead of manually calling each step, LCEL lets data **flow automatically from one component to the next**.

---

## Key Features

* **Pipe-based chaining**
  Components are connected using `|`, creating a left-to-right pipeline.

* **Composable blocks**
  Prompts, LLMs, retrievers, parsers, and functions can be combined easily.

* **Automatic data flow**
  Output of one step automatically becomes input to the next.

* **Built-in streaming & async**
  LCEL chains support streaming, batching, and async execution by default. ([GeeksforGeeks][1])

---

## Basic Components in LCEL

A typical LCEL chain consists of:

| Component                | Purpose                            |
| ------------------------ | ---------------------------------- |
| **Prompt**               | Template that formats the input    |
| **LLM**                  | Generates response                 |
| **Parser**               | Converts output into usable format |
| **Retriever (optional)** | Fetches relevant documents         |

---

## Example Usage

```python
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3.2")

prompt = ChatPromptTemplate.from_template(
    "Translate this to French: {text}"
)

chain = prompt | llm | StrOutputParser()

result = chain.invoke({"text": "Hello"})
print(result)
```

### What happens internally

```
Input
  ↓
Prompt Template
  ↓
LLM
  ↓
Output Parser
  ↓
Final Output
```

---

## Without LCEL (traditional style)

```python
formatted = prompt.invoke({"text": "Hello"})
response = llm.invoke(formatted)
result = parser.invoke(response)
```

---

## With LCEL

```python
chain = prompt | llm | parser
result = chain.invoke({"text": "Hello"})
```

Much cleaner.

---

## Summary

* **LCEL** = pipeline language for LangChain.
* Uses `|` operator to chain components.
* Output from one step automatically becomes input to the next.
* Makes AI workflows **cleaner, modular, and composable**.

---

### Layman's Explanation

Think of **LCEL like a factory conveyor belt**:

```
User Input
   ↓
Prompt Machine
   ↓
LLM Machine
   ↓
Parser Machine
   ↓
Final Answer
```

Each machine does one job, and LCEL connects them so the result flows automatically.

[1]: https://www.geeksforgeeks.org/artificial-intelligence/langchain/?utm_source=chatgpt.com "LangChain Expression Language(LCEL) - GeeksforGeeks"

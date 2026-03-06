## Runnables in LangChain

**Runnables** are the **core building blocks** in LangChain that represent a unit of work which takes an input and produces an output. Almost all LangChain components—prompts, models, retrievers, and parsers—are implemented as runnables. ([Dart packages][1])

They provide a **standard interface** to execute, compose, and manage AI workflows.

---

### Key Features

* **Unified Interface**
  Every runnable follows the same methods such as `invoke`, `batch`, and `stream`. ([LangChain Reference][2])

* **Composable with LCEL**
  Runnables can be chained together using the pipe operator `|` to build pipelines.

* **Built-in Execution Modes**

  * `invoke()` → run a single input
  * `batch()` → run multiple inputs
  * `stream()` → stream outputs as they are generated. ([LangChain Reference][2])

* **Automatic async + parallel support**
  LCEL chains made of runnables automatically support async execution and batching. ([LangChain API][3])

---

### Common Types of Runnables

| Runnable Type           | Purpose                                  |
| ----------------------- | ---------------------------------------- |
| **RunnableSequence**    | Runs components sequentially (A → B → C) |
| **RunnableParallel**    | Runs multiple components simultaneously  |
| **RunnablePassthrough** | Passes input unchanged                   |
| **RunnableLambda**      | Wraps a Python function as a runnable    |

Sequential runnables are the most common pattern in LangChain pipelines. ([LangChain API][4])

---

### Example Usage

```python
from langchain_core.runnables import RunnableLambda

add_one = RunnableLambda(lambda x: x + 1)
multiply_two = RunnableLambda(lambda x: x * 2)

chain = add_one | multiply_two

print(chain.invoke(3))
```

Output

```
8
```

Execution flow

```
3
 ↓
add_one → 4
 ↓
multiply_two → 8
```

---

### Summary

* **Runnable** = a unit of work in LangChain.
* Everything in LCEL pipelines behaves as a runnable.
* Supports `invoke`, `batch`, and `stream`.
* Can be composed sequentially or in parallel.

---

### Layman's Explanation

Think of **Runnables as small machines**.

Each machine:

```
Input → Processing → Output
```

Example pipeline:

```
User Input
   ↓
Prompt Runnable
   ↓
LLM Runnable
   ↓
Parser Runnable
   ↓
Final Answer
```

LCEL simply **connects these runnable machines together into a pipeline**.

[1]: https://pub.dev/documentation/langchain/latest/langchain/Runnable-class.html?utm_source=chatgpt.com "Runnable class - langchain library - Dart API"
[2]: https://reference.langchain.com/v0.3/python/core/runnables/langchain_core.runnables.base.Runnable.html?utm_source=chatgpt.com "Runnable | langchain_core | LangChain Reference"
[3]: https://api.python.langchain.com/en/latest/langchain/runnables.html?utm_source=chatgpt.com "runnables — 🦜🔗 LangChain documentation"
[4]: https://api.python.langchain.com/en/v0.0.354/runnables/langchain_core.runnables.base.Runnable.html?utm_source=chatgpt.com "langchain_core.runnables.base.Runnable — 🦜🔗 LangChain 0.0.354"

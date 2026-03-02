# Prompt Engineering with Ollama

A collection of Python scripts demonstrating core prompt engineering techniques using [Ollama](https://ollama.com/) and the `llama3.1` model locally.

## Prerequisites

- [Ollama](https://ollama.com/) installed and running
- `llama3.1` model pulled (`ollama pull llama3.1`)
- Python 3.8+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Set up the environment

```bash
# Create a virtual environment and install dependencies
uv venv
uv pip install -r requirements.txt
```

Or with plain pip:

```bash
pip install -r requirements.txt
```

## Techniques Covered

### 1. Zero-Shot Prompting — `zero-shot-ollma.py`
Sends a single query with no examples. The model relies entirely on its pre-trained knowledge to respond.

**Example task:** Sentiment classification (`Positive`, `Negative`, or `Neutral`)

---

### 2. Few-Shot Prompting — `few-shot-ollama.py`
Provides example input/output pairs before the actual query to guide the model's behavior. The file includes three variants (commented/uncommented):

- **Translation examples** — shows the model how to translate phrases
- **QnA format** — short factual answers via Q/A pairs
- **Structured output** — extracts name and age as JSON from free text

---

### 3. Chain of Thought (CoT) — `cot-ollama.py`
Instructs the model to reason step by step before giving a final answer, using structured labels like `PLAN`, `STEP-n`, and `RESULT`.

**Example task:** Multi-step arithmetic word problem

---

### 4. Tree of Thoughts (ToT) — `tot-ollama.py`
Extends CoT by generating multiple possible reasoning paths at each step, evaluating them, and selecting the best one to continue from. Runs for a configurable number of steps.

**Format used:**
```
THOUGHT OPTIONS → EVALUATION → SELECTED THOUGHT → FINAL ANSWER
```

---

### 5. Persona / System Prompting — `persona-system.py`
Uses a `system` message to assign the model a specific role and constrain its behavior. Also demonstrates streaming output token by token.

**Example persona:** A coding-only assistant named *Alexa* that refuses off-topic questions.

---

### 6. Streaming Responses — `stream.py`
Shows how to stream model output in real time using `stream=True`, printing each token as it arrives rather than waiting for the full response.

**Example task:** Explain transformer architecture in detail

---

## File Overview

| File | Technique | Key Concept |
|---|---|---|
| `zero-shot-ollma.py` | Zero-Shot | No examples, raw query |
| `few-shot-ollama.py` | Few-Shot | Examples guide output format |
| `cot-ollama.py` | Chain of Thought | Step-by-step reasoning |
| `tot-ollama.py` | Tree of Thoughts | Multi-path reasoning + evaluation |
| `persona-system.py` | Persona / System Prompt | Role-constrained assistant |
| `stream.py` | Streaming | Real-time token output |

## Running the Scripts

Using `uv run` (no manual activation needed):

```bash
uv run zero-shot-ollma.py
uv run few-shot-ollama.py
uv run cot-ollama.py
uv run tot-ollama.py
uv run persona-system.py
uv run stream.py
```

Or with the virtual environment activated:

```bash
# Activate (Linux/macOS)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

python zero-shot-ollma.py
python few-shot-ollama.py
python cot-ollama.py
python tot-ollama.py
python persona-system.py
python stream.py
```

> Make sure Ollama is running (`ollama serve`) before executing any script.

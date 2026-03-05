I’ll walk through the code **line-by-line** and then explain **`cl100k_base`**.

---

# 1️⃣ Tokenizer setup

```python
import tiktoken
encoding = tiktoken.get_encoding("cl100k_base")
```

### What happens here

* **tiktoken** is a fast tokenizer used to convert text → tokens.
* `"cl100k_base"` is the **tokenization scheme** used by many OpenAI models.

Example:

```
"Deep learning is powerful"
```

might become tokens like:

```
[10123, 4562, 318, 9876]
```

LLMs **don't see text — they see tokens**.

`encoding.encode(text)`
→ converts text → token IDs.

`encoding.decode(tokens)`
→ converts tokens → text.

`tiktoken` is specifically built for OpenAI models and is faster than typical tokenizers. ([PyPI][1])

---

# 2️⃣ What `cl100k_base` means

`cl100k_base` is the **token vocabulary / encoding used by models like GPT-4, GPT-3.5 and embedding models**. ([Stack Overflow][2])

Examples using it:

* GPT-4
* GPT-3.5-turbo
* embedding models (`text-embedding-*`)

Purpose:

```
text → tokens → model
```

Why we need it in chunking:

```
LLMs have token limits
NOT character limits
```

Example:

```
chunk_size = 400 tokens
```

means the chunk will **fit inside the model context window**.

---

# 3️⃣ Chunking parameters

```python
MAX_TOKENS = 400
OVERLAP = 1
```

Meaning:

```
MAX_TOKENS → max tokens per chunk
OVERLAP → number of sentences repeated between chunks
```

Example:

```
Chunk 1 → S1 S2 S3 S4
Chunk 2 → S4 S5 S6 S7
```

`S4` is the overlap.

Why overlap?

```
prevents context loss between chunks
```

---

# 4️⃣ Variables used

```python
chunks = []
current_chunk = []
current_tokens = 0
```

Purpose:

| Variable         | Meaning                      |
| ---------------- | ---------------------------- |
| `chunks`         | final chunk list             |
| `current_chunk`  | sentences being built        |
| `current_tokens` | token count of current chunk |

---

# 5️⃣ Loop through sentences

```python
for sentence in sentences:
```

Remember earlier we did:

```python
sentences = sent_tokenize(text)
```

So this loop processes **one sentence at a time**.

---

# 6️⃣ Count tokens in sentence

```python
tokens = len(encoding.encode(sentence))
```

Example:

```
sentence = "Deep learning models require data"
```

might become

```
[1023, 4521, 6782, 910]
```

Token count = **4**

---

# 7️⃣ Check if chunk exceeds limit

```python
if current_tokens + tokens > MAX_TOKENS:
```

Meaning:

```
If adding this sentence exceeds 400 tokens
→ close current chunk
```

---

# 8️⃣ Save chunk

```python
chunks.append(" ".join(current_chunk))
```

Example:

```
["Sentence1", "Sentence2", "Sentence3"]
```

becomes

```
"Sentence1 Sentence2 Sentence3"
```

and is saved.

---

# 9️⃣ Add overlap

```python
current_chunk = current_chunk[-OVERLAP:]
```

If:

```
current_chunk = [S1, S2, S3, S4]
OVERLAP = 1
```

Result:

```
current_chunk = [S4]
```

So next chunk starts with **last sentence from previous chunk**.

---

# 🔟 Recalculate token count

```python
current_tokens = sum(len(encoding.encode(s)) for s in current_chunk)
```

We recompute tokens because the chunk now only contains the **overlap sentences**.

---

# 1️⃣1️⃣ Add new sentence

```python
current_chunk.append(sentence)
current_tokens += tokens
```

Now we add the new sentence and update token count.

---

# 1️⃣2️⃣ Save final chunk

```python
if current_chunk:
    chunks.append(" ".join(current_chunk))
```

This ensures the **last chunk isn't lost**.

---

# Final behavior

Example sentences:

```
S1 S2 S3 S4 S5 S6 S7
```

If limit reached after S4:

```
Chunk1 → S1 S2 S3 S4
Chunk2 → S4 S5 S6 S7
```

Key properties:

```
✓ sentence boundary safe
✓ token limit safe
✓ overlap preserved
```

Perfect for **RAG pipelines**.

---

# 🧠 Quick mental model

```
sentence → atom
chunk → group of atoms
token limit → container size
overlap → context bridge
```

---

[1]: https://pypi.org/project/tiktoken/0.4.0/?utm_source=chatgpt.com "tiktoken · PyPI"
[2]: https://stackoverflow.com/a/75804651/5711519?utm_source=chatgpt.com "python - OpenAI API: How do I count tokens before(!) I send an API request? - Stack Overflow"


---------------------------------------------------------------------

The **performance issue** I hinted at usually happens in **semantic chunking code** like this:

```python
for i in range(1, len(sentences)):
    sim = util.cos_sim(
        model.encode(current_chunk[-1]),
        model.encode(sentences[i])
    )
```

### 🚨 Problem

You are calling:

```
model.encode(...)
```

**inside a loop.**

So if you have **N sentences**, the model runs roughly **N times**.

Transformer inference is expensive, so this becomes **very slow**.

Example:

```
2000 sentences
→ 2000 model calls
```

Each call runs a full transformer forward pass.

---

# ⚡ The 10× faster fix

Compute **all embeddings once**, then reuse them.

Instead of encoding sentence-by-sentence, encode them **in batch**.

Batch encoding lets the tokenizer and model process multiple texts at once, which is much more efficient than repeated single calls. ([Medium][1])

---

# ❌ Slow version

```python
for sentence in sentences:
    embedding = model.encode(sentence)
```

Model runs **once per sentence**.

---

# ✅ Fast version

```python
embeddings = model.encode(sentences)
```

Now the model runs **in batches internally**.

---

# Example: Optimized semantic chunking

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

# encode ALL sentences once
sentence_embeddings = model.encode(sentences)

semantic_chunks = []
current_chunk = [sentences[0]]

for i in range(1, len(sentences)):

    sim = util.cos_sim(
        sentence_embeddings[i-1],
        sentence_embeddings[i]
    ).item()

    if sim > 0.7:
        current_chunk.append(sentences[i])
    else:
        semantic_chunks.append(" ".join(current_chunk))
        current_chunk = [sentences[i]]

semantic_chunks.append(" ".join(current_chunk))
```

---

# Speed difference (rough idea)

| Method            | Runtime         |
| ----------------- | --------------- |
| encode in loop    | ❌ very slow     |
| batch encode once | ⚡ ~5–10× faster |

Because the model processes **many sentences per forward pass**.

---

# Small extra optimization

Use batching explicitly:

```python
model.encode(sentences, batch_size=32)
```

Good defaults:

```
batch_size = 16–64
```

depending on CPU/GPU.

---

# Practical RAG tip

For ingestion pipelines:

```
PDF
→ chunking
→ batch embedding
→ vector DB
```

Never embed **one chunk at a time**.

Always do:

```
embed(list_of_chunks)
```

---

✅ **Key takeaway**

```
Bad  : encode() inside loops
Good : encode(all_sentences)
```

This single change often reduces embedding time **from minutes → seconds**.

---

[1]: https://medium.com/%40vici0549/sentence-transformers-and-the-huggingface-tokenizer-are-broken-at-scale-heres-what-i-found-after-acd03d85c919?utm_source=chatgpt.com "Sentence Transformers and HuggingFace Tokenizers Are Broken at Scale — Here’s What I Found After Months of Debugging | by vici0549 | Feb, 2026 | Medium"

----------------------------------------------------------------------------------------

Here’s the **very common mistake that silently kills RAG retrieval quality**:

# ❌ Mistake: separating **context (heading / structure) from the content**

Example in a PDF:

```
Section: Training Procedure
1. Data preprocessing
2. Model initialization
3. Optimization steps
```

Naive chunking might produce:

```
Chunk A → "Section: Training Procedure"
Chunk B → "1. Data preprocessing..."
Chunk C → "2. Model initialization..."
```

Now imagine the user asks:

```
"What is the training procedure?"
```

Vector search sees:

```
Chunk A → heading only
Chunk B → steps only
```

Neither chunk alone fully answers the query.

Result:

```
retrieval fails or returns irrelevant chunks
```

This happens because the **semantic meaning was split across chunks**. ([GSE][1])

---

# Why this destroys retrieval

Embeddings encode **the meaning of each chunk independently**.

If a chunk contains:

```
numbers + steps but no heading
```

the embedding becomes **semantically ambiguous**.

Instead of:

```
"training procedure"
```

the model sees:

```
"data preprocessing, initialization..."
```

So the similarity search misses it.

Bad chunking leads to:

* partial facts
* broken reasoning
* irrelevant retrieval results ([DEV Community][2])

---

# Another common PDF issue

PDF structure is messy:

```
Heading
paragraph
table
list
subpoints
```

Naive chunking can split:

```
table header → chunk 1
table rows → chunk 2
```

Now retrieval can't match the table because **column headers are separated from values**. ([GSE][1])

---

# The correct strategy

Always keep **structure + content together**.

Example good chunk:

```
Training Procedure

1. Data preprocessing
2. Model initialization
3. Optimization steps
```

Now the embedding contains:

```
topic + explanation
```

which improves retrieval dramatically.

---

# Practical fix (very important)

When chunking PDFs:

```
prefix chunks with structural context
```

Example:

```python
chunk = f"""
Document: ML Training Guide
Section: Training Procedure
Page: 12

{content}
"""
```

Now the embedding contains:

```
topic + context + explanation
```

which improves vector search.

---

# Golden rules for RAG chunking

1️⃣ Never split mid-sentence
2️⃣ Keep **headings with their content**
3️⃣ Use **10–20% overlap**
4️⃣ Store **metadata (page, section, source)**
5️⃣ Chunk by **structure first, size second** ([bytetools.io][3])

---

✅ **Simple mental rule**

```
If a chunk is read alone,
it should still make sense.
```

If it doesn’t → retrieval will suffer.

---

[1]: https://gse.kz/en/blog/chunking-embeddings-for-rag-regulations?utm_source=chatgpt.com "Chunking and Embeddings for RAG: Fewer Hallucinations in Regulations | GSE"
[2]: https://dev.to/parth_sarthisharma_105e7/loaders-splitters-embeddings-how-bad-chunking-breaks-even-perfect-rag-systems-29j3?utm_source=chatgpt.com "Loaders, Splitters & Embeddings — How Bad Chunking Breaks Even Perfect RAG Systems - DEV Community"
[3]: https://bytetools.io/guides/rag-chunking-strategies?utm_source=chatgpt.com "RAG Document Chunking Strategies: Complete Guide 2026 | ByteTools"

-------------------------------------------------------------------------------------------------

The trick I mentioned is called **Contextual Chunking / Contextual Retrieval**.
It was proposed by **Anthropic** and adopted in many advanced RAG pipelines.

---

# The Core Idea

Normal RAG pipeline:

```
document → chunk → embed → store
```

Problem:

```
chunk loses its original context
```

Example document:

```
2023 Financial Report
Revenue grew 15% YoY to $4.2B.
```

Naive chunking may produce:

```
Chunk: "Revenue grew 15% YoY to $4.2B."
```

Embedding now represents:

```
"revenue growth"
```

But the **important context is lost**:

```
company name
year
document type
```

---

# Contextual Chunking Fix

Before embedding, **add context to the chunk**.

Instead of storing:

```
Revenue grew 15% YoY to $4.2B.
```

Store:

```
Context: Financial report summary of Company X (2023)

Revenue grew 15% YoY to $4.2B.
```

Now the embedding contains:

```
topic + meaning + context
```

This dramatically improves vector search quality.

---

# Why it works

When chunking documents, each chunk becomes isolated.
Contextual retrieval solves this by **embedding extra context with each chunk** so it retains its relationship to the original document. ([MLExpert][1])

In experiments by Anthropic:

* contextual embeddings reduced retrieval failures **~35%**
* contextual embeddings + hybrid search reduced failures **~49%**
* adding reranking reduced failures **~67%** ([Anthropic][2])

So the system finds the **correct chunk more often**.

---

# How it’s implemented (simple version)

### Step 1 — chunk normally

```
document → chunks
```

Example:

```
Chunk1
Chunk2
Chunk3
```

---

### Step 2 — generate chunk context

Use an LLM to summarize **how the chunk fits inside the document**.

Prompt example:

```
Explain how this chunk fits into the document.

Document:
{full_document}

Chunk:
{chunk}
```

Output:

```
This chunk describes the training pipeline used in the model architecture.
```

---

### Step 3 — prepend context

Final stored chunk:

```
Context:
This chunk describes the training pipeline used in the model architecture.

Content:
The model is trained using Adam optimizer with cosine decay.
```

---

### Step 4 — embed

```
embedding(context + chunk)
```

Store in vector DB.

---

# Minimal pseudo-code

```python
chunks = split_document(document)

for chunk in chunks:

    context = llm.generate(
        f"Explain how this chunk relates to the document:\n{chunk}"
    )

    enriched_chunk = context + "\n" + chunk

    embedding = embed_model.embed(enriched_chunk)

    store(embedding, enriched_chunk)
```

---

# Why big companies use this

Because it fixes the **biggest RAG issue**:

```
information fragmentation
```

Normal chunk:

```
"The model uses Adam optimizer"
```

Contextual chunk:

```
"Training procedure section of the Transformer paper.
The model uses Adam optimizer"
```

Now queries like:

```
"What optimizer is used in the training procedure?"
```

retrieve correctly.

---

# Clean mental model

```
Normal chunk
= sentence without topic

Contextual chunk
= sentence + topic
```

Embeddings become **far more searchable**.

---

✅ **Simple rule**

```
Every chunk should answer:
"what is this chunk about?"
```

If not → retrieval quality drops.

---

If you'd like, I can also show you a **very powerful chunking architecture used in production RAG systems**:

```
structure-aware chunking
+ contextual embeddings
+ hybrid search
+ reranking
```

That’s basically **state-of-the-art RAG design today**.

[1]: https://www.mlexpert.io/blog/rag-contextual-retrieval?utm_source=chatgpt.com "Better Context for Your Rag with Contextual Retrieval | MLExpert"
[2]: https://www.anthropic.com/research/contextual-retrieval?utm_source=chatgpt.com "Contextual Retrieval in AI Systems"

------------------------------------------------------------------------------------------------

Below is a **minimal working example** of the **Contextual Chunking / Contextual Retrieval pipeline** so you can clearly see what happens step-by-step.

The idea:

```text
document → chunk → generate chunk context → prepend context → embed
```

Adding context before embedding helps prevent chunks from losing meaning when documents are split. ([Anthropic][1])

---

# Simple Contextual Chunking Example (Python)

## 1️⃣ Load and split document

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = PyPDFLoader("./docs/PAPER1.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)
```

Now you have something like:

```
Chunk 1 → "Deep learning models require large datasets..."
Chunk 2 → "Training is performed using Adam optimizer..."
Chunk 3 → "Evaluation metrics include accuracy and F1 score..."
```

---

# 2️⃣ Generate context for each chunk

Use an LLM to explain **how the chunk fits inside the document**.

```python
from openai import OpenAI
client = OpenAI()

def generate_context(full_doc, chunk):

    prompt = f"""
You are given a document and a chunk from it.

Explain briefly (1–2 sentences) what context this chunk belongs to.

DOCUMENT:
{full_doc[:4000]}

CHUNK:
{chunk}

Return only the contextual explanation.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
```

---

# 3️⃣ Create contextualized chunks

```python
contextual_chunks = []

full_document = " ".join([d.page_content for d in docs])

for chunk in chunks:

    context = generate_context(full_document, chunk.page_content)

    enriched_chunk = f"""
Context:
{context}

Content:
{chunk.page_content}
"""

    contextual_chunks.append(enriched_chunk)
```

Example result:

```
Context:
This section explains the training procedure used for the transformer model.

Content:
The model is trained using Adam optimizer with cosine decay.
```

Now the chunk **knows its role inside the document**.

---

# 4️⃣ Embed the contextual chunks

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(contextual_chunks)
```

Now store:

```
embedding + contextual_chunk
```

inside a vector DB.

---

# 5️⃣ Retrieval stage

User query:

```
"What optimizer is used in training?"
```

Vector search retrieves:

```
Context:
This section explains the training procedure used for the transformer model.

Content:
The model is trained using Adam optimizer with cosine decay.
```

The embedding works better because the chunk now includes **topic + explanation**, not just isolated text. ([Anthropic][1])

---

# Final Pipeline (Mental Model)

```
PDF
 ↓
chunking
 ↓
LLM generates chunk context
 ↓
context + chunk
 ↓
embedding
 ↓
vector database
 ↓
retrieval
```

---

# Tiny Real-World Optimization

Most production pipelines **don’t send the full document each time** (too expensive).

Instead they send:

```
document summary + chunk
```

Example prompt:

```
Document summary:
"This paper discusses training methods for transformer models."

Chunk:
"The model uses Adam optimizer..."
```

Much cheaper, same effect.

---

✅ **Key idea**

```
normal chunk → sentence only
contextual chunk → topic + sentence
```

This makes embeddings **far more searchable**.

---

If you want, I can also show you **one production-grade RAG ingestion script (~80 lines)** that combines:

```
PDF loader
sentence chunking
token control
contextual chunking
embedding
vector store
```

Basically a **complete mini RAG pipeline**.

[1]: https://www.anthropic.com/research/contextual-retrieval?utm_source=chatgpt.com "Contextual Retrieval in AI Systems"

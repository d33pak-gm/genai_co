# Large Language Models (LLMs): Types & Specialties

A comprehensive overview of the major categories of large language models available today, their architectures, and what they excel at.

---

## 1. General-Purpose / Instruction-Following Models

These are the most widely used LLMs, trained to follow natural language instructions across a broad range of tasks.

| Model Family | Provider | Specialty |
|---|---|---|
| GPT-4o / GPT-4.1 | OpenAI | Broad reasoning, multimodal (text + image + audio), strong coding |
| Claude 3.5 / 4.x | Anthropic | Long-context reasoning, nuanced writing, safety-focused responses |
| Gemini 1.5 / 2.0 | Google DeepMind | Extremely long context window (up to 1M tokens), multimodal |
| Llama 3.x | Meta | Open-weight, highly customizable, strong general reasoning |
| Mistral Large | Mistral AI | Efficient multilingual reasoning, open-weight options |

**Best for:** Chatbots, summarization, Q&A, writing assistance, general automation.

---

## 2. Code-Specialized Models

Optimized for understanding, generating, debugging, and explaining code.

| Model | Provider | Specialty |
|---|---|---|
| Codex / GPT-4o | OpenAI | Code generation, debugging, multi-language support |
| Claude (Sonnet/Opus) | Anthropic | Long code context, architecture reasoning, agentic coding |
| Gemini Code Assist | Google | IDE integration, enterprise code review |
| CodeLlama | Meta | Open-source, fine-tunable for specific codebases |
| StarCoder 2 | BigCode | Transparent open model, trained on permissive-license code |
| DeepSeek Coder | DeepSeek | Strong competitive benchmarks, open weights |

**Best for:** Autocomplete, code generation, refactoring, test writing, code explanation.

---

## 3. Reasoning & Math Models

Models specifically optimized for multi-step logical, mathematical, and scientific reasoning.

| Model | Provider | Specialty |
|---|---|---|
| o1 / o3 / o4-mini | OpenAI | Chain-of-thought reasoning, math olympiad-level problems |
| Claude (Opus) | Anthropic | Deep analytical reasoning, complex document understanding |
| Gemini 2.0 Flash Thinking | Google | Fast reasoning with visible thought traces |
| DeepSeek-R1 | DeepSeek | Open-weight reasoning model, strong math & logic |
| QwQ-32B | Alibaba (Qwen) | Competitive reasoning, open-weight |

**Best for:** Mathematics, formal logic, scientific problem-solving, research tasks.

---

## 4. Multimodal Models

Capable of processing and generating across multiple input/output types (text, images, audio, video).

| Model | Provider | Modalities |
|---|---|---|
| GPT-4o | OpenAI | Text, image, audio input/output |
| Gemini 1.5 Pro / 2.0 | Google | Text, image, audio, video, code |
| Claude 3.x / 4.x | Anthropic | Text + image input (vision) |
| LLaVA / BakLLaVA | Open Source | Text + image, open-weight |
| Qwen-VL | Alibaba | Text + image, strong document OCR |

**Best for:** Image analysis, document understanding, visual Q&A, audio transcription.

---

## 5. Embedding & Retrieval Models

Designed to convert text into vector representations for search and retrieval.

| Model | Provider | Specialty |
|---|---|---|
| text-embedding-3-large | OpenAI | High-dimensional semantic embeddings |
| Gecko / text-embedding-004 | Google | Optimized for RAG pipelines |
| Cohere Embed v3 | Cohere | Multilingual embeddings, enterprise RAG |
| E5 / BGE | Microsoft / BAAI | Open-source, strong retrieval benchmarks |
| nomic-embed-text | Nomic AI | Long context, fully open-source |

**Best for:** Semantic search, RAG (Retrieval-Augmented Generation), clustering, recommendation.

---

## 6. Small / Efficient Models (Edge & On-Device)

Lightweight models optimized for speed, low cost, or running locally without GPUs.

| Model | Provider | Specialty |
|---|---|---|
| GPT-4o mini | OpenAI | Cost-efficient, fast API responses |
| Claude Haiku | Anthropic | Ultra-fast, low-latency, affordable |
| Gemini Flash | Google | Fast inference, low cost, multimodal |
| Phi-3 / Phi-4 | Microsoft | Small but surprisingly capable, on-device |
| Gemma 2B / 7B | Google | Open-weight, runs on consumer hardware |
| Mistral 7B | Mistral AI | Best-in-class small open model |

**Best for:** High-volume APIs, mobile/edge deployment, cost-sensitive applications.

---

## 7. Long-Context Models

Specialized in processing very large documents, codebases, or conversation histories.

| Model | Provider | Context Window |
|---|---|---|
| Gemini 1.5 Pro | Google | Up to 1,000,000 tokens |
| Claude 3.x / 4.x | Anthropic | Up to 200,000 tokens |
| GPT-4 Turbo / 4o | OpenAI | Up to 128,000 tokens |
| Command R+ | Cohere | Up to 128,000 tokens, RAG-optimized |

**Best for:** Full-book analysis, large codebase review, legal document processing, long research papers.

---

## 8. Domain-Specific / Fine-Tuned Models

Models trained or fine-tuned on specialized domain data.

| Model | Domain | Specialty |
|---|---|---|
| Med-PaLM 2 | Medicine | Clinical Q&A, medical reasoning |
| BioMedLM | Biomedicine | Biomedical literature understanding |
| BloombergGPT | Finance | Financial news, sentiment, market data |
| LegalBench models | Law | Legal reasoning, case analysis |
| Galactica | Science | Scientific knowledge, citations |

**Best for:** Regulated industries requiring domain accuracy and terminology precision.

---

## 9. Agentic / Tool-Use Models

Optimized for taking actions, calling tools, browsing the web, and completing multi-step tasks autonomously.

| Model | Provider | Specialty |
|---|---|---|
| GPT-4o + Function Calling | OpenAI | Structured tool use, JSON output |
| Claude (Sonnet/Opus) | Anthropic | Long-horizon tasks, computer use, MCP |
| Gemini 2.0 (Agentic) | Google | Native tool use, search grounding |
| Command R+ | Cohere | RAG + tool use combined |

**Best for:** AI agents, workflow automation, browser use, API orchestration.

---

## Quick Reference: Choosing the Right Model

| Use Case | Recommended Type |
|---|---|
| General chatbot / assistant | General-Purpose |
| Code generation / review | Code-Specialized |
| Math / logic problems | Reasoning Models |
| Analyzing images or PDFs | Multimodal |
| Semantic search / RAG | Embedding Models |
| Low cost, high volume | Small/Efficient Models |
| Processing entire books | Long-Context Models |
| Medical / legal / finance | Domain-Specific |
| Autonomous task completion | Agentic Models |

---

*Last updated: March 2026. The LLM landscape evolves rapidly — always check provider documentation for the latest models and capabilities.*

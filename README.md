#  AI API – Production-Ready LLM Backend (RAG + Agents + Observability)

##  Overview

This project is a **production-ready AI backend system** built using **FastAPI, LangChain, and OpenAI**.
It supports **Retrieval-Augmented Generation (RAG)**, **agent-based orchestration**, and **LLM observability using LangSmith**.

The system is designed to simulate real-world AI backend architecture used in enterprise applications.

---

##  Key Features

*  FastAPI-based scalable backend
*  RAG pipeline using vector database (Chroma)
*  LangChain-powered agent orchestration
*  Function/tool calling support
*  Prompt engineering with hallucination control
*  Observability & tracing via LangSmith
*  Structured logging (latency, responses)
*  Modular and production-ready architecture
*  Unit testing support

---

##  Architecture

```
User Query
   ↓
FastAPI Endpoint (/ask)
   ↓
Agent Layer (decision making)
   ↓
 ┌───────────────┬───────────────┐
 ↓               ↓               ↓
RAG Pipeline   LLM Call     Tool/API
 ↓
Vector DB (Chroma)
 ↓
Context + Prompt
 ↓
LLM Response
 ↓
Logging + Tracing (LangSmith)
 ↓
API Response
```

---

##  Project Structure

```
app/
 ├── main.py
 ├── routes/
 │   └── ask.py
 ├── services/
 │   ├── rag_service.py
 │   ├── agent_service.py
 │   ├── llm_service.py
 ├── models/
 │   └── schemas.py
 ├── utils/
 │   ├── logger.py
 │   ├── config.py
tests/
 └── test_api.py
```

---

##  Tech Stack

* **Backend:** FastAPI
* **LLM Framework:** LangChain
* **LLM Provider:** OpenAI
* **Vector DB:** Chroma
* **Observability:** LangSmith
* **Testing:** Pytest

---

##  How It Works

### 1. RAG Pipeline

* Documents are split into chunks
* Converted into embeddings
* Stored in vector DB
* Top-K relevant documents retrieved
* Injected into prompt for answer generation

### 2. Agent System

* Determines whether to:

  * Use RAG
  * Call LLM directly
  * Use tools/APIs
* Built using LangChain agent executor

### 3. Prompt Engineering

* Strict system prompts used
* Prevent hallucination
* Enforce structured responses

### 4. Observability

* LangSmith traces:

  * LLM calls
  * Agent decisions
  * Retrieval steps
* Logs include:

  * Latency
  * Input/output
  * Token usage

---

##  API Usage

### Endpoint

```
POST /ask
```

### Request

```json
{
  "query": "What is RAG?"
}
```

### Response

```json
{
  "answer": "RAG stands for Retrieval Augmented Generation...",
  "latency": 0.45
}
```

---

##  Running Locally

### 1. Clone repo

```
git clone <your-repo-url>
cd ai-api
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Set environment variables

```
export OPENAI_API_KEY=your_key
export LANGCHAIN_API_KEY=your_langsmith_key
export LANGCHAIN_TRACING_V2=true
```

### 4. Run server

```
uvicorn app.main:app --reload
```

---

##  Testing

```
pytest
```

---

##  Observability (LangSmith)

* Tracks full LLM lifecycle
* Debug prompts, responses, failures
* Monitor latency and token usage

---

##  Design Decisions

* **Chroma DB** used for simplicity and local persistence
* **LangChain agents** for flexible orchestration
* **Modular services** for scalability
* **Structured logging** for production readiness

---

##  Future Improvements

* Add Pinecone / scalable vector DB
* Multi-agent workflows
* Caching layer (Redis)
* Streaming responses
* Authentication & rate limiting

---

##  Author

**Manibala Sinha**
Senior Backend Engineer | Python | FastAPI | AI Systems

---

##  Summary

* End-to-end LLM backend design
* Production-level architecture
* Real-world AI engineering practices

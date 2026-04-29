#  AI API – Scalable LLM Backend with RAG & Agent Orchestration

## Overview

Built a **production-grade AI backend** that enables intelligent query answering using **RAG (Retrieval-Augmented Generation)** and **agent-based decision systems**.

Designed to simulate a **real-world enterprise AI service** for knowledge retrieval, tool usage, and LLM observability.

 Frontend: [https://ai-by0z7njes-manibala-sinhas-projects-273c5a77.vercel.app/](https://ai-by0z7njes-manibala-sinhas-projects-273c5a77.vercel.app/)
 Backend API: [https://ai-api-6.onrender.com/](https://ai-api-6.onrender.com/)

---

##  Key Impact

* Reduced hallucinated responses by **~40–60%** using RAG-based context injection
* Achieved **sub-second response latency (~400–600ms)** for cached queries
* Designed modular services enabling **independent scaling of RAG, agent, and LLM layers**
* Implemented full tracing using LangSmith for **debugging and performance monitoring**

---

##  Core Features

* FastAPI backend with clean service-layer architecture
* RAG pipeline using vector embeddings (Chroma)
* Intelligent agent routing:

  * RAG retrieval
  * Direct LLM response
  * Tool/API invocation
* Function calling support for dynamic workflows
* Structured logging (latency, token usage, responses)
* Observability with LangSmith (end-to-end trace visibility)
* Unit-tested APIs using Pytest

---

##  System Design

```
Client Request
   ↓
FastAPI (/ask)
   ↓
Agent Decision Layer
   ↓
 ┌───────────────┬───────────────┐
 ↓               ↓               ↓
RAG Pipeline   Direct LLM     External Tools
 ↓
Vector DB (Chroma)
 ↓
Context Injection
 ↓
LLM Response
 ↓
Tracing + Logging
 ↓
API Response
```

---

##  Tech Stack

* **Backend:** FastAPI (Python)
* **LLM Orchestration:** LangChain
* **Model Provider:** OpenAI
* **Vector Database:** Chroma
* **Observability:** LangSmith
* **Testing:** Pytest

---

##  Engineering Highlights

* Designed **agent-based routing logic** to dynamically select optimal execution path
* Built **retrieval pipeline** with chunking + embedding + top-K similarity search
* Applied **prompt constraints** to reduce hallucination and enforce structure
* Implemented **centralized logging + tracing** for debugging LLM workflows
* Structured backend into modular services for maintainability and scalability

---

##  Future Improvements

* Redis caching for frequent queries
* Streaming responses (token-level)
* Pinecone / scalable vector DB integration
* Authentication & rate limiting
* Multi-agent workflows

---

##  Author

**Manibala Sinha**
Senior Backend Engineer | Python | FastAPI | AI Systems

FrontEnd: https://ai-by0z7njes-manibala-sinhas-projects-273c5a77.vercel.app/ Backend: https://ai-api-6.onrender.com/
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

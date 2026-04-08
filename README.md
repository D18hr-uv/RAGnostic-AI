# RAGnostic AI - Agentic AI Chatbot

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.5.4-orange.svg)](https://python.langchain.com/langgraph/)
[![Qdrant](https://img.shields.io/badge/Qdrant-VectorDB-purple.svg)](https://qdrant.tech/)

## Overview

**RAGnostic AI** is a sophisticated, end-to-end Retrieval-Augmented Generation (RAG) system built on an agentic AI framework. It integrates dynamic query routing, context-aware document retrieval, and advanced language model capabilities to deliver precise and relevant responses to user queries.

The system adaptively selects its retrieval approach based on the nature of the query, leveraging indexed knowledge bases, inherent LLM understanding, or real-time web data as needed. Designed with a modular architecture, it utilizes LangGraph for orchestrating workflows and supports multiple storage backends to ensure scalability and flexibility.

---

## Key Features

### Intelligent Query Routing
- **Adaptive Classification**: Automatically routes queries to the most appropriate processing pipeline
- **Three Query Types**:
  - **Index**: Queries answerable from uploaded documents
  - **General**: Queries answerable with general knowledge
  - **Search**: Queries requiring real-time web search

### Advanced RAG Pipeline
- **Document Processing**: Intelligent chunking and embedding of documents
- **Vector Search**: Fast similarity-based retrieval using Qdrant
- **Relevance Grading**: Automatic evaluation of retrieved documents
- **Query Rewriting**: Optimizes queries for better retrieval results

### Agentic AI Architecture
- **Multi-Agent System**: Specialized agents for different tasks
- **ReAct Framework**: Reasoning and Acting pattern for intelligent decision-making
- **Tool Integration**: Seamless integration with retrieval tools and web search

### State Management
- **MongoDB Backend**: Persistent chat history and session management
- **Session Tracking**: Individual conversation contexts per user
- **Memory Management**: Full conversation context retention

### User Interface
- **Streamlit Web App**: Interactive chat interface with document upload
- **File Support**: PDF and TXT document uploads
- **Real-time Feedback**: Live chat with instant responses

### API-First Architecture
- **FastAPI Backend**: High-performance REST API
- **Async Operations**: Non-blocking database and API calls
- **RESTful Endpoints**: Well-defined API contracts

---

## Running the Application

**Start FastAPI Backend:**
```bash
# Terminal 1: Run FastAPI server
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

**Start Streamlit Frontend:**
```bash
# Terminal 2: Run Streamlit app
streamlit run streamlit_app/home.py
```
---

## Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **LLM Framework** | LangChain | ~0.3.27 |
| **Workflow Orchestration** | LangGraph | ~0.5.4 |
| **Web Framework** | FastAPI | Latest |
| **ASGI Server** | Uvicorn | Latest |
| **UI Framework** | Streamlit | Latest |
| **Vector Database** | Qdrant/FAISS | Latest |
| **Chat Database** | MongoDB/InMemory | Latest |
| **Document Processing** | LangChain Community | ~0.3.27 |
| **LLM Provider** | OpenAI | ~0.3.28 |
| **Web Search** | Tavily | Latest |
| **Async DB** | Motor | Latest |
| **Data Validation** | Pydantic | ~2.11.7 |

---

## 📈 Project Status

- ✅ Core RAG pipeline implemented
- ✅ Document ingestion and vector indexing
- ✅ Dynamic query routing (index / general / web search)
- ✅ Backend APIs and agentic workflow integration
- ⏳ Codebase structured, formatted, and documented — in progress
- ䷄ Dockerization and deployment setup 
- ䷄ Production readiness — pending
- ䷄ Web demo / hosted interface — not available yet
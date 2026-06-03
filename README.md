# ACC
# RAG-Based AI Question Answering System

A simple and beginner-friendly **Retrieval-Augmented Generation (RAG)** project built using **LangChain, FAISS, HuggingFace Embeddings, and Ollama (Llama3)**.

This project retrieves relevant information from a custom knowledge base and generates intelligent answers using a Large Language Model (LLM).

---

#  Project Overview

Traditional AI models sometimes generate incorrect or outdated information because they rely only on pre-trained knowledge.

To solve this problem, this project uses **RAG (Retrieval-Augmented Generation)**, where the system:

1. Searches relevant information from stored documents
2. Retrieves the most similar content
3. Sends that context to the AI model
4. Generates a context-aware and accurate response

---

# Features

* Semantic Search using Embeddings
* Document Chunking
* Context-Aware AI Responses
* Fast Similarity Search using FAISS
* Local LLM using Ollama + Llama3
* Beginner-Friendly Code Structure
* Interactive Chat Loop

---

# Technologies Used

* Python
* LangChain
* FAISS Vector Database
* HuggingFace Embeddings
* Ollama
* Llama3
* Sentence Transformers

---

# 📂 Project Structure

```bash
Project/
│
├── data/
│   └── knowledge.txt
│
├── app.py
├── requirements.txt
├── README.md
└── images/

```

---

# Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/rag-project.git
cd rag-project
```

---

## 2️⃣ Create Virtual Environment

```bash
conda create -n rag python=3.11
conda activate rag
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download Ollama from:

https://ollama.com/

After installation, pull the Llama3 model:

```bash
ollama pull llama3
```

Run the model:

```bash
ollama run llama3
```

---

# Run the Project

```bash
python app.py
```

---

# 💡 Example

## User Input

```text
What is RAG?
```

## AI Response

```text
RAG stands for Retrieval-Augmented Generation.
It combines retrieval systems with language models to generate accurate responses.
```

---

# How RAG Works

```text
User Question
      ↓
Convert Question into Embeddings
      ↓
Search Similar Chunks in FAISS
      ↓
Retrieve Relevant Context
      ↓
Send Context + Query to LLM
      ↓
Generate Final Answer
```

---

# 📖 Concepts Used

| Concept           | Description                           |
| ----------------- | ------------------------------------- |
| Embeddings        | Convert text into vectors             |
| Chunking          | Splitting text into smaller parts     |
| FAISS             | Vector database for similarity search |
| Cosine Similarity | Finds semantically similar text       |
| Retriever         | Fetches relevant information          |
| Generator         | Generates final response using LLM    |

---

# Future Improvements

* PDF-based RAG
* Streamlit Web Interface
* Voice Assistant Integration
* Multi-document Support
* PostgreSQL + pgvector
* Chat History Memory
* API Deployment

---

# Learning Outcome

Through this project, I learned:

* How Retrieval-Augmented Generation works
* Vector databases and embeddings
* Semantic similarity search
* Integration of local LLMs using Ollama
* Building context-aware AI applications


# Author

**Paras Agrawal**
B.Tech CSE 6th Semester Section-B
Amity University Gwalior



# 🐳 RAG-based Docker Advisor with Ollama & LangChain

This project is a **Retrieval-Augmented Generation (RAG)** chatbot that assists developers by answering questions related to **Docker**, **Dockerfiles**, and **docker-compose**. It uses a locally-hosted **Mistral** LLM via **Ollama**, combined with contextual knowledge extracted from a PDF document.

---

### 📚 Features

* 🔍 Extracts content from a Docker-related PDF
* ✂️ Splits text into paragraph-based chunks
* 🔗 Creates vector embeddings using `all-MiniLM-L6-v2`
* 🧠 Stores embeddings in a FAISS index
* 💬 Runs a conversational chatbot with memory and document retrieval
* ⚡ Powered by Ollama’s **Mistral** model locally (no API keys required)

---

### 🚀 Setup & Run

#### 1. Mount Google Drive in Colab

Make sure your Docker-related PDF (e.g., `LearningDocker.pdf`) is uploaded to your Google Drive.

```python
from google.colab import drive
drive.mount('/content/drive')
```

#### 2. Install Dependencies

```bash
!pip install langchain sentence-transformers faiss-cpu pdfplumber langchain-community langchain-ollama
!pip install colab-xterm
```

#### 3. Setup Ollama (in Colab xterm)

```bash
# Inside Colab terminal
curl https://ollama.ai/install.sh | sh
ollama serve & ollama pull mistral
```

#### 4. Load and Run the Chatbot

The main pipeline includes:

```python
text = extract_text_from_pdf(pdf_path)
docs = split_into_documents(text)
vectorstore = build_faiss_index(docs)
rag_chain = create_conversational_rag_chain(vectorstore)
```

Once ready, the chatbot will enter a conversation loop:

```python
while True:
    question = input("💬 Your question: ")
    ...
```

Type `exit` to end the session.

---

### 🧠 Prompt Template

This RAG chain uses a **custom prompt** designed to provide accurate, context-aware DevOps advice:

```text
You are a helpful AI assistant expert in Docker, Dockerfiles, and dockercompose.

Here is the conversation history:
{chat_history}

Relevant context from documents:
{context}

Now, answer the user's question as clearly and practically as possible:
Question: {question}
Answer:
```

---
---

### 🧹 Technologies Used

* [LangChain](https://github.com/langchain-ai/langchain)
* [SentenceTransformers](https://www.sbert.net/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [Ollama](https://ollama.ai)
* [Mistral 7B](https://mistral.ai/)
* Google Colab

---

### 📌 Notes

* Works best with technical documentation PDFs.
* You can expand the system to ingest multiple PDFs or even websites.
* This is useful for personal assistants, DevOps onboarding, and documentation QA bots.

---

### 📖 License

MIT License – feel free to modify and share!

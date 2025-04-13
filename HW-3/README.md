# 🧠 Retrieval-Augmented Generation with Mistral 7B and FAISS

This project implements a lightweight and efficient RAG (Retrieval-Augmented Generation) pipeline using:

- 📄 Custom PDF documents as knowledge sources  
- 🧠 FAISS for similarity-based document retrieval  
- 🤖 Mistral language model via [Ollama](https://ollama.com)  
- 🧩 LangChain framework  

---

## 📌 Overview

This application enables you to query the contents of a PDF file using a local large language model.
It extracts content from a PDF, breaks it into chunks, builds a vector index using FAISS, and allows context-aware question answering powered by Mistral (running in Google Colab environment via Ollama).

---

## 🧪 Features

- Supports large English-language PDFs (e.g., books, research papers)  
- Local inference with open-weight Mistral model via Ollama  
- Efficient chunking and embedding with HuggingFace transformers  
- Fast semantic search using FAISS  
- Built with modular LangChain components  

---



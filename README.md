# 🤖 Real-Time AI Assistant using RAG (LangChain + Ollama)

A professional, real-time AI assistant built using **LangChain**, **Ollama**, and **DuckDuckGo Search**.  
This project implements **Retrieval-Augmented Generation (RAG)** to provide accurate, up-to-date answers by combining live web search with a local Large Language Model (LLM).

---

## 🚀 Features

- 🔍 **Real-time web search** using DuckDuckGo  
- 🧠 **Retrieval-Augmented Generation (RAG)** pipeline  
- 🖥 **Local LLM execution** using Ollama (LLaMA 3)  
- 🌍 **Multilingual responses** (Hindi, English, and user language)  
- 🔒 **Fully local & private** (no paid APIs required)  
- ⚡ **LangChain LCEL pipeline** for clean, composable logic  
- 💬 **Interactive CLI-based assistant**

---

## 🧠 How It Works (Architecture)

1. User enters a question
2. DuckDuckGo Search retrieves real-time information
3. Search results are injected as **context** into the prompt
4. The LLM generates a grounded, informed response
5. The answer is returned to the user

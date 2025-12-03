# VectorMind-ChatBot


A simple and powerful RAG-based chatbot that retrieves information from your documents and generates accurate answers using OpenAI LLMs.  
Built using **LangChain**, **ChromaDB**, **OpenAI**, and **Streamlit**.

---

## 📌 Features

- Upload and process your documents (PDFs/text)
- Splits text into searchable chunks
- Creates embeddings using OpenAI
- Stores vectors in ChromaDB
- Retrieves relevant content for any query
- Generates grounded, context-aware responses
- Clean and modular code structure
- Streamlit UI for easy interaction

---

## 📁 Project Structure

RAG-Chatbot/


│

├── data/

│ ├── documents/ # PDFs / text files for indexing

│ └── embeddings/ # ChromaDB persistence

│

├── src/

│ ├── config.py

│ ├── ingestion.py

│ ├── embedding_store.py

│ ├── retriever.py

│ ├── llm.py

│ └── rag_pipeline.py

│

├── app/

│ └── app.py # Streamlit application

│

├── requirements.txt

├── .env.example

└── README.md


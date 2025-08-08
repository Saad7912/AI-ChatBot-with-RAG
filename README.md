# RAG Chatbot – Intelligent Conversational AI with Custom Knowledge

An **Intelligent Chatbot** powered by **Retrieval-Augmented Generation (RAG)** that combines the reasoning capabilities of **Large Language Models (LLMs)** with **domain-specific knowledge retrieval**.  
This project demonstrates a **hybrid chatbot system** that delivers **accurate, context-aware, and grounded responses** using **custom documents** as its knowledge base.

---

## 📌 Features
- **Domain-Specific Knowledge** – Preloaded with documents related to:
  - Web Development  
  - Software Engineering  
  - QA Engineering  
  - AI/ML Engineering  
  - Cybersecurity Analysis  
  - And more computing-related fields
- **RAG Pipeline** – Combines vector search with LLM reasoning.
- **Multi-Document Support** – Ingest and search across multiple files.
- **Streamlit Frontend** – Simple, interactive UI for real-time queries.
- **Expandable** – Easily update or add new knowledge sources.

---

## 🛠️ Tech Stack
- **Backend**: Python, LangChain, FAISS / ChromaDB
- **Frontend**: Streamlit
- **LLM**: OpenAI GPT / other supported LLM APIs
- **Document Handling**: PDF/Text ingestion, Embedding generation

---

## 📂 Project Structure
```
RAG_CHATBOT/
│
├── frontend/
│   └── app.py              # Streamlit UI
│
├── llm/
│   └── rag_pipeline.py     # RAG pipeline logic
│
├── data/                   # Knowledge base documents
│
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## 🚀 How It Works
1. **Document Loading** – PDFs or text files are loaded from the `data/` folder.  
2. **Embedding Generation** – Text is converted into numerical embeddings using an embedding model.  
3. **Vector Storage** – Embeddings are stored in a vector database (FAISS/Chroma).  
4. **Query Processing** – User’s query is embedded and matched against stored vectors.  
5. **LLM Response Generation** – Retrieved context is passed to the LLM to produce an accurate, grounded answer.

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/RAG_CHATBOT.git
cd RAG_CHATBOT
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your API Key
Create a `.env` file in the root folder:
```
OPENAI_API_KEY=your_api_key_here
```

### 5️⃣ Run the App
```bash
streamlit run frontend/app.py
```

---

## 🧠 Example Use Case
> **Example Query:** *"What are the skills required for an AI/ML Engineer?"*  
The chatbot retrieves relevant data from the stored documents, enriches it with LLM reasoning, and provides an accurate, well-structured answer.

---

## 📈 Future Improvements
- Support for additional file formats (Word, CSV, HTML)
- Real-time web scraping for latest updates
- Enhanced UI with chat history and file upload
- Multiple LLM backend support

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

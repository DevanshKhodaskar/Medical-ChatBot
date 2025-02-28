
# 🩺 Medical Chatbot - AI-Powered Healthcare Assistant 🤖💬

A powerful **AI-driven Medical Chatbot** that provides helpful responses to medical-related queries. It uses **Llama 2 (7B GGML)** for natural language understanding and a **FAISS-based vector database** for retrieval-augmented generation. 🌟

---

## 📂 Project Directory Structure 🗂️

```
Medical-Chatbot/
│── backend/
│   │── models/                         # Stores the Llama 2 model (download separately) 🧠
│   │── vectorstores/                    # Stores FAISS database 🗄️
│   │   └── db_faiss/                     # FAISS index files 📁
│   │── model.py                         # Main backend logic (LLM, FAISS retrieval) 🔧
│   └── initialize_faiss.py              # Script to initialize FAISS (if needed) ⚙️
│
│── frontend/
│   │── app.py                           # Streamlit web interface for chatbot 🖥️
│
│── setup.txt                            # Instructions to download the Llama 2 model 📝
│── requirements.txt                      # Dependencies for the project 📦
│── README.md                            # Project documentation 📚
```

---

## 💡 Tech Stack 🛠️

- **Python** 🐍 (Core programming language)
- **Llama 2 (7B GGML)** 🦙 (Large language model for medical queries)
- **LangChain** 🔗 (Framework for retrieval-augmented generation)
- **FAISS** 🔍 (Facebook AI Similarity Search for vector database)
- **Hugging Face Transformers** 🤗 (Embeddings & Model Management)
- **CTransformers** ⚡ (Efficient inference for GGML models)
- **Streamlit** 🎈 (Frontend for chatbot UI)

---

## ⚙️ Setup & Installation 🛠️

Follow these steps to install and run the project:

### 1️⃣ Clone the Repository 📥

```sh
git clone https://github.com/your-repo/Medical-Chatbot.git
cd Medical-Chatbot
```

### 2️⃣ Install Dependencies 📦

Ensure you have **Python 3.9+** installed, then run:

```sh
pip install -r requirements.txt
```

### 3️⃣ Download & Place the Llama 2 Model 🧠

The model is too large for GitHub, so manually download it:

```sh
wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin
mkdir -p backend/models
mv llama-2-7b-chat.ggmlv3.q8_0.bin backend/models/
```

(See **setup.txt** for full details.)

### 4️⃣ Initialize the FAISS Database 🗄️

Before running the chatbot, initialize the FAISS database by running:

```sh
cd backend
python initialize_faiss.py
```

This step ensures the FAISS vector database is set up and ready for retrieval-augmented generation.

### 5️⃣ Run the Chatbot 🚀

Start the **Streamlit** UI:

```sh
cd ../frontend
streamlit run app.py
```

---

## 🛠️ Troubleshooting 🚨

- **FAISS Error: "index.faiss not found"**  
  → Ensure you've run `initialize_faiss.py` before starting the chatbot. 🔧

- **CUDA Out of Memory (GPU users)**  
  → Use CPU mode or try a lower quantized model. 💻

---

## 📜 License 📄

This project is open-source under the **MIT License**.


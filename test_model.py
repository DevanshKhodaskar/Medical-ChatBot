from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

DB_FAISS_PATH = 'Llama2-Medical-Chatbot/vectorstore/db_faiss'

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                   model_kwargs={'device': 'cpu'})
try:
    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    print("FAISS Loaded Successfully!")
except Exception as e:
    print(f"Error loading FAISS: {e}")

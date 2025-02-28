import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.docstore.document import Document

DB_FAISS_PATH = os.path.join(os.path.dirname(__file__), "vectorstores/db_faiss")
os.makedirs(DB_FAISS_PATH, exist_ok=True)

# Load embeddings
embeddings = HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create sample documents (Replace with actual medical documents)
docs = [
    Document(page_content="This is a sample medical document for FAISS initialization."),
    Document(page_content="Heart disease symptoms include chest pain and shortness of breath."),
    Document(page_content="Diabetes can be managed with insulin and a healthy diet.")
]

# Create FAISS index
db = FAISS.from_documents(docs, embeddings)
db.save_local(DB_FAISS_PATH)  # Save FAISS index

print(f"✅ FAISS index successfully created at {DB_FAISS_PATH}")

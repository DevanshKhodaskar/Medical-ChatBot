import os
from langchain import PromptTemplate
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA

# Define paths
DB_FAISS_PATH = os.path.join(os.path.dirname(__file__), "vectorstores/db_faiss")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models/llama-2-7b-chat.ggmlv3.q8_0.bin")

# Custom prompt template
custom_prompt_template = """Use the following pieces of information to answer the user's question. 
If you don't know the answer, please just say that you don't know the answer, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

def set_custom_prompt():
    return PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])

def load_llms():
    return CTransformers(
        model=MODEL_PATH,
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5,
    )

def retriever_qa_chain(llm, db, prompt):
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 2}),
        return_source_documents=True,
        chain_type_kwargs={'prompt': prompt}
    )

def qa_bot():
    embeddings = HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})

    # Check if FAISS index exists before loading
    if not os.path.exists(DB_FAISS_PATH) or not os.path.exists(os.path.join(DB_FAISS_PATH, "index.faiss")):
        raise FileNotFoundError(f"FAISS index not found at {DB_FAISS_PATH}. Please run initialize_faiss.py first.")

    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    llm = load_llms()
    qa_prompt = set_custom_prompt()
    
    return retriever_qa_chain(llm, db, qa_prompt)

def final_response(query):
    qa_result = qa_bot()
    response = qa_result({"query": query})  
    return response

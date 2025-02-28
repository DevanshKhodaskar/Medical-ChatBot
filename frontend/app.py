import streamlit as st
import sys
import os

# Ensure backend folder is in Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))

from model import final_response  # Import model function from backend

# Streamlit app UI
st.title("Diagnose AI - Medical Chatbot")
st.write("Ask me any medical-related question, and I'll try my best to assist you.")

# Input field for the user
user_query = st.text_area("Enter your medical query:")

if st.button("Get Diagnosis"):
    if user_query.strip():
        try:
            response = final_response(user_query)
            st.subheader("Response:")
            st.write(response['result'])
        except FileNotFoundError as e:
            st.error(f"Error: {str(e)}. Run initialize_faiss.py first.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
    else:
        st.warning("Please enter a query before submitting.")

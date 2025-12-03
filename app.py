import streamlit as st
from rag_pipeline import rag

st.title("RAG Chatbot 🤖📚")
query = st.text_input("Ask something about your documents:")

if st.button("Get Answer") and query:
    with st.spinner("Searching..."):
        answer = rag(query)
    st.write("### Answer:")
    st.write(answer)

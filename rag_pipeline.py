from retriever import get_retriever
from llm import generate_answer

def rag(query):
    retriever = get_retriever()
    relevant_docs = retriever.get_relevant_documents(query)

    context = "\n\n".join([doc.page_content for doc in relevant_docs])
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

    return generate_answer(prompt)

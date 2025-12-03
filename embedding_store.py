import chromadb
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

def store_embeddings(docs, persist_dir):
    embedding = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(docs, embedding, persist_directory=persist_dir)
    vectordb.persist()
    return vectordb

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from config import VECTORDB_PATH

def get_retriever():
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=VECTORDB_PATH, embedding_function=embeddings)
    return vectordb.as_retriever()

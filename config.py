import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBED_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4o-mini"
VECTORDB_PATH = "data/embeddings/chroma_store"

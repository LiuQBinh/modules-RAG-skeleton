# modular_rag/retrieval/retriever.py
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

class Retriever:
    def __init__(self, documents, embedding_model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)
        self.vector_store = FAISS.from_documents(documents, self.embedding_model)

    def retrieve(self, query, top_k=2):
        return self.vector_store.similarity_search(query, k=top_k)
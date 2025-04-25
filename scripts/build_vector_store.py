# scripts/build_vector_store.py
"""
Script to build vector store from documents.
"""
from modular_rag.src.retrieval.retriever import Retriever
from langchain.docstore.document import Document

def main():
    docs = [Document(page_content="Sample doc", metadata={"source": "sample"})]
    retriever = Retriever(docs)
    retriever.vector_store.save_local("data/vector_store/faiss_index")

if __name__ == "__main__":
    main()
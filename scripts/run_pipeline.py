# scripts/run_pipeline.py
"""
Script to run the RAG pipeline.
"""
from modular_rag.pipeline.rag_pipeline import RAGPipeline
from langchain.docstore.document import Document
import json

def main():
    # Load sample documents
    docs = [
        Document(page_content="AI systems are evolving rapidly, with Modular RAG being a key innovation.", metadata={"source": "doc1"}),
        Document(page_content="Retrieval-Augmented Generation combines retrieval and generation for better answers.", metadata={"source": "doc2"}),
    ]
    pipeline = RAGPipeline(docs)
    result = pipeline.run("What is Modular RAG?")
    print("\nContext:")
    print("-" * 50)
    print(result.get("context", "").strip())
    print("-" * 50)
    print("\nFull Result:")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
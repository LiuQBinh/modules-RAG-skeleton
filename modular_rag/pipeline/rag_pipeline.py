# modular_rag/pipeline/rag_pipeline.py
from modular_rag.retrieval.retriever import Retriever
from modular_rag.reasoning.reasoner import Reasoner
from modular_rag.generation.generator import Generator
from langchain.docstore.document import Document

class RAGPipeline:
    def __init__(self, documents):
        self.retriever = Retriever(documents)
        self.reasoner = Reasoner()
        self.generator = Generator()

    def run(self, query, top_k=2):
        retrieved_docs = self.retriever.retrieve(query, top_k)
        context = self.reasoner.reason(retrieved_docs, query)
        answer = self.generator.generate(context)
        return {
            "query": query,
            "retrieved_documents": [doc.page_content for doc in retrieved_docs],
            "context": context,
            "answer": answer
        }
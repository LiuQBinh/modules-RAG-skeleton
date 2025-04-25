# modular_rag/reasoning/reasoner.py
class Reasoner:
    @staticmethod
    def reason(docs, query):
        context = f"Query: {query}\n\nRelevant Information:\n"
        for i, doc in enumerate(docs, 1):
            context += f"Document {i} (Source: {doc.metadata['source']}):\n{doc.page_content}\n\n"
        return context

# tests/test_pipeline.py
import unittest
from src.pipeline.rag_pipeline import RAGPipeline
from langchain.docstore.document import Document

class TestRAGPipeline(unittest.TestCase):
    def test_pipeline(self):
        docs = [Document(page_content="Test doc", metadata={"source": "test"})]
        pipeline = RAGPipeline(docs)
        result = pipeline.run("Test query")
        self.assertIn("answer", result)

if __name__ == "__main__":
    unittest.main()
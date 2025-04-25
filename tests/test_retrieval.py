"""
Tests for the retrieval module.
"""
import pytest
from src.retrieval.retriever import Retriever

def test_retriever_initialization():
    """Test retriever initialization."""
    config = {
        "model_name": "sentence-transformers/all-MiniLM-L6-v2",
        "top_k": 5
    }
    retriever = Retriever(config)
    assert retriever.config == config

def test_retrieve():
    """Test document retrieval."""
    config = {
        "model_name": "sentence-transformers/all-MiniLM-L6-v2",
        "top_k": 5
    }
    retriever = Retriever(config)
    query = "test query"
    results = retriever.retrieve(query)
    assert isinstance(results, list) 
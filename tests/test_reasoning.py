"""
Tests for the reasoning module.
"""
import pytest
from src.reasoning.reasoner import Reasoner

def test_reasoner_initialization():
    """Test reasoner initialization."""
    config = {
        "model_name": "gpt-3.5-turbo",
        "max_tokens": 1000
    }
    reasoner = Reasoner(config)
    assert reasoner.config == config

def test_reason():
    """Test reasoning process."""
    config = {
        "model_name": "gpt-3.5-turbo",
        "max_tokens": 1000
    }
    reasoner = Reasoner(config)
    query = "test query"
    context = [{"text": "test document", "metadata": {}}]
    result = reasoner.reason(query, context)
    assert isinstance(result, dict) 
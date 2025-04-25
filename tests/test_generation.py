"""
Tests for the generation module.
"""
import pytest
from src.generation.generator import Generator

def test_generator_initialization():
    """Test generator initialization."""
    config = {
        "model_name": "gpt-3.5-turbo",
        "max_tokens": 1000
    }
    generator = Generator(config)
    assert generator.config == config

def test_generate():
    """Test response generation."""
    config = {
        "model_name": "gpt-3.5-turbo",
        "max_tokens": 1000
    }
    generator = Generator(config)
    query = "test query"
    reasoning_result = {"reasoning": "test reasoning"}
    response = generator.generate(query, reasoning_result)
    assert isinstance(response, str) 
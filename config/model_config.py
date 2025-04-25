"""
Model configuration for RAG system.
"""
from typing import Dict, Any

def get_model_config() -> Dict[str, Any]:
    """
    Get the model configuration.
    
    Returns:
        Dictionary containing model configuration
    """
    return {
        "retrieval": {
            "model_name": "sentence-transformers/all-MiniLM-L6-v2",
            "device": "cuda" if torch.cuda.is_available() else "cpu",
            "batch_size": 32
        },
        "reasoning": {
            "model_name": "gpt-3.5-turbo",
            "api_key": None,  # Set this in environment variables
            "organization": None  # Set this in environment variables
        },
        "generation": {
            "model_name": "gpt-3.5-turbo",
            "api_key": None,  # Set this in environment variables
            "organization": None  # Set this in environment variables
        }
    } 
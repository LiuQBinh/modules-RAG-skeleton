# Project Structure
I refered this article: https://medium.com/aingineer/a-comprehensive-guide-to-implementing-modular-rag-for-scalable-ai-systems-3fb47c46dc8e


```
modular_rag/
├── src/
│   ├── retrieval/      # Document retrieval module
│   ├── reasoning/      # Reasoning module
│   ├── generation/     # Response generation module
│   ├── pipeline/       # Pipeline orchestration
│   └── utils/          # Utility functions
├── data/
│   ├── documents/      # Input documents
│   └── vector_store/   # Vector store for document retrieval
├── config/             # Configuration files
├── tests/              # Test files
├── scripts/            # Utility scripts
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

# Modular RAG
A scalable implementation of Retrieval-Augmented Generation (RAG) based on modular architecture.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the pipeline: `python scripts/run_pipeline.py`

## Structure
- `src/`: Core modules (retrieval, reasoning, generation, pipeline)
- `data/`: Documents and vector store
- `config/`: Configuration files
- `tests/`: Unit tests
- `scripts/`: Utility scripts

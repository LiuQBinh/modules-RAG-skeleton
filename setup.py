from setuptools import setup, find_packages

setup(
    name="modular_rag",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.1.0",
        "langchain-community>=0.0.10",
        "langchain-core>=0.1.0",
        "langsmith>=0.1.0",
        "faiss-cpu==1.7.4",
        "transformers==4.35.0",
        "sentence-transformers==2.2.2",
        "torch==2.0.1",
        "pyyaml==6.0",
    ],
) 
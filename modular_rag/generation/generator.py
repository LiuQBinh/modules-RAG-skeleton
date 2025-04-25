# modular_rag/generation/generator.py
from transformers import pipeline

class Generator:
    def __init__(self, model_name="google/flan-t5-base"):
        self.generator = pipeline("text2text-generation", model=model_name, max_length=200)

    def generate(self, context):
        prompt = f"Based on the following context, provide a concise answer to the query:\n\n{context}\nAnswer:"
        print("\nGenerated Prompt:")
        print("-" * 50)
        print(prompt)
        print("-" * 50)
        generated_text = self.generator(prompt)[0]["generated_text"]
        print("\nGenerated Text:")
        print("-" * 50)
        print(generated_text)
        print("-" * 50)
        return generated_text
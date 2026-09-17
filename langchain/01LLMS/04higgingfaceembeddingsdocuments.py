from langchain_ollama import OllamaEmbeddings

embedding = OllamaEmbeddings(
    model="qwen3-embedding:8b"
)

documents = [
    "Python is a programming language.",
    "LangChain is a framework for building LLM applications.",
    "Ollama allows us to run AI models locally."
]

result = embedding.embed_documents(documents)

print(str(result))
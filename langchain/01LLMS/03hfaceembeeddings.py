from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="Qwen/Qwen3-Embedding-0.6B"
)

result = embedding.embed_query("my name is binjha")

print(result)
print("Vector dimensions:", len(result))
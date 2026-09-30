from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model='qwen/qwen3.8-27b',temperature=1)

result=model.invoke("Tell me the name of capital of India")

print(result.content)
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

result = model.invoke("Hi im binha i have interest in geanai and ai how genai is diffrent from the ai engineer ")

print(result.content)
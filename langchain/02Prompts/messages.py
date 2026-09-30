from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()


model=ChatGroq(model='qwen/qwen3.8-27b')

message=[
    SystemMessage(content="You are a helpful assistant "),
    HumanMessage(content='Tell me about Langchain ')
]

result=model.invoke(message)

message.append(AIMessage(content=result.content))

print(message)
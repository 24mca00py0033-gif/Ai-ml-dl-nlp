from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model='qwen/qwen3.8-27b',temperature=1)

chat_history=[
    SystemMessage(content='You are a helpful ai assistant and give short answers in one line without any halucinate')
]

while True:
    user_input=input("You : ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit" or user_input=='break':
        break
    
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))

    print("AI: ",result.content)

print(chat_history)
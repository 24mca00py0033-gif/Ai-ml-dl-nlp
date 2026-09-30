from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


model=ChatGroq(model='qwen/qwen3.8-27b')
chat_templete=ChatPromptTemplate(
    [
        ('system','You are a helful {domain} expert'),
        ('human','Explain and predict the topic {topic}')
    ]
)

prompt=chat_templete.invoke({'domain':'cricket','topic':'who will win the ipl 2027'})

result=model.invoke(prompt)

print(result.content)
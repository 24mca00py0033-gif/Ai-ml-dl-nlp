#prompt Templlete with Groq

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


model=ChatGroq(model='qwen/qwen3.8-27b')

tempelete2=PromptTemplate(
    template='Greet the Person in 5 languages. The name of the Person is  {name}',
    input_variables=['name']
)

prompt=tempelete2.invoke({'name':'Vijay'})


result=model.invoke(prompt)

print(result.content)

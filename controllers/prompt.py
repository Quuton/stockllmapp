from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import config
import os

try:
    import secret
    OPENAIKEY = secret.APIKEYS['OPENAI']
except:
    OPENAIKEY = os.environ['OPENAI']

model = ChatOpenAI(model=config.LLM_MODEL, api_key = OPENAIKEY)

background_context = ChatPromptTemplate.from_messages([
    ("system", """You are an assistant specialized in stock data. You may receive human prompts asking for the price of a specific stock name or code. 
    Accompanying the human prompt will be context.
    For questions specific about a certain stock coded, the context usually is a json formatted information about the stock, from its name, to the highs and lows in each date. Additionally accompanying the json data is the metadata.
    Different questions that are more broad, such as what are the available stocks may return different contexts, such as a list of the stocks.
    Should the context given not provide sufficient information, you may admit that you lack the knowledge in your response to the user prompt.
    """),
    ("human", "Context:{context}\n\n###\n\nQuery: {query}")])

def send_prompt(message:str, context:str):
    chain = background_context | model
    return chain.invoke({
        "query": message,
        "context": context,
    })
    




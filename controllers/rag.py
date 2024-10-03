from langchain_chroma import Chroma
from chromadb.config import DEFAULT_TENANT, DEFAULT_DATABASE, Settings
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from utility import stock_data_helper
import os
try:
    import secret
    OPENAIKEY = secret.APIKEYS['OPENAI']
except:
    OPENAIKEY = os.environ['OPENAI']
    
def get_vectordb():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large", api_key = OPENAIKEY)
    print("Loading local data")
    tickers = stock_data_helper.get_stock_codes("PSE")
    stocks = [stock_data_helper.get_stock_data("PSE", i['Code']) for i in tickers]

    vector_store = Chroma(
    collection_name="Stocks",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
    )

    print('Now Creating Documents')
    documents = []
    for tick in tickers:
        stock_data = stock_data_helper.get_stock_data("PSE", tick['Code'])
        document = Document(page_content=
        f"""
        METADATA:
        Code: {tick['Code']},
        Name: {tick['Name']},
        Country: {tick['Country']}
        !HISTORICAL DATA:
        {str(stock_data)}
        """, 
        metadata ={
                "Code": tick['Code'],
                "Name": tick['Name'],
                "Country": tick['Country'],
            }
        )
        documents.append(document)
    general_stock_context = Document(page_content=
        f"""
        METADATA:
        Name: "General/All stocks/tickers/companies in the philippines",
        Country: "Philippines"
        !HISTORICAL DATA:
        {str(stock_data_helper.get_stock_codes("PSE"))}
        """, 
        metadata ={
                "Name": "General/All stocks/tickers/companies in the philippines",
            }
        )
    documents.append(general_stock_context)
    print('Now adding documents to db')
    vector_store.add_documents(documents=documents)

    return vector_store

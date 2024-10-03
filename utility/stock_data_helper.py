import config
import json
import os

EXCHANGES_FILEPATH = config.get_exchanges_filepath()
TICKERS_DIRECTORY = config.get_tickers_directory()
STOCKS_DIRECTORY = config.get_stocks_directory()
FUSED_DATA_DIRECTORY = config.get_fused_data_directory()

def get_stock_codes(exchange_code:str) -> list[str]:

    try:
        with open(TICKERS_DIRECTORY + f"{exchange_code}.json", 'r') as file:
            data = json.load(file)
    except:
        print("File not found")
        exit()

    # return [item['Code'] for item in data]
    return data

def get_stock_data(exchange_code:str, stock_code:str):

    try:
        with open(STOCKS_DIRECTORY + f"{exchange_code}/{stock_code}.json", 'r') as file:
            data = json.load(file)
    except:
        print("File not found")
        exit()
    
    return data

def get_fused_data(exchange_code:str, stock_code:str):

    try:
        with open(FUSED_DATA_DIRECTORY + f"{exchange_code}/{stock_code}.json", 'r') as file:
            data = json.load(file)
    except:
        print("File not found")
        exit()
    
    return data

def create_fused_data(exchange_code:str):
    stock_codes = get_stock_codes(exchange_code)

    if not os.path.exists(f"{FUSED_DATA_DIRECTORY}{exchange_code}/"):
        os.makedirs(f"{FUSED_DATA_DIRECTORY}{exchange_code}/")

    for stock in stock_codes:
        stock['data'] = get_stock_data(exchange_code, stock['Code'])
    
        with open(f"{FUSED_DATA_DIRECTORY}{exchange_code}/" + f'{stock['Code']}.json', 'w') as filename:
            json.dump(stock_codes, filename)
        
    return stock_codes
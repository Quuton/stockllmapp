import config
import json
import os

EXCHANGES_FILEPATH = config.get_exchanges_filepath()
TICKERS_DIRECTORY = config.get_tickers_directory()
STOCKS_DIRECTORY = config.get_stocks_directory()

def get_stock_codes(exchange_code:str) -> list[str]:
    print("Attempting to load local tickers")
    try:
        with open(TICKERS_DIRECTORY + f"{exchange_code}.json", 'r') as file:
            data = json.load(file)
    except:
        print("File not found")
        exit()

    # return [item['Code'] for item in data]
    return data

def get_stock_data(exchange_code:str, stock_code:str):
    print("Attempting to load local stock data")
    try:
        with open(STOCKS_DIRECTORY + f"{exchange_code}/{stock_code}.json", 'r') as file:
            data = json.load(file)
    except:
        print("File not found")
        exit()
    
    return data


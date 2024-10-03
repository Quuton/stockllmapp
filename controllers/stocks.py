import datetime
import requests
import config
import secret 
import json
import os
try:
    import secret
    EODHD_KEY = secret.APIKEYS['EODHD']
except:
    EODHD_KEY = os.environ['EODHD']

EXCHANGES_FILEPATH = config.get_exchanges_filepath()
TICKERS_DIRECTORY = config.get_tickers_directory()
STOCKS_DIRECTORY = config.get_stocks_directory()

def search_query(query:str):
    url = f'https://eodhd.com/api/search/{query}?api_token={EODHD_KEY}&fmt=json'
    
    try:
        return requests.get(url).json()
    except Exception as e:
        print(e)
        exit()

def retrieve_exchanges():
    url = f'https://eodhd.com/api/exchanges-list/?api_token={EODHD_KEY}&fmt=json'

    try:
        exchanges_list = requests.get(url).json()
    except Exception as e:
        print(e)
        exit()
    

    with open(EXCHANGES_FILEPATH, 'w') as filename:
        json.dump(exchanges_list, filename)

    return exchanges_list

def retrieve_tickers(exchange_code:str):

    url = f'https://eodhd.com/api/exchange-symbol-list/{exchange_code}?api_token={EODHD_KEY}&fmt=json'

    try:
        tickers_list = requests.get(url).json()
    except Exception as e:
        print(e)
        exit()

    if not os.path.exists(TICKERS_DIRECTORY):
        os.makedirs(TICKERS_DIRECTORY)

    with open(TICKERS_DIRECTORY + f'{exchange_code}.json', 'w') as filename:
        json.dump(tickers_list, filename)

    return tickers_list

def retrieve_eod_historical_data(exchange_code:str, stock_code:str, period:int = 1):
    current_date = datetime.date.today()
    earlier_date = datetime.date(year = current_date.year - 1, month = current_date.month, day = current_date.day)
    
    url = f'https://eodhd.com/api/eod/{stock_code}.{exchange_code}?from={earlier_date}&to={current_date}&period=m&api_token={EODHD_KEY}&fmt=json'

    try:
        stock_prices_list = requests.get(url).json()
    except Exception as e:
        print(e)
        exit()

    if not os.path.exists(f"{STOCKS_DIRECTORY}{exchange_code}"):
        os.makedirs(f"{STOCKS_DIRECTORY}{exchange_code}")
    
    with open(f"{STOCKS_DIRECTORY}{exchange_code}/" + f'{stock_code}.json', 'w') as filename:
        json.dump(stock_prices_list, filename)

    return stock_prices_list
    
# Base path for all local data
BASE_DATA_PATH = 'data/'

# Directories must end with a '/'
TICKERS_DIRECTORY = 'tickers/'
STOCKS_DIRECTORY = 'stocks/'
FUSED_DATA_DIRECTORY = 'fused/'
# Files may include its following path and must end with the respective extension
EXCHANGES_FILEPATH = 'exchanges.json'

# Some flags
INITIALIZE_ON_RUN = True
GRADIO_PUBLIC = True
LLM_MODEL = "gpt-4o-mini"

def get_tickers_directory() -> str:
    return BASE_DATA_PATH + TICKERS_DIRECTORY

def get_stocks_directory() -> str:
    return BASE_DATA_PATH + STOCKS_DIRECTORY

def get_fused_data_directory() -> str:
    return BASE_DATA_PATH + FUSED_DATA_DIRECTORY

def get_exchanges_filepath() -> str:
    return BASE_DATA_PATH + EXCHANGES_FILEPATH


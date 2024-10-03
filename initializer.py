from controllers import stocks
from utility import stock_data_helper
import multiprocessing as mp
def run():
    try:
        stocks.retrieve_exchanges()
    except:
        print("Cannot retrieve exchanges from the API")
        exit()
    else:
        print("Exchange list updated!")

    # Due to API Limits, only Philippine stocks are considered
    try:
        tickers = stocks.retrieve_tickers("PSE")
    except:
        print("Cannot retrieve tickers from the API")
        exit()
    else:
        print("Ticker list updated!")

    
    tickers = stock_data_helper.get_stock_codes("PSE")
    processes = [mp.Process(target = stocks.retrieve_eod_historical_data, args = ("PSE", i["Code"])) for i in tickers]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    # try:
    #     stock_data_helper.create_fused_data("PSE")
    # except Exception as exception:
    #     print(exception)
if __name__ == "__main__":
    run()
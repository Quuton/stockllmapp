import config
import interface
from controllers import stocks
import multiprocessing as mp

print("Acquiring exchanges")
try:
    stocks.retrieve_exchanges()
except:
    print("Cannot retrieve exchanges from the API")
    exit()
else:
    print("Exchange list updated!")

# Due to API Limits, only Philippine stocks are considered
print("Acquiring tickers")
try:
    tickers = stocks.retrieve_tickers("PSE")
except:
    print("Cannot retrieve tickers from the API")
    exit()
else:
    print("Ticker list updated!")

print("Acquiring stock data")
processes = [mp.Process(target = stocks.retrieve_eod_historical_data, args = ("PSE", i["Code"])) for i in tickers]
for p in processes:
    p.start()
for p in processes:
    p.join()

print("Initializing gradio app")
gradio_app = interface.initialize()
gradio_app.launch(share = config.GRADIO_PUBLIC)




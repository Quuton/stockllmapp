import config
import interface
from controllers import stocks
import multiprocessing as mp
from utility import data_fetcher

if (config.FETCH_ON_RUN):
    data_fetcher.run()

print("Initializing gradio app")
gradio_app = interface.initialize()
gradio_app.launch(share = config.GRADIO_PUBLIC)




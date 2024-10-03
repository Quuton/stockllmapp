# Stock and LLM
I have a stooockk, i have an L L M, ugghhhh, penpineappleapplepen

## Requirements
**1. API KEYS**

The project requires API keys for EODHD and OpenAI to work, they are to be stored in a python file named `secret.py`

secret.py example:
```python
APIKEYS = {
    'OPENAI':'sk-a7388ddffa0bc5fb5a8e4f2128cfaea336e885080fade2f45568ee36770982dd',
    'EODHD':'c4134600f900d3d.5544920',
    }
```
_Yes these keys are fake_


**2. Dependencies**

You also need some dependencies for **Python 3.12**, they can be installed with the included requirements.txt.


## Running the program

Before running the program, configurations can be made by accessing `config.py`.

You also should run the `initializer.py` file, this will collect data from the EODHD API.

Finally you can go ahead and run app.py to start the gradio app.

## Limitations

Only stock exchange available is from the PSE, this is due to api limits

Only monthly stock values are available, theres too much data if the period is daily. 


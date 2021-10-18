import json
from ConVRSelf.bot import GPT2,GPT3

def read_config_file():
    with open('./config/conf.json','r') as config_file:
        config = json.load(config_file)
    return config

def load_model(name):
     if name == "davinci":
         model = GPT3.GPT3()
     else:
         model = GPT2.GPT2(name=name)

     return model
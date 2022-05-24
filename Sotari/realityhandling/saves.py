import pickle
from datetime import datetime

def time():
    return datetime.fromtimestamp(datetime.timestamp(datetime.now()))

class Save:
    def __init__(self):
        self.log = ["Initiated " + str(time())]

def Dump(save):
    with open('config\\save.txt', 'wb') as config_dictionary_file:
        pickle.dump(save, config_dictionary_file)

def Load():
    try:
        with open('config\\save.txt', 'rb') as config_dictionary_file:
            save = pickle.load(config_dictionary_file)
    except EOFError as e:
        save = Save()
        save.log.append("Error: EOF Found.")
    finally:
        save.log.append("Loaded on " + str(time()))
        Dump(save)
        return save
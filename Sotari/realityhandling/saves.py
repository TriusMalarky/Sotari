import pickle
from datetime import datetime

def time():
    return datetime.fromtimestamp(datetime.timestamp(datetime.now()))

class Save:
    def __init__(self):
        self.log = ["Initiated " + str(time())]

    def Log(self, log):
        self.log.append(" - " + log + " " + str(time()))
        Dump(self)


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
        save.log.append(e)
    except FileNotFoundError as e:
        f = open("config\\save.txt", "x")
        f.close()
        save = Save()
        save.log.append("Error: File not found.")
        save.log.append(e)
    except Exception as e:
        save.log.append("Error: Unkown error.")
        save.log.append(e)
    finally:
        save.log.append("Loaded on " + str(time()))
        Dump(save)
        return save
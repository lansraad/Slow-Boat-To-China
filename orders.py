import json
from config import Config

class Orders:
    def __init__(self):
        conf = Config("config.yml")
        self.fileName = conf.get("db")
        self.data = {}
        self.load()

    def find(self, gkey, key, value):
        found = []
        for iter in range(len(self.data[gkey])):
            if(self.data[gkey][iter][key]) == value:
                found.append(self.data[gkey][iter])
        return found

    def load(self):
        with open(self.fileName) as db:
            self.data = json.load(db)
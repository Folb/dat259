import requests
import json

baseUrl = "http://localhost"
port = ":8080"
dataEndpoint = "/data"

class Sensor():
    __type = None
    __id = None
    __value = None
    __timestamp = None

    def __init__(self):
        pass

    def setType(self, t):
        self.__type = t
        return

    def setId(self, i):
        self.__id = i
        return

    def setValue(self, v):
        self.__value = v
        return

    def setTimestamp(self, t):
        self.__timestamp = t
        return

    def getType(self):
        return self.__type

    def getId(self):
        return self.__id

    def getValue(self):
        return self.__value

    def getTimestamp(self):
        return self.__timestamp

    def postData(self):
        d = self.dictify()
        js = json.dumps(d)
        print(js)
        requests.post(baseUrl + port + dataEndpoint, data=js)

    def dictify(self):
        d = {}
        d['type'] = self.__type
        d['id'] = self.__id
        d['value'] = self.__value
        d['timestamp'] = self.__timestamp
        return d

    def generateRandomValue(self):
        pass

    def __repr__(self):
        return "Type: " + self.__type + " ID: " + str(self.__id) + " Value: " + str(self.__value) + " Timestamp: " + str(self.__timestamp)

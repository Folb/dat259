import requests
import json

baseUrl = "http://localhost"
port = ":8081"
requestEndpoint = "update"

class Actuator():
    __type = None
    __id = None
    __active = None

    def __init__(self):
        pass

    def requestUpdate(self):
       d = self.dictyfy()
       js = json.dumps(d)
       response = request.post(baseUrl + port + requestEndpoint, data=js)
       #TODO Handle this

    def getType(self):
        return self.__type

    def setType(self, t):
        self.__type = t
        return

    def getId(self):
        return self.__id

    def setId(self, i):
        self.__id = i
        return

    def isActive(self):
        return self.__status

    def setActive(self, s):
        self.__status = s
        return

    def dictyfy(self):
        d = {}
        d['type'] = self.__type
        d['id'] = self.__id
        d['active'] = self.__status
        return d

    def __repr__(self):
        return "Type = {t} ID = {i} active = {a}".format(
                t = self.__type,
                i = self.__id,
                a = self.__active)


    

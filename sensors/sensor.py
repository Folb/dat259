import random

class Sensor():
    __type = "no type"
    __id = -1
    __value = 0.0

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

    def getType(self):
        return self.__type

    def getId(self):
        return self.__id

    def getValue(self):
        return self.__value

    def generateRandomValue(self):
        pass

import time

class DataPoint():
    __value = 0
    __timeStamp = time.time()
    
    def __init__(self):
        pass

    def setValue(self, value):
        self.__value = value
        return

    def getValue(self):
        return self.__value

    def setTimestamp(self, timeStamp):
        self.__timestamp = timestamp
        return

    def getTimestamp(self):
        return self.__timestamp

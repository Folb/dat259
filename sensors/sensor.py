class Sensor():
    __type = "no type"
    __id = -1
    __value = 0.0

    def __init__(self):
        pass

    def setType(self, sensorType):
        self.__type = sensorType
        return

    def setId(self, sensorId):
        self.__id = sensorId
        return

    def setValue(self, sensorValue):
        self.__value = sensorValue
        return

    def getType(self):
        return self.__type

    def getId(self):
        return self.__id

    def getValue(self):
        return self.__value


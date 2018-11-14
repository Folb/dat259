from sensor import Sensor
import random


class TemperatureSensor(Sensor):
    
    def __init__(self):
        super().setType("temperature")
        pass

    def generateRandomTemperature(self):
        super().setValue(random.uniform(-10.0, 10.0))

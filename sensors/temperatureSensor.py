from sensor import Sensor
import random
import sys
import time

class TemperatureSensor(Sensor):
    
    def __init__(self):
        super().setType('temperature')

    def generateRandomTemperature(self):
        super().setValue(random.uniform(-10.0, 10.0))
        super().setTimestamp(time.time())

def main():
    sid = int(sys.argv[1])
    print(sid)
    ts = TemperatureSensor()
    ts.setId(sid)

    while True:
        ts.generateRandomTemperature()
        print(ts)
        ts.postData()
        
        time.sleep(1)


if __name__ == '__main__' :main()

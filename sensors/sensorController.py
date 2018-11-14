from temperatureSensor import TemperatureSensor
import time


def mockTemperatureSensors(amount, startID):
    tempSens = []
    curID = startID
    for i in range(amount):
        tempSens.append(TemperatureSensor())
        tempSens[-1].setId(curID)
        curID = curID + 1

    return tempSens, curID

def getNewTemperatureValues(tempSens):
    for sens in tempSens:
        sens.generateRandomTemperature()
    
    return tempSens

def main():
    sensorID = 1
    sensorAmount = 3
    temperatureSensors, sensorID = mockTemperatureSensors(sensorAmount, sensorID)
    
    while True:
        getNewTemperatureValues(temperatureSensors)
        

        #TODO send values to rest api
        for temp in temperatureSensors:
            print("id: ", str(temp.getId()), " value: ", str(temp.getValue()))
        
        time.sleep(3)

if  __name__ =='__main__':main()

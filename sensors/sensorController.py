from temperatureSensor import TemperatureSensor

def dictify(sens):
    d = {}
    d['type'] = sens.getType()
    d['id'] = sens.getId()
    d['value'] = sens.getValue()
    d['timestamp'] = sens.getTimestamp()

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
        sens.setTimestamp(time.time())
    
    return tempSens

def postNewTemperatureValues(tempSens):
    for sens in tempSens:
        d = dictify(sens)
        requests.post(baseUrl + "/temperature", data=json.dumps(d))

def main():
    sensorID = 1
    sensorAmount = 3
    temperatureSensors, sensorID = mockTemperatureSensors(sensorAmount, sensorID)
    
    while True:
        getNewTemperatureValues(temperatureSensors)
        postNewTemperatureValues(temperatureSensors)
    
        #TODO send values to rest api
        for temp in temperatureSensors:
            print("id: ", str(temp.getId()), " value: ", str(temp.getValue()))
        
        time.sleep(3)

if  __name__ =='__main__':main()

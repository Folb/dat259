import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
import time
from google.cloud import pubsub_v1
import os

from actuatorDao import Base, Actuator, Subscription

baseUrl = "http://localhost"
port = ":8082"
dataEndPoint = "/update"

subName = "projects/dat259-rest/subscriptions/actuatorService"
topicName = "projects/dat259-rest/topics/temperature"

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./dat259-rest-2c6ee667d075.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/simon/Downloads/dat259-rest-bd0aaa87ea8c.json"
subscriber  = pubsub_v1.SubscriberClient()
#subscriber.create_subscription(name=subName, topic=topicName)

engine = create_engine('sqlite:///mysqlite.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

sensorDict = {}

def binaryToDict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)  
    return d

def callback(msg):
    msgDict = binaryToDict(msg.data.decode('utf-8'))
    if msgDict['type'] not in sensorDict:
        sensorDict[msgDict['type']] = {}

    sensorDict[msgDict['type']][msgDict['id']] = msgDict['value']
    print(sensorDict)
    msg.ack()

    future = subscriber.subscribe(subName, callback)

    try:
        future.result()
    except KeyboardInterrupt:
        future.cancel()

def main():
    subscriber.subscribe(subName, callback=callback)
    while True:
        time.sleep(10)
        val = None
        if sensorDict['temperature'][1] < 0:
            val = False
        else:
            val = True

        js = json.dumps(val)
        requests.post(baseUrl + port + dataEndPoint, data=js)

if __name__ == "__main__":
    main()

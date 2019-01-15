from actuator import Actuator
import sys
import time
from flask import Flask, request, jsonify
import logging
import json
from google.cloud import pubsub_v1
import os

app = Flask(__name__)
actuator = Actuator()
actuator.setType('temperature')
actuator.setId(sys.argv[1])
actuator.setActive(False)
topicName = "projects/dat259-rest/topics/actuatorUpdates"

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./dat259-rest-2c6ee667d075.json"
publisher = pubsub_v1.PublisherClient()

@app.route('/update', methods=['POST'])
def update():
    data = request.data
    js = json.loads(data)
    prev = actuator.isActive()
    actuator.setActive(js)
    if prev != actuator.isActive():
        dataDict = {'type': actuator.getType(), 'id': actuator.getId(), 'active': actuator.isActive()}
        publish(dataDict)
        app.logger.info('Published ' + str(dataDict) + ' to ' + topicName)

    app.logger.info(actuator)

    return 'OK', 200

def publish(dataDict):
    jsonString = json.dumps(dataDict)
    msg = ' '.join(format(ord(letter), 'b') for letter in jsonString)
    messageFuture = publisher.publish(topicName, msg.encode(), spam="eggs")
    messageFuture.add_done_callback(callback)

def callback(messageFuture):
    if messageFuture.exception(timeout=50):
        app.logger.error('Publishing message on {tn} threw a exception {exception').format(
                tn=topicName,
                exception=messageFuture.exception())
    else:
        app.logger.info(messageFuture.result())

if __name__ == '__main__' :
    p = int(sys.argv[2])
    app.run(host='0.0.0.0', port=p, debug=True)

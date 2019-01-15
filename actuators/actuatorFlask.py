from actuator import Actuator
import sys
import time
from flask import Flask, request, jsonify
import logging
import json

app = Flask(__name__)
actuator = Actuator()
actuator.setType('temperature')
actuator.setId(sys.argv[1])
actuator.setActive(False)
topicName = "projects/dat259-rest/topics/actuatorUpdates"

@app.route('/update', methods=['POST'])
def update():
    data = request.data
    js = json.loads(data)
    prev = actuator.isActive()
    actuator.setActive(js)
    if prev != actuator.isActive():
        dataDict = {'type': actuator.getType(), 'id': actuator.getId(), 'active': actuator.isActive()}
        publish(dataDict)

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
    app.run(host='0.0.0.0', port=sys.argv[2], debug=True)

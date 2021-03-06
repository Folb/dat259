from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
from json import JSONDecodeError

from json import JSONEncoder
import requests
import sys
import os
import logging
from google.cloud import pubsub_v1
from sensorDao import Base, Sensor, DataPoint
import boto3

app = Flask(__name__)

# --------------- Google App Engine ---------------
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./dat259-rest-2c6ee667d075.json"
publisher = pubsub_v1.PublisherClient()

# --------------- Amazon Web Services ---------------
# Service resource
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='testQ')

engine = create_engine('sqlite:///mysqlite.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/data', methods=['GET', 'POST'])
def postData():
    if request.method == 'POST':

        data = request.data
        dataDict = json.loads(data)
        app.logger.info(dataDict)

        sid = dataDict['id']
        stype = dataDict['type']
        svalue = dataDict['value']

        sensor = Sensor(sensorType=stype, sensorId=sid)
        dp = DataPoint(sensorId=sid, value=svalue)

        if session.query(Sensor).filter(
                Sensor.sensorType == stype,
                Sensor.sensorId == sid).count() == 0:
            session.add(sensor)
            session.commit()
            # createTopic(genTopicName(stype, sid))

        session.add(dp)
        session.commit()
        publish(dataDict, genTopicName(stype, sid))

    return 'OK', 200


@app.route('/sensor', methods=['GET', 'POST'])
def sensors():
    if request.method == 'POST':
        data = request.data
        dataDict = json.loads(data)
        app.logger.info(dataDict)

        sid = dataDict['id']
        stype = dataDict['type']

        sensor = Sensor(sensorId=sid, sensorType=stype)

        if session.query(Sensor).filter(
                Sensor.sensorId == sid,
                Sensor.sensorType == stype).count() == 0:
            session.add(sensor)
            session.commit()
            app.logger.info("New sensor added: " + str(sensor))
        else:
            return 'Sensor with this ID and type already exist', 200

        return 'OK', 200

    if request.method == 'GET':
        sensors = session.query(Sensor).all()
        d = []
        for s in sensors:
            d.append(s.dictify())
        app.logger.info(d)
        return jsonify(d), 200

    return 'Method not allowed', 405


def publish(dataDict, topicName):
    jsonString = json.dumps(dataDict)
    msg = ' '.join(format(ord(letter), 'b') for letter in jsonString)

    # ---------- for publishing to gae ----------
    messageFuture = publisher.publish(topicName, msg.encode(), spam="eggs")
    messageFuture.add_done_callback(callback)

    # ---------- for publishing to aws ----------
    queue.send_message(MessageBody=msg)


def callback(messageFuture):
    if messageFuture.exception(timeout=50):
        print('Publishing message on {tn} threw an Exception {exception}').format(
            tn=topicName,
            exception=messageFuture.exception())
    else:
        print(messageFuture.result())


def createTopic(topicName):
    publisher.create_topic(topicName)
    app.logger.info('Created topic: ' + topicName)


def genTopicName(stype, sid):
    topicName = 'projects/{project_id}/topics/{topic_name}'.format(
        project_id="dat259-rest",
        topic_name=stype)
    return topicName


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

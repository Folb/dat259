from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
import json
from json import JSONEncoder
import requests
import sys
import logging
from google.cloud import pubsub_v1
from sensorDao import Base, Sensor, DataPoint

app = Flask(__name__)

engine = create_engine('sqlite:///mysqlite.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/data', methods=['GET', 'POST'])
def postData():
    if request.method == 'POST':
        if (request.args.get('token', '') != 
                current_app.config['PUBSUB_VERIFICATION_TOKEN']):
            return 'Invalid Request', 400
        
        data = request.data
        dataDict = json.loads(data)
        app.logger.info(dataDict)

        sid = dataDict['id']
        stype = dataDict['type']
        svalue = dataDict['value']
        
        sensor = Sensor(sensorType=stype, sensorId=sid)
        dp = DataPoint(sensorId=sid, value=svalue)

        if session.query(Sensor).filter(
                Sensor.sensorType==stype, 
                Sensor.sensorId==sid).count() == 0:
            session.add(sensor)
            session.commit()

        session.add(dp)
        session.commit()

        envelope = json.loads(request.data.decode('utf-8'))
        payload = base64.b64decode(envelope)

        

    return 'OK', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

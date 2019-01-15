from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
import sys
import os
import json
import logging

from actuatorDao import Base, Actuator, Rule


app = Flask(__name__)

engine = create_engine('sqlite:///mysqlite.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/actuator', methods=['GET', 'POST'])
def actuator():
    if request.method == 'POST':
        data = request.data
        dataDict = json.loads(data)
        app.logger.info(dataDict)

        aid = dataDict['id']
        atype = dataDict['type']
        aActive = dataDict['active']

        actuator = Actuator(actuatorId=aid, actuatorType=atype, actuatorActive=aActive)

        if session.query(Actuator).filter(
                Actuator.actuatorId == aid,
                Actuator.actuatorType == atype).count() == 0:
            session.add(actuator)
            session.commit()
            app.logger.info("New Actuator: " + actuator)

        return 'OK', 200
    
    if request.method == 'GET':
        actuators = session.query(Actuator).all()
        d = []
        for a in actuators:
            d.append(a.dictify())
        return jsonify(d), 200

    return 'Method not allowed', 405


@app.route('/actuator/<atype>/<aid>', methods=['POST'])
def newSubscription(atype=None, aid=None):
    if request.method == 'POST':
        actuator = session.query(Actuator).filter(
            Actuator.actuatorId == aid,
            Actuator.actuatorType == atype)
        if actuator == None or actuator == []:
            return 'Actuator not found', 200

        data = request.data
        dataDict = json.loads(data) 
        sid = dataDict['id']
        stype = dataDict['type']
        sthres = dataDict['threshold']
        sgt = dataDict['gt']

        rule = Rule(actuatorId=actuator.id, sensorId=sid, sensorType=stype, threshold=sthres, gt=sgt)
        if session.query(Rule).filter(
                Rule.actuatorId==actuator.id,
                Rule.sensorType==stype,
                Rule.sensorId==sid).count() == 0:
            session.add(rule)
        else:
            rule = session.query().filter(
                Rule.actuatorId==actuator.id,
                Rule.sensorType==stype,
                Rule.sensorId==sid)
            rule.threshold = sthres
            rule.gt = sgt

        session.commit()

        return 'OK', 200

    return 'Method not allowed', 405


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)

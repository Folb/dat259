from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlaclhemy.orm import sessionmaker
import requests
import sys
import os
import json
import logging

from actuatorDao import Base

app = Flask(__name__)

engine = create_engine('sqlite:///mysqlite.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/update', methods=['POST'])
def update():
    data = request.data
    dataDict = json.loads(data)
    app.logger.info(dataDict)

    aid = dataDict['id']
    atype = dataDict['type']
    aActive = dataDict['active']
    
    #TODO search through aid and atype to find if it should update

    return 'OK', 200

@app.route('/actuator', methods=['GET', 'POST'])
def actuator():
    data = request.data
    dataDict = json.loads(data)
    app.logger.info(dataDict)

    aid = dataDict['id']
    atype = dataDict['type']
    aActive = dataDict['active']

    actuator = Actuator(actuatorId=aid, actuatorType=atype, actuatorActive=aActive)

    if session.query(Actuator).filter(
            Actuator.actuatorId==aid,
            Actuator.actuatorType==atype).count() == 0:
        session.add(actuator)
        session.commit()
        app.logger.info("New Actuator: " + actuator)

    return 'OK', 200

@app.route('/actuator/<atype>/<aid>', methods=['POST'])
def newSubscription(atype=None, aid=None):
    actuator = session.query(Actuator).filter(
            Actuator.actuatorId==aid,
            Actuator.actuatorType==atype)

    data = request.data
    dataDict = json.loads(data)
    app.logger.info("New subscription:" + dataDict)
    athres = dataDict['threshold']


    sub = Subscription(actuatorId=actuator.id, threshold=athres)
    session.add(sub)
    session.commit()

    return 'OK', 200
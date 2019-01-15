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

@app.route('/update', methods=['POST'])
def update():
    data = request.data
    js = json.loads(data)
    app.logger.info(type(js))
    actuator.setActive(js)

    app.logger.info(actuator)

    return 'OK', 200

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=8082, debug=True)

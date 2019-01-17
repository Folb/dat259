import requests
import json


def post_new_rule(rule: dict, atype, aid):
    requests.post('http://localhost:8081/actuator/' + atype + "/" + aid, data=rule)
    print("New rule added.")

def list_actuators():
    actuators = requests.get("http://localhost:8081/actuator")
    print(actuators.text)


def add_actuator(actuator: dict):
    js = json.dumps(actuator)
    requests.post('http://localhost:8081/actuator', data=js)
    print("New actuator added.")


def update_actuator(bool_val, atype, aid):
    requests.post('http://localhost:8081/actuator/' + atype + "/" + aid + "/status", data=bool_val)
    print("Actuator updated.")


def list_sensors():
    sensors = requests.get("http://localhost:8080/sensor")
    print(sensors.text)


def add_sensor(sensor: dict):
    requests.post('http://localhost:8080/sensor', data=sensor)
    print("New sensor added.")

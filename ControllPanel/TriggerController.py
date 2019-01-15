import requests


def post_new_rule(rule: dict, atype, aid):
    requests.post('localhost:8081/actuator/' + atype + "/" + aid, data=rule)

# list actuators

# add actuators

# update actuator

# list sensors

# add sensors





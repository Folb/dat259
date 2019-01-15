import os
from pubSubClient import Subscriber

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/simon/Downloads/dat259-rest-bd0aaa87ea8c.json"

Subscriber.create_subscription("dat259-rest", "actuatorUpdates", "actuator_update_listener")


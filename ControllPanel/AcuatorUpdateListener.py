import os
import json
import time

from google.cloud import pubsub_v1
from sqlalchemy import create_engine, Sequence, ForeignKey, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./dat259-rest-2c6ee667d075.json"

engine = create_engine('sqlite:///UpdateDB.db')
Base = declarative_base()


class Updates(Base):
    __tablename__ = 'actuator_updates'
    t_id = Column(Integer, Sequence('sIdSeqId'), primary_key=True)
    actuator_id = Column(Integer, nullable=False)
    actuator_type = Column(String(30), nullable=False)
    active = Column(Boolean, nullable=False)


DBSession = sessionmaker(bind=engine)
session = DBSession()


def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)
    return d


#subscriber = Subscriber.create_subscription("dat259-rest", "actuatorUpdates", "actuator_update_listener")
subscriber = pubsub_v1.SubscriberClient()
topic_path = subscriber.topic_path("dat259-rest", "actuatorUpdates")
subscription_path = subscriber.subscription_path("dat259-rest", "actuator_update_listener")
#subscriber.create_subscription(subscription_path, topic_path)
#print(f'Subscription created: {subscription_path}')


def callback(msg):
    msg.ack()

    message = binary_to_dict(msg.data.decode("utf-8"))
    print(message)
    a_type = message["type"]
    a_id = message["id"]
    active_status = message["active"]
    session.add(Updates(actuator_id=a_id, actuator_type=a_type, active=active_status))
    print(session.query(Updates).all())


    # returns a StreamingPullFuture that represents a process that asynchronously
    # performs streaming pull and schedules messages to be processed
    future = subscriber.subscribe(subscription_path, callback)

    try:
        # causes the calling thread to block indefinitely
        future.result()
    except KeyboardInterrupt:
        # stops the process of pulling messages, shuts down the background thread
        future.cancel()


Base.metadata.create_all(engine)


if __name__ == '__main__':
    subscriber.subscribe(subscription_path, callback=callback)
    while True:
        time.sleep(60)

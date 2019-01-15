import os
import json
from google.cloud import pubsub_v1
from sqlalchemy import create_engine, Sequence, ForeignKey, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite://UpdateDB')
Base = declarative_base()


class Updates(Base):
    __tablename__ = 'actuator_updates'
    t_id = Column(Integer, Sequence('sIdSeqId'), primary_key=True)
    a_id = Column(Integer, nullable=False)
    a_type = Column(String(30), nullable=False)
    active = Column(bool, nullable=False)


DBSession = sessionmaker(bind=engine)
session = DBSession()


def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)
    return d


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/simon/Downloads/dat259-rest-bd0aaa87ea8c.json"

#subscriber = Subscriber.create_subscription("dat259-rest", "actuatorUpdates", "actuator_update_listener")
subscriber = pubsub_v1.SubscriberClient()
topic_path = subscriber.topic_path("dat259-rest", "actuatorUpdates")
subscription_path = subscriber.subscription_path("dat259-rest", "actuator_update_listener")
subscriber.create_subscription(subscription_path, topic_path)
print('Subscription created: {subscription_path}')


def callback(msg):

    msg = binary_to_dict(msg.data.decode("utf-8"))
    a_type = msg("type")
    a_id = msg("id")
    active = msg("active")
    session.add(Updates(a_id=a_id, a_type=a_type, active=active))

    msg.ack()

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
    subscriber.subscribe(subscription_path, callback)

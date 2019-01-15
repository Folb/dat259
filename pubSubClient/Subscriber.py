import os
import json
from google.cloud import pubsub_v1


class Subscriber(object):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/simon/Downloads/dat259-rest-bd0aaa87ea8c.json"

    # topic_name = 'projects/{}/topics/{}'.format(
    #     'dat259-rest',
    #     'temperature_sensors',
    # )
    # subscription_name = 'projects/{}/subscriptions/{}'.format(
    #     'dat259-rest',
    #     'my-test-sub',
    # )
    def __init__(self):
        __subscriber = pubsub_v1.SubscriberClient()

    def create_subscription(self, subscriber, subscription_name, topic_name):
        subscriber.create_subscription(
            name=subscription_name, topic=topic_name)

    def callback(self, msg, subscriber, subscription_name):
        """
        Asynchronously processes messages received from a subscription.
        Sends an ack when a message is processed
        :param subscription_name:
        :param subscriber:
        :param msg: The Message instance
        """
        print(json.dumps(msg.data.decode('utf-8')))
        msg.ack()

        # returns a StreamingPullFuture that represents a process that asynchronously
        # performs streaming pull and schedules messages to be processed
        future = subscriber.subscribe(subscription_name, callback)

        try:
            # causes the calling thread to block indefinitely
            future.result()
        except KeyboardInterrupt:
            # stops the process of pulling messages, shuts down the background thread
            future.cancel()

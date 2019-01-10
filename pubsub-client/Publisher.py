import os
import time
from google.cloud import pubsub_v1

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/simon/Downloads/dat259-rest-bd0aaa87ea8c.json"

# can be configured to publish a batch when a specified threshold is met
# topic_name = 'projects/{}/topics/{}'.format(
#     'dat259-rest',
#     'temperature_sensors',
# )


def create_topic(topic_name):
    publisher = pubsub_v1.PublisherClient()

    publisher.create_topic(topic_name)


def callback(message_future, topic_name):
    if message_future.exception(timeout=50):
        print('Publishing message on {} threw an Exception {}.'.format(
            topic_name, message_future.exception()))
    else:
        print(message_future.result())


def publish(msg, publisher, topic_name):
    message_future = publisher.publish(topic_name, msg.encode(), spam='eggs')

    # Attaches the provided callable to the future.
    # The provided function is called, with this future as its only argument, when the future finishes running.
    message_future.add_done_callback(callback)

    # We must keep the main thread from exiting to allow it to process
    # messages in the background.
    while True:
        time.sleep(60)

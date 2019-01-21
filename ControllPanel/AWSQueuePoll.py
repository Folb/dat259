from json import JSONDecodeError

import boto3
import json


# Service resource
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='testQ')

while True:

    for message in queue.receive_messages():

        msg = ''.join(chr(int(x, 2)) for x in message.body.split())
        try:

            body = json.loads(msg)
            print(msg)
            message.delete()

            print()

        except JSONDecodeError:
            print('Decode error')

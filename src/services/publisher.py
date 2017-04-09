import pika
import os

class Publisher:
    class __Publisher:
        def __init__(self):
            print("born")
            print(os.environ['RABBIT_IP'])
            credentials = pika.PlainCredentials(os.environ['RABBIT_LOGIN'], os.environ['RABBIT_PASSWORD'])
            params = pika.ConnectionParameters(os.environ['RABBIT_IP'], 5672, '/', credentials)
            self.connection = pika.BlockingConnection(params)
            self.channel = self.connection.channel()

        def __del__(self):
            print("die")
            self.channel.close()
            self.connection.close()

        def publish(self, message, exchange, routing_key):
            self.channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)

    instance = None

    def __new__(self):
        if not Publisher.instance:
            Publisher.instance = Publisher.__Publisher()
        return Publisher.instance

    def __getattr__(self, attr):
        return getattr(self.instance, attr)

    def __setattr__(self, attr, val):
        return setattr(self.instance, attr, val)

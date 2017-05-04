import pika
from src.services.environements import Environements

class Publisher:
    class __Publisher:
        def __init__(self):
            print("born")
            print(Environements().get('RABBIT_IP'))
            credentials = pika.PlainCredentials(Environements().get('RABBIT_LOGIN'), Environements().get('RABBIT_PASSWORD'))
            params = pika.ConnectionParameters(Environements().get('RABBIT_IP'), 5672, '/', credentials)
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

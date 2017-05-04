from src.services.redis_connector import RedisConnector
from src.services.publisher import Publisher
from rq.decorators import job
import pika


EXCHANGE_NAME = 'chiepherd.main'


@job('low', connection=RedisConnector().connection)
def create():
    channel = Publisher().channel

    channel.exchange_declare(exchange=EXCHANGE_NAME, type='topic')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange=EXCHANGE_NAME, routing_key='chiepherd.projects.create', queue=queue_name)

    channel.basic_consume(create_callback, queue=queue_name, no_ack=True)
    channel.start_consuming()


def create_callback(channel, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

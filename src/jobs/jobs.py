import time
from rq import Queue
from src.jobs.hello_world import five_hello, five_hello2
from src.services.redis_connector import RedisConnector
from src.jobs.projects.create import create


def jobs():
    redis_conn = RedisConnector().connection
    q = Queue(connection=redis_conn)
    q.enqueue(create, timeout=-1)

import time
from rq import Queue
from redis import Redis
from src.jobs.hello_world import five_hello


def jobs():
    redis_conn = Redis()
    q = Queue(connection=redis_conn)
    job = q.enqueue(five_hello)

    time.sleep(2)

    print(job.result)
    return 221

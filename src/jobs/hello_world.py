import time
from rq.decorators import job
from src.services.redis_connector import RedisConnector


@job('low', connection=RedisConnector().connection, timeout=0)
def five_hello2():
    print("Two")
    for i in range(0, 5):
        print("Hello")
    file = open("testfile_date.txt", "w")

    file.write("Hello World\n")
    file.write("This is our new text file")
    file.write(" and this is anotherline.\n")
    file.write("Why? Because we can.")

    file.close()

    return 221



def five_hello():
    print("One")
    for i in range(0, 5):
        print("Hello")
    file = open("testfile.txt", "w")

    file.write("Hello World\n")
    file.write("This is our new text file")
    file.write(" and this is anotherline.\n")
    file.write("Why? Because we can.")

    file.close()

    return 221

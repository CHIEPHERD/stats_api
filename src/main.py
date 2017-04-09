from src.services.publisher import Publisher
from time import time, sleep


def main():
    fps = 5
    frameperiod = 1.0 / fps
    now = time()
    try:
        while True:
            print("Publish `hello world 2 truc :p`")
            Publisher().publish("hello world 2 truc :p ", "chiepherd.app", "chiepherd.foo")
            nextframe = now + frameperiod
            while now < nextframe:
                sleep(nextframe - now)
                now = time()
            nextframe += frameperiod

    except KeyboardInterrupt:
        pass

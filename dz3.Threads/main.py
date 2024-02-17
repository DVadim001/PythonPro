# trafficlight in thereads

from threading import Thread
import time


def green() -> None:
    color: str = 'GREEN'
    print(color)
    sleep


t1: Thread = Thread(target=green)
t1.start()


def yellow() -> None:
    color: str = 'YELLOW'
    print(color)


t2: Thread = Thread(target=yellow)
t2.start()


def red() -> None:
    color: str = 'RED'
    print(color)


t3: Thread = Thread(target=red)
t3.start()


print(' пешеход побежал')

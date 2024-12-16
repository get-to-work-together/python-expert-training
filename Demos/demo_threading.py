import random
import time
from threading import Thread


def myfunc(i):
    t = random.randint(1, 5)
    print(f'thread {i} sleeping for {t} secconds')
    time.sleep(t)
    print(f'thread {i} finished sleeping')

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()

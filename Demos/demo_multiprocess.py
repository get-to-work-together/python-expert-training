import random
import time
from multiprocessing import Process


def f(i):
    t = random.randint(1, 5)
    print(f'process {i} sleeping for {t} secconds')
    time.sleep(t)
    print(f'process {i} finished sleeping')


if __name__ == '__main__':
    for i in range(5):
        p = Process(target=f, args=(i,))
        p.start()

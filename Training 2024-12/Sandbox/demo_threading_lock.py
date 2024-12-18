import time
from threading import Thread, Lock

class Counter:
    def __init__(self):
        self.total = 0
    def add(self, n):
        with Lock():
            self.total += n

counter = Counter()

# calculate the sum of all the numbers between lowest_number and highest number
lowest_number = 1
highest_number = int(10000)
number_of_numbers = highest_number - lowest_number + 1

expected_result = int((lowest_number + highest_number) * (number_of_numbers / 2))

print(f'Sum of all numbers between {lowest_number} and {highest_number}. Expected result: {expected_result}')

number_of_threads = 100
number_of_numbers_per_thread = number_of_numbers // number_of_threads + 1

def myfunc(i, lowest, highest, counter):
    print(f'thread {i} started working on range from {lowest} to {highest}')
    for number in range(lowest, highest + 1):
        counter.add(number)
        time.sleep(0.000000001)
    print(f'thread {i} done.')

t0 = time.perf_counter_ns()

threads = []
lowest = lowest_number
for i in range(number_of_threads):
    highest = min(lowest + number_of_numbers_per_thread - 1, highest_number)
    thread = Thread(target=myfunc, args=(i, lowest, highest, counter))
    threads.append(thread)
    thread.start()
    lowest = highest + 1

for thread in threads:
    thread.join()

t1 = time.perf_counter_ns()

print(f'Duration: {t1 - t0}ns')
print(f'Result: {counter.total}')
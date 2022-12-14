import queue
import sys
import threading
import time
from functools import lru_cache

global resultsQueue
COSNT_MAX_N = 100000

resultsQueue = queue.Queue()

class Worker(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.result = 0
    def run(self):
        self.result = process_queue(self.name)

def process_queue(name):
        result = 0
        while True:
            try:
                value = resultsQueue.get(block=False)
                if (result==0):
                    result = value
                else:
                    result = result * value
                    
            except queue.Empty:
                return result

def fillQueue(n):
    for item in range(1,n+1):
        resultsQueue.put(item)

def get_ttl_hash(seconds=3600):
    return round(time.time() / seconds)

@lru_cache(maxsize = 128)
def factorial(n, numberOfworkers, ttl_hash=None):
    del ttl_hash

    if n < 0 or n > COSNT_MAX_N:
        raise Exception("Number of N is incorrenct.")
    if n < 1:
        return 1
    else:
        finalresult = 0
        workers = []

        fillQueue(n)
        for item in range(1,numberOfworkers+1):
            worker = Worker(item)
            workers.append(worker)
            worker.start()

        for worker in workers:
            worker.join()

        for worker in workers:
            if worker.result != 0:
                if finalresult == 0:
                    finalresult = worker.result
                else:
                    finalresult = finalresult * worker.result

        return finalresult

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__== "__main__":
    if (isint(sys.argv[1]) == False or isint(sys.argv[2]) == False):
         raise Exception("Argeuments are incorrect.")

    number = int(sys.argv[1])
    workers = int(sys.argv[2])

    factorial(number, workers, get_ttl_hash())
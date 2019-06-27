import logging
import threading
import time

import concurrent.futures


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)


# Lock use
"""
The basic functions to do this are .acquire() and .release(). A thread will call my_lock.acquire() to get the lock. 
If the lock is already held, the calling thread will wait until it is released. There’s an important point here. 
If one thread gets the lock but never gives it back, your program will be stuck. You’ll read more about this later.

Fortunately, Python’s Lock will also operate as a context manager, so you can use it in a with statement, and it 
gets released automatically when the with block exits for any reason.
"""


class FakeDatabase2:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("START 1")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    # .submit() has a signature that allows both positional and named arguments to be passed
    # to the function running in the thread
    logging.info("Testing update. Ending value is %d.", database.value)

    logging.info("START 2")

    logging.getLogger().setLevel(logging.DEBUG)

    database2 = FakeDatabase2()
    logging.info("Testing update. Starting value is %d.", database2.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database2.locked_update, index)
    logging.info("Testing update. Ending value is %d.", database2.value)


    # Deadlock
    # logging.info("START 3")
    # l = threading.Lock()
    # print("before first acquire")
    # l.acquire()
    # print("before second acquire")
    # l.acquire()
    # print("acquired lock twice")

    # An RLock on the other hand, can be acquired multiple times, by the same thread.
    # Another difference is that an acquired Lock can be released by any thread, while an acquired RLock can only be
    # released by the thread which acquired it.
    logging.info("START 4")
    r = threading.RLock()
    print("before first acquire")
    r.acquire()
    print("before second acquire")
    r.acquire()
    print("acquired lock twice")
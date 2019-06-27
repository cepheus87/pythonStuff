import logging
import threading
import time

import concurrent.futures


def thread_function(name):
    logging.info("Thread %s: starting", name)
    if name == 1:
        raise RuntimeError()
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO,
                        datefmt="%H:%M:%S")

    max_no = 3

    # executor do .join() on each of the threads in the pool
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_no) as executor:
        executor.map(thread_function, range(max_no))

    # ThreadPoolExecutor hides all exception thrown in the thread

    logging.info("Main    : all done")

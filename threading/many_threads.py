import logging

import threading

import time


def thread_function(name):

    logging.info("Thread %s: starting", name)

    time.sleep(5)

    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO,

                        datefmt="%H:%M:%S")




    threads = list()
    for i in range(3):
        logging.info("Main    : before creating thread")
    
        x = threading.Thread(target=thread_function, args=(i,))
        threads.append(x)
        x.start()

    for i, thr in enumerate(threads):
        logging.info("Main    : before joining thread %d", i)
#        x.join()        
        logging.info("Main    : thread %d done", i)



    # tell thread to wait for another thread
    
    logging.info("Main    : all done")

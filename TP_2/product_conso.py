from threading import Thread,Lock
import random
import time

verrou = Lock()

class PopulateList(Thread):
    my_list = []
    ended = False
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(10):
            time.sleep(random.randrange(1,3,1))
            with verrou:
                PopulateList.my_list.append(i)
                print("Added in pending list : {}".format(i))
        PopulateList.ended = True

class ComsumeList(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while not(PopulateList.ended) or len(PopulateList.my_list):
            if len(PopulateList.my_list):
                with verrou:
                    consumed = PopulateList.my_list.pop(0)
                time.sleep(random.randrange(1,3,1))
                print("Consumed from pending list : {}".format(consumed))
            else:
                time.sleep(0.1)

threads = [PopulateList(),ComsumeList()] 

for thread in threads:
    thread.start()

# if we do not join, we do not wait the end of the threads

for thread in threads:
    thread.join()
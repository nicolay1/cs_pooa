from threading import Thread,Lock,Semaphore
import random
import time

# this lock create a "poooooool" of threads
verrou = Semaphore(2)

# this Lock only allow one printing a time
# verrou = Lock()
nb_doc = 5

class DocumentsPrint(Thread):
    """Thread chargé simplement d'afficher un mot dans la console."""
    id_singleton = 0
    def __init__(self):
        Thread.__init__(self)
        DocumentsPrint.id_singleton += 1
        self.id = DocumentsPrint.id_singleton
        self.nb_page = random.randint(1,10)

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        with verrou:
            for i in range(self.nb_page):
                time.sleep(0.5)
                print("Thread {} : page {}".format(self.id,i+1))

threads = [DocumentsPrint() for i in range(nb_doc)]

for thread in threads:
    thread.start()

# if we do not join, we do not wait the end of the threads

for thread in threads:
    thread.join()
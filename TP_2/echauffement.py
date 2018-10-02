from threading import Thread,Lock

verrou = Lock()

class IncDec(Thread):
    """Thread chargé simplement d'afficher un mot dans la console."""
    compteur = 0
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        for i in range(10000):
            with verrou:
                IncDec.compteur += 1
        for i in range(10000):
            with verrou:
                IncDec.compteur -= 1
        with verrou:
            IncDec.compteur += 1

threads = [IncDec() for i in range(1000)]

for thread in threads:
    thread.start()

# if we do not join, we do not wait the end of the threads

for thread in threads:
    thread.join()

print(IncDec.compteur)
# 31/05/22
# Gorvien - Perrichet

import multiprocessing as mp
import time
import sys

def travailleur(k_bills):
    for i in range(m):
        demander(k_bills)
        time.sleep(2)
        rendre(k_bills)
    
if __name__ == "__main__" :

    #init variables
    Nb_process = 4
    k_bills = 9
    max_billes= k_bills
    m = 4
    listeProcess = []

    #Création processus travailleurs
    P1=mp.Process(target=travailleur, args=(k_bills))
    P2=mp.Process(target=travailleur, args=(k_bills))
    P3=mp.Process(target=travailleur, args=(k_bills))
    P4=mp.Process(target=travailleur, args=(k_bills))

    #Lancement des processus travalleurs
    P1.start()
    P2.start()
    P3.start()
    P4.start()

    #Création processus controleur
    Pcontrole=mp.Process(target=controleur, args=(max_billes))

    #Lancement du processus controleur
    Pcontrole.start()

    #Attente de la fin des processus
    P1.join()
    P2.join()
    P3.join()
    P4.join()

    Pcontrole.join()

    sys.exit(0)
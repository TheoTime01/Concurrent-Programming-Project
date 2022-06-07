"""
Created on Tue May 30 10:00:00 2022
@author: Mathis Gorvien & Theotime Perrichet
github : https://github.com/TheoTime01/Projet_CS_PC
To do : évolution du nb de billes doit évoluer
"""

import multiprocessing as mp
import time
import sys

nb_dispo_billes=9

#Sémaphore d'attente pour la disponibilité des billes
bills_token = mp.Semaphore(9)
wait_token=mp.Semaphore(1)

def travailleur(k_bills):
    m=4
    for i in range(m):
        print("process", mp.current_process().pid, "commence sa tache: n°", i+1)
        demander(k_bills)
        time.sleep(2)
        rendre(k_bills)
        print("process", mp.current_process().pid, "a terminé  sa tache: n°", i+1)

def controleur(max_bills):
    global nb_dispo_billes
    while 1>0:
        if 0 <= nb_dispo_billes <= max_bills:
            None
        else:
            print("Erreur : nb_dispo_billes =", nb_dispo_billes)
            sys.exit(0)

def demander(k_bills):
    global nb_dispo_billes
    while nb_dispo_billes < k_bills:
        wait_token.acquire()
        print("process", mp.current_process().pid, "est en attente")
    nb_dispo_billes-=k_bills
    for i in range(k_bills):
            bills_token.acquire()

def rendre(k_bills):
    global nb_dispo_billes
    nb_dispo_billes+=k_bills
    for i in range(k_bills):
            bills_token.release()
    
if __name__ == "__main__" :

    #init variables
    Nb_process = 4
    max_billes = nb_dispo_billes
    k1,k2,k3,k4=4,3,5,2

    #Création process travailleurs
    P1=mp.Process(target=travailleur, args=(k1,))
    P2=mp.Process(target=travailleur, args=(k2,))
    P3=mp.Process(target=travailleur, args=(k3,))
    P4=mp.Process(target=travailleur, args=(k4,))

    #Lancement des process travalleurs
    P1.start()
    P2.start()
    P3.start()
    P4.start()

    #Création process controleur
    # Pcontrole=mp.Process(target=controleur, args=(max_billes,))

    #Lancement du process controleur
    # Pcontrole.start()

    #Attente de la fin des process
    P1.join()
    P2.join()
    P3.join()
    P4.join()
    # Pcontrole.join()

    sys.exit(0)
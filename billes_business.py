"""
Created on Tue May 30 10:00:00 2022
@author: Mathis Gorvien & Theotime Perrichet
github : https://github.com/TheoTime01/Projet_CS_PC
"""

import multiprocessing as mp
import time
import sys

from numpy import disp

#Sémaphore d'attente pour la disponibilité des billes
bills_token = mp.Semaphore(9)
wait_token = mp.Semaphore(1)

def travailleur(k_bills, billes_dispo):
    m=4
    for i in range(m):
        wait_token.acquire()
        demander(k_bills,billes_dispo)
        wait_token.release()
        time.sleep(3)
        wait_token.acquire()
        rendre(k_bills,billes_dispo)
        wait_token.release()
        print("Le", mp.current_process().name, "a rendu", k_bills, "billes lors de sa tache n°", i+1,"Billes dispos :", billes_dispo.value)

def controleur(max_bills,billes_dispo):
    dispo = int(billes_dispo.value)
    max= max_bills
    while 1>0:
        if 0 > dispo or dispo > max:
            print("Erreur : nb_dispo_billes =", billes_dispo.value)
            sys.exit(0)
        time.sleep(1)

def demander(k_bills, billes_dispo):
    n=0
    while billes_dispo.value < k_bills:
        n+=1
    print("Le", mp.current_process().name, "demande", k_bills, "billes et le nombre de billes dispos :", billes_dispo.value)
    for i in range(k_bills):
        bills_token.acquire()
        print("Le", mp.current_process().name, "a pris une billes")
        billes_dispo.value -= 1


def rendre(k_bills, billes_dispo):
    for i in range(k_bills):
        bills_token.release()
        billes_dispo.value += 1
    
    
if __name__ == "__main__" :

    #init variables
    nb_dispo_billes = mp.Value('i', 9)
    Nb_process = 4
    max_billes = 9
    k1,k2,k3,k4=4,3,5,2

    #Création processus travailleurs
    P1=mp.Process(target=travailleur, args=(k1, nb_dispo_billes,))
    P2=mp.Process(target=travailleur, args=(k2, nb_dispo_billes,))
    P3=mp.Process(target=travailleur, args=(k3, nb_dispo_billes,))
    P4=mp.Process(target=travailleur, args=(k4, nb_dispo_billes,))

    #Lancement des process travalleurs
    P1.start()
    P2.start()
    P3.start()
    P4.start()

    #Création processus controleur
    Pcontrole=mp.Process(target=controleur, args=(max_billes, nb_dispo_billes))

    #Lancement du process controleur
    Pcontrole.start()

    #Attente de la fin des process
    P1.join()
    P2.join()
    P3.join()
    P4.join()
    Pcontrole.join()

    sys.exit(0)
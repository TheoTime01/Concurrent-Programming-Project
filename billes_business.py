"""
Created on Tue May 30 10:00:00 2022
@author: Mathis Gorvien & Theotime Perrichet
github : https://github.com/TheoTime01/Projet_CS_PC
"""

import multiprocessing as mp
from os import kill
import time
import sys

from numpy import disp

#Sémaphore d'attente pour la disponibilité des billes
wait_token = mp.Semaphore(1)

def travailleur(k_bills, billes_dispo,Tours,A):
    m=4
    
    for i in range(m):
        if A.value:
            wait_token.acquire()
            demander(k_bills,billes_dispo)
            wait_token.release()
            time.sleep(3)
            wait_token.acquire()
            rendre(k_bills,billes_dispo)
            print("Le", mp.current_process().name, "a rendu", k_bills, "billes lors de sa tache n°", i+1,"Billes dispos :", billes_dispo.value)
            wait_token.release()
    Tours.value += 1
    print('Tourns', Tours.value, "finito")
    if Tours.value == 4:
            A.value=False

def controleur(max_bills,billes_dispo,A):
    while A.value:
        wait_token.acquire()
        dispo = int(billes_dispo.value)
        print("dispo", dispo)
        max= max_bills
        if 0 > dispo or dispo > max:
            print(" ")
            print("           Erreur : nb_dispo_billes =", billes_dispo.value)
            print(" ")
            A.value=False
            sys.exit()
        wait_token.release()
        time.sleep(1)
    sys.exit()

def demander(k_bills, billes_dispo):
    n=0
    while billes_dispo.value < k_bills:
        n+=1
    print("Le", mp.current_process().name, "demande", k_bills, "billes et le nombre de billes dispos :", billes_dispo.value)
    for i in range(k_bills):
        print("Le", mp.current_process().name, "a pris une billes")
        billes_dispo.value -= 1


def rendre(k_bills, billes_dispo):
    for i in range(k_bills):
        billes_dispo.value += 1
        print("Le", mp.current_process().name, "a rendu une billes")
    
    
if __name__ == "__main__" :

    #init variables
    nb_dispo_billes = mp.Value('i', 9)
    Tours=mp.Value('i', 0)
    A=mp.Value('b', True)
    Nb_process = 4
    max_billes = 9
    k1,k2,k3,k4=4,3,5,2

    #Création processus travailleurs
    P1=mp.Process(target=travailleur, args=(k1, nb_dispo_billes,Tours,A,))
    P2=mp.Process(target=travailleur, args=(k2, nb_dispo_billes,Tours,A,))
    P3=mp.Process(target=travailleur, args=(k3, nb_dispo_billes,Tours,A,))
    P4=mp.Process(target=travailleur, args=(k4, nb_dispo_billes,Tours,A,))

    #Lancement des process travalleurs
    P1.start()
    P2.start()
    P3.start()
    P4.start()

    #Création processus controleur
    Pcontrole=mp.Process(target=controleur, args=(max_billes, nb_dispo_billes,A,))

    #Lancement du process controleur
    Pcontrole.start()

    #Attente de la fin des process
    P1.join()
    P2.join()
    P3.join()
    P4.join()
    Pcontrole.join()

    sys.exit(0)
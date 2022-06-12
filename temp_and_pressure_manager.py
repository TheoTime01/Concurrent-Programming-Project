"""
Created on Tue May 30 10:00:00 2022
@author: Mathis Gorvien & Theotime Perrichet
github : https://github.com/TheoTime01/Projet_CS_PC
"""

import multiprocessing as mp
import time
import sys

# Init & declare var

ver=mp.Semaphore(1)
seuil_T,seuil_P = 20,10
go_pompe = False
go_chauffage = True
mem_T = mp.Value('i', 0)
mem_P = mp.Value('i', 0)

def control_task(X,mem_T,mem_P):
    "X : période"
    Z=1
    while True:
        ver.acquire()
        T = mem_T.value
        P = mem_P.value
        ver.release()
        if T > seuil_T :
            go_chauffage = False
            if P > seuil_P :
                go_pompe = True
            else :
                go_pompe = False
        elif T < seuil_T :
            go_pompe = True
            go_chauffage = True
        else :
            go_chauffage = False
            if P > seuil_P :
                go_pompe = True
            else :
                go_pompe = False
        heat_task(go_chauffage)
        pump_task(go_pompe)
        time.sleep(X)

###############################################################################
def heat_task(go_chauffage):
    if go_chauffage :
        print("Mise en marche du chauffage...")
    else:
        print("Arret du chauffage...")


def pump_task(go_pompe):
    if go_pompe :
        print("Mise en marche de la pompe...")
    else:
        print("Arret de la pompe...")

###############################################################################
def temp_task(S,mem_T):
    "S : période"
    V=20
    while True:
        print("Lecture de V capteur de température et conversion...")
        ver.acquire()
        mem_T.value = V
        ver.release()
        time.sleep(S)

def press_task(U,mem_P):
    "U : période"
    V=40
    while True:
        print("Lecture de V capteur de pression et conversion...")
        ver.acquire()
        mem_P.value = V
        ver.release()
        time.sleep(U)

def screen_task(mem_T,mem_P):
    while True:
        ver.acquire()
        T = mem_T.value
        P = mem_P.value
        ver.release()
        print("Température :", T, "°C")
        print("Pression :", P, "bar")
        time.sleep(1)

if __name__ == "__main__":
    
    # Création des process
    T=mp.Process(target=temp_task, args=(1,mem_T))
    P=mp.Process(target=press_task, args=(1,mem_P))
    S=mp.Process(target=screen_task, args=(mem_T,mem_P))

    Controler=mp.Process(target=control_task, args=(1,mem_T,mem_P))

    T.start()
    P.start()
    S.start()

    T.join()
    P.join()
    S.join()
    
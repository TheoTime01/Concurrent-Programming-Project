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
seuil_T,seuil_P = 0,0
go_pompe = False
go_chauffage = True
mem_T = mp.Value('i', 0)
mem_P = mp.Value('i', 0)

def control_task(X,mem_T,mem_P):
    "X : période"
    while 1>0:
        ver.acquire()
        T = mem_T.value
        P = mem_P.value
        if T > seuil_T :
            go_chauffage = False
            if P > seuil_P :
                go_pompe = True
            else :
                go_pompe = False
        elif :
            go_pompe = True
            go_chauffage = True
        else :
            go_chauffage = False
            if P > seuil_P :
                go_pompe = True
            else :
                go_pompe = False
        time.sleep(X)

def heat_task():
    pass

def temp_task(S):
    "S : période"
    while 1>0:
        time.sleep(S)
        print("Température : ", S)
    pass

def press_task():
    "U : période"
    pass

def pump_task():
    "Z : période"
    pass

def screen_task():
    pass

if __name__ == "__main__":
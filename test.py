"""
Created on Wed Jun 1 19:30:34 2022
@author: Gorvien Mathis / Perrichet Théotime

"""

import random
import multiprocessing as mp
import numpy as np



def draw(tab):
    for raw in tab:
        print(raw, end="\n")
    print(end="\n")

def cellule(tab,largeur,hauteur,taille):
    sum = 0
    for l,c in ((largeur-1,hauteur),(largeur,hauteur-1),(largeur,hauteur+1),(largeur+1,hauteur)):
        if l>=0 and c>=0 and l<=taille-1 and c<=taille-1:
            sum += tab[l][c]
    return sum
    
def calcul(sum,tab,largeur,hauteur):
    if tab[largeur][hauteur]==1:
        if sum < 2:
            Val = 0
        elif sum == 2 or sum == 3:
            Val = 1
        elif sum > 3:
            Val = 0
    else:
        if sum == 3:
            Val = 1
        else:
            Val = tab[largeur][hauteur]
    return Val

def update(tab,largeur,hauteur,taille):
    sum = cellule(tab,largeur,hauteur,taille)
    val = calcul(sum,tab,largeur,hauteur)

    lock.acquire()
    new_tab[largeur][hauteur] = val
    lock.release()







taille = 15
lock=mp.Lock()
process = [[None for _ in range(taille)]for _ in range(taille)]

tab = [[random.randint(0,1) for k in range(taille)] for i in range(taille)]
new_tab_v = [[0 for k in range(taille)] for i in range(taille)]

while not np.array_equal(new_tab_v, tab):
    draw(tab)

    new_tab_mp = mp.RawArray('d', taille*taille)
    new_tab = np.frombuffer(new_tab_mp, dtype=np.float64).reshape((taille,taille))

    for i in range(taille):
        for k in range(taille):
            process[i][k]= mp.Process(target=update, args=(tab,i,k,taille))
            process[i][k].start()
            process[i][k].join()

    new_tab_v = tab[:]
    tab = new_tab[:]

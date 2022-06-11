"""
Created on Tue Jun 7 10:40:12 2022
@author: Gorvien Mathis / Perrichet Théotime

"""

import multiprocessing as mp
from queue import Empty
from random import randint


def Q_sort(Q,tab,lock,keep_running):
    while keep_running.value:
        
        # verification si la liste 'tab' est bien triée
        verif = True
        for i in range(len(tab)-1):
            if tab[i] > tab[i+1]:
                verif = False
        keep_running.value = not verif

        # vérification que la queue est non vide
        try:
            list_args = Q.get(timeout=1)
        except (Empty): 
            pass

        
        liste = list_args[0]
        position = list_args[1]

        # ne met rien dans la pile si la liste fournie est vide
        if liste == []:
            pass

        else:
            pivot = liste[0] # le pivot est le premier élément de la liste
            
            # initialisation des listes T1 et T2
            T1 = []
            T2 = []

            # tri dans les deux listes les valeurs inférieurs et supérieures au le pivot
            for c in liste[1:]:
                if c <= pivot:
                    T1.append(c)
                else:
                    T2.append(c)

            # Utilisation d'un Lock pour le tableau partagé par les Process 
            lock.acquire()
            tab[position+len(T1)] = pivot
            lock.release()

            # mise dans la Queue les nouvelles listes à trier avec le bon indice de référence
            Q.put((T1,position))
            Q.put((T2,len(T1)+position+1))


if __name__ == '__main__':

    # création du tableau 
    taille_tab = 100
    tab = mp.Array('i', [randint(1,99) for i in range(taille_tab)])
    print("tableau de base",tab[:])

    # Variables partagées
    keep_running = mp.Value('b',True)
    q = mp.Queue()
    lock = mp.Lock()

    # Mise en queue du tab de départ
    q.put((tab[:],0))



    process = [mp.Process(target=Q_sort, args=(q,tab,lock,keep_running)) for i in range(8)]
    for p in process:
        p.start()
    for p in process:
        p.join()

    print("tableau trié croissant : ",tab[:])

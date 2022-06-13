"""
Created on Tue May 31 8:10:28 2022
@author: Gorvien Mathis / Perrichet Théotime

"""

import multiprocessing as mp
import time
from matplotlib import pyplot as plt
import math

def arc_tan(N,n,pi,I):
    """ Chaque process va calculer une somme de même taille et ajouter celle-ci dans la variable partagée pi
Arguments:
    n : nombre d'itération du process
"""
    somme_Part = 0
    for i in range(n*(I-1),n*I ):
        somme_Part += 4/(1+ ((i+0.5)/N)**2)
    pi.value += (1/N)*somme_Part

if __name__ == "__main__" :

    # On effectue plusieurs tests pour voir l'influence du nombre de processus
    N = 10**6
    Nb_process_max = 10
    Nb_process_min = 2

    Nb_process_List = [i for i in range(Nb_process_min,Nb_process_max+1)]
    time_list = []

    for Nb_process in Nb_process_List:
        start_time = time.time()
        nb_iteration_par_process = N/Nb_process
        i=0
        listeProcess = []
        pi = mp.Value('f',0)
        
        for _ in range(Nb_process) :
            i+=1
            process = mp.Process(target = arc_tan, args = (N,int(nb_iteration_par_process),pi,i,))
            listeProcess.append(process)
            process.start()
        
        for p in listeProcess :
            p.join()
        time_list.append(math.floor(10000*(time.time()-start_time))/10000)

        print(f"estimation de pi en {Nb_process} process : PI = {pi.value}")
        print(f"Durée du calcul multi Process : {time_list[-1]} s")
        print("\n")
    
    plt.figure(1)
    plt.plot(Nb_process_List,time_list)
    plt.xlabel("nbr de process en parallèle")
    plt.ylabel("temps de calcul")
    plt.title(f"Temps de calcul d'une approximation de PI")
    plt.show()
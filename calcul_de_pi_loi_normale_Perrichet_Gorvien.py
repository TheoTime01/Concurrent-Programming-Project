# -*- coding: utf-8 -*-
"""
Created on Tue May 31 8:10:28 2022
@author: Gorvien Mathis / Perrichet Théotime

"""

import time
import random
import multiprocessing as mp
import numpy as np

def calcul_Monoprocess(f ,a ,b,n): 
    somme=0
    for i in range(0,n): 
        xi = a+ (b-a) * i / float(n)
        xj= a+ (b-a)*(i+1)/float(n)
        somme+= (f(xi)+f(xj))/2.0*(xj-xi)
    somme = (2*somme**2)    
    return somme  
   
def fn(x): 
    return np.exp((-x**2)/2)
    

def calcul_Multiprocess(inf,sup,k,f):
    sum_local=0
    
    for i in range(inf,sup):
        xi = inf+ (sup-inf) * i / float(sup)
        xj= inf+ (sup-inf)*(i+1)/float(sup)
        sum_local+= (f(xi)+f(xj))/2.0*(xj-xi)
    sum_local = (2*sum_local**2)   
    

    mutex.acquire()
    tableau[k]+=sum_local
    mutex.release()

nb_process = 30
tableau = mp.Array('f', nb_process) 
tableau[:]= [0 for _ in range(nb_process)]

x1=0                          #Borne de debut 
x2=random.randint(1, 10**5)   # Borne de fin 
x3= random.randint(1, 10**5)  # le Pas des trapèzes 

mutex = mp.Lock()

#mono-process
debut = time.time()
sum = calcul_Monoprocess(fn, x1 , x2, x3)
fin= time.time()
print("Valeur estimée Pi par la méthode Mono−process : ", sum)
print("Temps ", (fin-debut))


tableau_pid= [None for _ in range(nb_process)]

debut2 = time.time()
for k in range (nb_process) :
    tableau_pid[k]=mp.Process(target=calcul_Multiprocess, args=(k*x2//nb_process,(k+1)*x3//nb_process,k,fn))
    tableau_pid[k].start()
	
for k in range (nb_process) :
	tableau_pid[k].join()
fin2 = time.time()

som_tab = sum(tableau)

print("Valeur estimée Pi par la méthode Multi−process : ", som_tab)
print("Multi_proc: Temps = ", (fin2-debut2))
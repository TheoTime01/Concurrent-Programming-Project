"""
Created on Tue May 31 8:10:28 2022
@author: Gorvien Mathis / Perrichet Théotime

"""

import  time


def arc_tan(nb_total_iteration):

	sum = 0 
	for i in range(0, int(nb_total_iteration)-1):
		sum = sum +(( 4/(1+((i-0.5)/nb_total_iteration)*((i-0.5)/nb_total_iteration))))
	return sum
 
	

nb_total_iteration = 10**6

debut=time.time()
somme_process=arc_tan(nb_total_iteration)
fin=time.time()

print("Valeur estimée de Pi par la méthode Mono−Processus : ", somme_process/ nb_total_iteration)
print("Temps=",(fin-debut))
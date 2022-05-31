# 31/05/22
# Gorvien - Perrichet

import multiprocessing as mp
import time

if __name__ == "__main__" :

    #init variables
    Nb_process = 4
    Nb_billes = 9
    m = 4
    listeProcess = []

    #Création processus travailleurs

    #Création processus controleur


    def travailleur(k_bills):
        global Nb_billes
        demander(k_bills)
        time.sleep(2)
        rendre(k_bills)

    
    
    
    def demander(k_bills):
        global Nb_billes


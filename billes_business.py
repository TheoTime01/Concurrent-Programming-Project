# 31/05/22
# Gorvien - Perrichet

import multiprocessing as mp
import time

if __name__ == "__main__" :

    #init variables
    Nb_process = 4
    Nb_billes = 5
    m = 4
    listeProcess = []

    def travailleur(k_bills):
        for i in range(m):
            process = mp.Process(target = demander, args = (int(k_bills),))
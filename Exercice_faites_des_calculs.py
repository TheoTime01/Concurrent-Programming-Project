"""
Created on Tue Jun 7 12:04:26 2022
@author: Gorvien Mathis / Perrichet Théotime

"""

import time,os,sys,random
import multiprocessing as mp


def calcul_fils(commande, stockage):
    print("Bonjour du Fils calculateurs", os.getpid())
    while True:
        calcul = commande.get()
        id = calcul[0]
        cmd = calcul[1]
        res = eval(cmd)
        stockage.put([id, res])
        time.sleep(1)
    sys.exit(0)


def fils_demand(commands, stockage, lock):
    id = os.getpid()
    print('bonjour du fils demandeur', id)

    while True:
        # Le pere envoie au fils un calcul aléatoire à faire et récupère le résultat
        opd1 = random.randint(1, 100)
        opd2 = random.randint(1, 100)
        operateur = random.choice(['+', '-', '*', '/', '**'])
        str_commande = f"{opd1} {operateur} {opd2}"
        commands.put([id, str_commande])
        print(f"Le père {id} demande à faire : ", str_commande)
        lock.acquire()
        bool_getcalcul = True
        while bool_getcalcul:
            calcul = stockage.get()
            if calcul[0] == id:
                res = calcul[1]
                bool_getcalcul = False
            else:
                stockage.put(calcul)
        lock.release()
        print(f"Le Pere {id} a recu ", res)
        print('-' * 60)
        time.sleep(1)
    sys.exit(0)


if __name__ == "__main__":
    stockage = mp.Queue()
    commands = mp.Queue()
    nbr_demandeurs = 4
    lst_demandeurs = [0 for i in range(nbr_demandeurs)]
    nbr_calculateurs = 4
    lst_calculateurs = [0 for i in range(nbr_demandeurs)]

    lock = mp.Semaphore()
    for i in range(nbr_calculateurs):
        lst_calculateurs[i] = mp.Process(
            target=calcul_fils, args=(commands, stockage))
        lst_calculateurs[i].start()

    for i in range(nbr_demandeurs):
        lst_demandeurs[i] = mp.Process(
            target=fils_demand, args=(commands, stockage, lock))
        lst_demandeurs[i].start()

    for i in range(nbr_calculateurs):
        lst_calculateurs[i].join()
    for i in range(nbr_demandeurs):
        lst_demandeurs[i].join()
"""
Created on Tue Jun 7 12:04:26 2022
@author: Gorvien Mathis / Perrichet Théotime

"""

import multiprocessing as mp
import time,os,sys,random


def calcul_fils(commande, lst_att): #fonction qui fait le calcul et met le reseultat dans la liste lst_att
    while True:
        calcul = commande.get()
        id = calcul[0]
        m = calcul[1]
        r = eval(m)
        lst_att.put([id, r])
        time.sleep(1)
    sys.exit(0)


def demande(commands, lst_att, lock): #fonction qui demande un calcul aleatoire a un fils et le revoie au pere
    id = os.getpid()

    while True:
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        opt = random.choice(['+', '-', '*', '/', '**'])
        str_commande = f"{x} {opt} {y}"
        commands.put([id, str_commande])
        print(f"Le père {id} demande : ", str_commande)
        lock.acquire()
        calcul_get = True
        while calcul_get:
            calcul = lst_att.get()
            if calcul[0] == id:
                respond = calcul[1]
                calcul_get = False
            else:
                lst_att.put(calcul)
        lock.release()
        print(f"Le Pere {id} reçoit ", respond)
        print('#' * 50)
        time.sleep(2)
    sys.exit(0)


if __name__ == "__main__":
    lst_att = mp.Queue()
    commands = mp.Queue()
    nbs_demandeur = 4
    demandeurs = [0 for i in range(nbs_demandeur)]
    nbs_calculateurs = 4
    calculateurs = [0 for i in range(nbs_demandeur)]

    lock = mp.Semaphore()
    for i in range(nbs_calculateurs):
        calculateurs[i] = mp.Process(
            target=calcul_fils, args=(commands, lst_att))
        calculateurs[i].start()

    for i in range(nbs_demandeur):
        demandeurs[i] = mp.Process(
            target=demande, args=(commands, lst_att, lock))
        demandeurs[i].start()

    for i in range(nbs_calculateurs):
        calculateurs[i].join()
    for i in range(nbs_demandeur):
        demandeurs[i].join()
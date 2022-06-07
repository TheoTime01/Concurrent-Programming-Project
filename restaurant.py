"""
Created on Tue May 31 8:10:28 2022
@author: Gorvien Mathis / Perrichet Théotime

"""

import multiprocessing as mp
import signal, sys, time, random

CLEARSCR="\x1B[2J\x1B[;H"        #  Clear SCReen

# VT100 : Actions sur le curseur
CURSON   = "\x1B[?25h"             #  Curseur visible
CURSOFF  = "\x1B[?25l"             #  Curseur invisible

def effacer_ecran() : print(CLEARSCR,end='')
def curseur_invisible() : print(CURSOFF,end='')
def curseur_visible() : print(CURSON,end='')

def move_to(lig, col) :
    print("\033[" + str(lig) + ";" + str(col) + "f",end='')

def Client(i,tableau,lock): # commande à intervalle irrégulier
    while True:
        time.sleep(random.randint(3,10)) # attente random
        lock.acquire() # assure qu'il est le seul à écrire dans le tampon
        for indice in range(0,len(tableau[:])-1,2): # parcours le tableau avec un pas de 2
            if tableau[indice] != -1: # si commande rentrée à cet emplacement, on passe au couple suivant
                pass
            else:
                tableau[indice] = i//100
                tableau[indice+1] = ord('A')+random.randint(0,25)
                break
        lock.release() # laisse la place à un autre client qui souhaiterai commander


def Serveur(Q,numero,tableau,lock):
    rien_faire = False # variable pour ne pas remplir la queue de messages indiquant qu'il est libre
    while True:
        lock.acquire() # assure qu'il est le seul à écrire dans le tampon
        
        # si il n'y à rien à la première place du tableau et que le serveur n'a jamais indiqué au major d'homme qu'il était libre
        if (tableau[0] == -1) and (rien_faire == False):
            Q.put((-1,-1,numero,-1)) # transmet au major d'homme son état ( -1 = serveur qui ne fait rien )
            lock.release() # laisse la place à un autre serveur libre
            rien_faire = True # memorise que le serveur à déja dit qu'il ne faisait rien
        
        # Si il y à une commande à la première place du tableau
        elif tableau[0] != -1:
            rien_faire = False # réinitialise la variable

            num_commande = tableau[0]
            plat = tableau[1]
            tableau[0] = -1
            tableau[1] = -1

            # le serveur décale toutes les commandes d'un pas en avant dans le tableau 
            indice = 0
            while indice <= (len(tableau[:])-2):
                if tableau[indice+2] == -1:
                    tableau[indice] = -1
                    tableau[indice+1] = -1
                    break
                else:
                    tableau[indice] = tableau[indice+2]
                    tableau[indice+1] = tableau[indice+3]
                indice += 2
            lock.release() # laisse la place à un autre serveur libre

            Q.put((num_commande,plat,numero,'preparation')) # envoie au major d'homme qu'il s'occupe d'une commande
            time.sleep(random.randint(3,5)) # simulation du temps de préparation de la commande
            Q.put((num_commande,plat,numero,'servit')) # envoie au major d'homme qu'il sert une commande
        else:
            lock.release() # laisse la place à un autre serveur libre


def Major_dHomme(Q,tableau,nb_serveurs):
    while True:
        arguments = Q.get() # recoie les informations des serveurs
        ident,plat,num_serveur,etat = arguments # stock chaque valeur reçu
        if etat == 'preparation':
            move_to(num_serveur,10)
            print(f"Le serveur {num_serveur} traite la commande ({ident,chr(plat)})         ")
        elif etat == 'servit':
            move_to(nb_serveurs+3,10)
            print(f"Le serveur {num_serveur} sert la commande ({ident,chr(plat)})           ")
        elif etat == -1: # si le serveur est dans l'état libre
            move_to(num_serveur,10)
            print(f"Le serveur {num_serveur} est libre                         ")
        
        # la liste d'attente qui contient chaque couple (identifiant,plat)
        liste_attente = []
        for indice in range(0,len(tableau[:])-1,2):
            if tableau[indice] != -1:
                liste_attente.append((tableau[indice],chr(tableau[indice+1])))
        move_to(nb_serveurs+1,10)
        print("Les commandes clients en attente :",liste_attente,"                                                                ")
        move_to(nb_serveurs+2,10)
        print("Nombres de commandes en attente :",len(liste_attente),"              ")

def FinService(signal,frame): # interruption avec un ctrl+c 
    global nb_serveurs
    move_to(nb_serveurs+4,10)
    print("Fin du service")
    curseur_visible()
    sys.exit(0)

#--------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    
    nb_client = 8
    nb_serveurs = 5
    taille_tableau = 50

    # le tableau est défini pour une taille de deux fois la taille demandée 
    # chaque commande prendra deux places dans le tableau
    # une première place pour le numero du client qui à commandé et le deuxième sera l'ascii du plat commandé
    tableau_commandes = mp.Array('b',[-1 for _ in range(taille_tableau*2)])
    access = mp.Lock() # Lock pour le tableau
    effacer_ecran() # effaçage de l'écran pour affichage
    curseur_invisible() # rend invisible le curseur
    pile = mp.Queue() # queue de discussion entre les serveurs et le major d'homme
    signal.signal(signal.SIGINT, FinService) # pour arreter le service

    # création de la liste des process et du lancement de ceux ci
    Lprocess = [mp.Process(target=Client,args=((i+1)*100,tableau_commandes,access)) for i in range(nb_client)]
    Lprocess.extend([mp.Process(target=Serveur,args=(pile,i+1,tableau_commandes,access)) for i in range(nb_serveurs)])
    Lprocess.append(mp.Process(target=Major_dHomme,args=(pile,tableau_commandes,nb_serveurs)))
    for p in Lprocess:
        p.start()
    for p in Lprocess:
        p.join()


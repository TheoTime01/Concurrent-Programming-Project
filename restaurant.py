# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 8:10:28 2022
@author: Gorvien Mathis / Perrichet Théotime

"""
import time,random,random
import multiprocessing as mp


semTampon = mp.Semaphore(1)
sem_Serveur = mp.Semaphore(1)
mutex = mp.Lock()

# %%----------------------Fonctions-------------------------------------------#

def Serveur(p_num, ptampon, proc_etat_Serveur, pService):
    """Fonction simulant un serveur
    Args:
        p_num (int): numéro du serveur
        ptampon (liste de 2 mp Array): contien 2 mp Array, respectivement le numéro du client et la lettre de la commande dans la liste d'attente
        proc_etat_Serveur ([liste de 2 mp Array): contien 2 mp Array, respectivement le numéro du client et la lettre de la commande que les serveur sont en train de traiter. Chaque mp Array à la même taille que pNombreProcServeur
        pService (mp Array): indique si le serveur a fini sont plat
    """
    while True:
        semTampon.acquire()
        mutex.acquire()

        num_Client = ptampon[1][0]
        lettre_Commande = ptampon[0][0]

        if num_Client != 0:   # on recupere la commande et on la retire de la liste
            ptampon[1] = fDecaleurListe(ptampon[1])
            ptampon[0] = fDecaleurListe(ptampon[0])
            
        mutex.release()
        semTampon.release()
        
        if num_Client == 0 :
            time.sleep(1)
        else:
            
            #print(f"le serveur {p_num} s'occupe de la commande {(num_Client,lettre_Commande)}")
            sem_Serveur.acquire()
            proc_etat_Serveur[0][p_num] = lettre_Commande
            proc_etat_Serveur[1][p_num] = num_Client
            sem_Serveur.release()

            time.sleep(random.randint(3,6))

            sem_Serveur.acquire()
            proc_etat_Serveur[0][p_num] = 0
            proc_etat_Serveur[1][p_num] = 0
            pService[p_num] = 1 
            sem_Serveur.release()


            #print(f"le serveur {p_num} a fini avec la commande {(num_Client,lettre_Commande)}")

def clients(ptampon, pTamponSize):
    """process simulant les client, générant les commandes
    Args:
        ptampon (liste de 2 mp Array): contien 2 mp Array, respectivement le numéro du client et la lettre de la commande dans la liste d'attente
        pTamponSize (int): taille du tampon
    """
    while True:
        semTampon.acquire()
        index = fFindLastNotNullIndex(ptampon[1])

        if index <= pTamponSize-1: #Si le carnet de commande n'est pas plein
            lettre_Commande = random.randint(1,26)
            num_Client = random.randint(1,10)

            ptampon[0][index] = lettre_Commande
            ptampon[1][index] = num_Client

        semTampon.release()

        time.sleep(1)

def major_dHomme(pNombreProcServeur, ptampon,pServeur, pService):
    """Fonction major d'homme qui sert à draw toutes les informations du programme
    Args:
        pNombreProcServeur (int): nombre de serveur
        ptampon (liste de 2 mp Array): contien 2 mp Array, respectivement le numéro du client et la lettre de la commande dans la liste d'attente
        pServeur (liste de 2 mp Array): contien 2 mp Array, respectivement le numéro du client et la lettre de la commande que les serveur sont en train de traiter. Chaque mp Array à la même taille que pNombreProcServeur
        pService (mp Array): indique si le serveur a fini sont plat
    """
    while True:
        semTampon.acquire()
        sem_Serveur.acquire()
        mutex.acquire()

        ptamponLettre = fIntListToAlphabet(fArrayToList(ptampon[0]))
        ptamponNumero = fArrayToList(ptampon[1])
        pServeurLettre = fIntListToAlphabet(fArrayToList(pServeur[0]))
        pServeurNumero = fArrayToList(pServeur[1])
        pEnService = fArrayToList(pService)
        pService = fResetList(pService)

        mutex.release()
        sem_Serveur.release()
        semTampon.release()

        print("\x1B[2J\x1B[;H",end='')

        for i in range(pNombreProcServeur):
            if pServeurNumero[i] == 0:
                print(f"Le serveur {i+1} traite la commande")
            else:
                print(f"Le serveur {i+1} traite la commande {(pServeurNumero[i],pServeurLettre[i])}")
        
        tailleListeCommande = fFindLastNotNullIndex(ptamponNumero)
        ListeCommande = []
        for i in range(tailleListeCommande):
            ListeCommande.append((ptamponNumero[i],ptamponLettre[i]))
        print(f"Les commandes clients en attentes : {ListeCommande}")
        print(f"Nombre de commandes en attente : {tailleListeCommande}")

        for i,element in enumerate(pEnService):
            if element == 1:
                print(f"Le serveur {i+1} à fini sa préparation et l'a servi au client")

        time.sleep(1)

def fFindLastNotNullIndex(pListe):
    """Retourne l'index du premier zéro trouvé dans pListe. Si pas de résultat, donne la TAILLE de la liste.
    Args:
        pListe (liste): liste de nombre avec un zéro (ou pas)
    Returns:
        int: index du premier zéro/longueur de la liste si pas trouvé
    """
    valren = len(pListe)
    for i,element in enumerate(pListe):
        if element == 0:
            valren = i
            break
    return valren

def fArrayToList(pArray):
    """Fonction permettant de transformer un Array de multiprocessing en liste 
    Args:
        pArray (mp Array): Array qui va être transformer en liste pour simplifier le traitement
    Returns:
        liste: exacte copie de l'array mais en liste :)
    """
    valren = []
    for i,element in enumerate(pArray):
        valren.append(element)
    return valren

def fIntListToAlphabet(pListe):
    """Converti les éléments d'une liste d'entier correspondant au numéro des lettres en liste de lettre
    Args:
        pListe (liste): liste d'élément dont les valeurs correspondent au numéro des lettres (0<=x<=26)
    Returns:
        liste: liste des lettres
    """
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    valren = []
    for i,element in enumerate(pListe):
        valren.append(alphabet[element])
    return valren

def fIntToAlphabet(pEntier):
    """Retourne la lettre associé au numéro fourni
    Args:
        pEntier (int): numéro de la lettre à retourner
    Returns:
        str: lettre
    """
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet[pEntier]

def fDecaleurListe(pListe):
    """Décalle les éléments d'une liste d'un index vers la gauche et met un 0 à la fin
    Args:
        pListe (Liste): Liste à décallé
    Returns:
        Liste: Liste avec les éléments décallés de 1 vers la gauche
    """
    for i in range(len(pListe)-1):
        pListe[i] = pListe[i+1]
    pListe[len(pListe)-1] = 0
    return pListe

def fResetList(pListe):
    """Rempli pListe avec des 0
    Args:
        pListe (Liste): Liste à remplir de 0
    Returns:
        Liste: Liste de la même taille que pListe mais remplie de 0
    """
    for i in range(len(pListe)):
        pListe[i] = 0
    return pListe

# %%----------------------Initialisation-----------------------------------------#

NombreProcServeur = 4
EquipeServeur =  [0 for i in range(NombreProcServeur)]
TamponSize = 20

tamponLettre = mp.Array('i',TamponSize)
tamponNumero = mp.Array('i',TamponSize)
ServeurLettre =  mp.Array('i',NombreProcServeur)
ServeurNumero =  mp.Array('i',NombreProcServeur)
EnService = mp.Array('i',NombreProcServeur)

tampon = [tamponLettre, tamponNumero]
etatServeur = [ServeurLettre, ServeurNumero]

# %%----------------------Lancement multiprocessing---------------------------------#

PClient = mp.Process(target=clients, args= (tampon, TamponSize))
PMajorHomme = mp.Process(target=major_dHomme, args= (NombreProcServeur, tampon, etatServeur, EnService))
for i in range(NombreProcServeur):
    EquipeServeur[i] = mp.Process(target=Serveur, args= (i, tampon, etatServeur, EnService))
  
PClient.start()
PMajorHomme.start()
for i in range(NombreProcServeur):
    EquipeServeur[i].start()

PClient.join()
PMajorHomme.join()
for i in range(NombreProcServeur):
    EquipeServeur[i].join()
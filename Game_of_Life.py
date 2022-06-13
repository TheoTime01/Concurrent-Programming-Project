"""
Created on Wed Jun 1 19:30:34 2022
@author: Gorvien Mathis / Perrichet Théotime

"""

import random
import multiprocessing as mp
import numpy as np

# Quelques codes d'échappement (tous ne sont pas utilisés)
CLEARSCR="\x1B[2J\x1B[;H"          #  Clear SCreen
CLEAREOS = "\x1B[J"                #  Clear End Of Screen
CLEARELN = "\x1B[2K"               #  Clear Entire LiNe
CLEARCUP = "\x1B[1J"               #  Clear Curseur UP
GOTOYX   = "\x1B[%.2d;%.2dH"       #  ('H' ou 'f') : Goto at (y,x), voir le code

DELAFCURSOR = "\x1B[K"             #  effacer après la position du curseur
CRLF  = "\r\n"                     #  Retour à la ligne

# VT100 : Actions sur le curseur
CURSON   = "\x1B[?25h"             #  Curseur visible
CURSOFF  = "\x1B[?25l"             #  Curseur invisible

# Actions sur les caractères affichables
NORMAL = "\x1B[0m"                  #  Normal
BOLD = "\x1B[1m"                    #  Gras
UNDERLINE = "\x1B[4m"               #  Souligné


# VT100 : Couleurs : "22" pour normal intensity
CL_BLACK="\033[22;30m"                  #  Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m"                    #  Rouge
CL_GREEN="\033[22;32m"                  #  Vert
CL_BROWN = "\033[22;33m"                #  Brun
CL_BLUE="\033[22;34m"                   #  Bleu
CL_MAGENTA="\033[22;35m"                #  Magenta
CL_CYAN="\033[22;36m"                   #  Cyan
CL_GRAY="\033[22;37m"                   #  Gris

# "01" pour quoi ? (bold ?)
CL_DARKGRAY="\033[01;30m"               #  Gris foncé
CL_LIGHTRED="\033[01;31m"               #  Rouge clair
CL_LIGHTGREEN="\033[01;32m"             #  Vert clair
CL_YELLOW="\033[01;33m"                 #  Jaune
CL_LIGHTBLU= "\033[01;34m"              #  Bleu clair
CL_LIGHTMAGENTA="\033[01;35m"           #  Magenta clair
CL_LIGHTCYAN="\033[01;36m"              #  Cyan clair
CL_WHITE="\033[01;37m"                  #  Blanc
#-------------------------------------------------------

# Définition de qq fonctions de gestion de l'écran
def effacer_ecran() : print(CLEARSCR,end='')
def erase_line_from_beg_to_curs() : print("\033[1K",end='')
def curseur_invisible() : print(CURSOFF,end='')
def curseur_visible() : print(CURSON,end='')


def move_to(lig, col) : # déplacement du curseur
    print("\033[" + str(lig) + ";" + str(col) + "f",end='')


def draw(tab): # Affiche le tableau de jeu sur l'écran
    effacer_ecran() # Efface l'écran
    curseur_invisible()
    i=0
    for raw in tab:
        for k in range(len(raw)):
            if raw[k]==1:
                move_to(i,k)
                print(CL_RED + "*")
            else:
                move_to(i,k)
                print(CL_YELLOW + "x")
        i+=1

def cellule(tab,largeur,hauteur,taille): # Calcule la valeur de la cellule
    sum = 0
    for x,y in ((largeur-1,hauteur),(largeur,hauteur-1),(largeur,hauteur+1),(largeur+1,hauteur)):
        if (x>=0 and y>=0) and (x<=taille-1 and y<=taille-1):
            sum += tab[x][y]
    return sum
    
def calcul(sum,tab,largeur,hauteur): # Calcul la valeur de la prochaine generation de cellules
    if tab[largeur][hauteur]==1: # Si la cellule est vivante
        if sum < 2: # Si elle a moins de 2 voisines vivantes
            Val = 0 # On la tue
        elif sum == 2 or sum == 3: # Si elle a 2 ou 3 voisines vivantes
            Val = 1 # On la garde
        elif sum > 3: # Si elle a plus de 3 voisines vivantes
            Val = 0 # On la tue
    else: # Si la cellule est morte
        if sum == 3: # Si elle a 3 voisines vivantes
            Val = 1 # On la vivifie
        else: # Si elle n'a pas 3 voisines vivantes
            Val = tab[largeur][hauteur] # On la garde
    return Val

def update(tab,largeur,hauteur,taille): # Création de la prochaine generation de cellules
    sum = cellule(tab,largeur,hauteur,taille)
    val = calcul(sum,tab,largeur,hauteur)

    lock.acquire()
    new_tab[largeur][hauteur] = val
    lock.release()







if __name__ == '__main__':
    
    taille = 20
    process = [[None for _ in range(taille)]for _ in range(taille)]
    lock=mp.Lock()
    tab = [[random.randint(0,1) for k in range(taille)] for i in range(taille)]
    new_tab_v = [[0 for k in range(taille)] for i in range(taille)]

    while not np.array_equal(new_tab_v, tab):

        draw(tab)

        new_tab_copie = mp.RawArray('d', taille*taille)
        new_tab = np.frombuffer(new_tab_copie, dtype=np.float64).reshape((taille,taille))

        for i in range(taille):
            for k in range(taille):
                process[i][k]= mp.Process(target=update, args=(tab,i,k,taille))
                process[i][k].start()
                process[i][k].join()

        new_tab_v = tab[:]
        tab = new_tab[:]

        

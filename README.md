
**Exercices d’introduction aux calculs parallèles Exercices avec Python**

(CPE 21-22)

(Version élèves)



Mai 2022

Plan (de ce document)

#2
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.002.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.003.png)

1. Plan (de ce document)
- I) Voir les documents pdf des 2 cours sur la programmation concurrente.

☞ Chaque exercice porte un barème.

Rendre assez d’exercices pour constituer 20 points. Tout point supplémentaire est en bonus.

- II) **Exercices à réaliser** avec la package multiprocessing.
  1. Course Hippique et affichage à l’écran (éventuellement avec le module *curses* de Python)
  1. Client-serveur de calculs
  1. Gestion des ressources (Billes)
  1. Calcul parallèle d’estimation de PI

← Il y a différentes autres techniques de calcul de PI

1. Merge-sort par de multiples Processus
1. Quick-sort par de multiples Processus
1. Compléments sur le calcul de Pi

Une 2nde séquence d’exercices est proposée par la suite.

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)
Quelques fonctions utiles

#3
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.005.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.006.png)

1. Quelques fonctions utiles

Dans la package **multiprocessing**, on dispose de quelques fonctions utilitaires :

- *multiprocessing.active\_children()* : renvoie la liste des processus fils encore en vie du processus courant.
- *multiprocessing.cpu\_count()* : renvoie le nombre de CPU (processus réellement parallèles pos- sibles) sur votre ordinateur.
- *multiprocessing.current\_process()* : renvoie l’objet Processus correspondant a processus cou- rant.
- *multiprocessing.parent\_process()* : renvoie un object Process qui correspond au parent du pro- cesssus courant. Pour le processus principal (main), le processus parent est None.
- voir les autres méthodes utilitaires en page

https ://docs.python.org/3.8/library/multiprocessing.html ?highlight=queue#multiprocessing.Queue

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)
Exercices à réaliser

#6
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.007.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.008.png)

1. Exercices à réaliser
   1. *Exercice : Course Hippique*

Difficulté : \*/\*\*\*\*\*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.009.png), **(3 points)**

On souhaite réaliser, sur les machine Linux, une course hippique. L’image suivante donne une idée de cette application (dans une fenêtre *Terminal* sous *Ubuntu*).

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.010.jpeg)

Pour ne pas compliquer la "chose"", on n’aura pas recours aux outils d’affichages graphiques. Les affichages se feront en console avec des séquences de caractères d’échappement (voir plus loin).

Chaque cheval est représenté simplement par une lettre (ici de ’A’ à ’T’) que l’on a entouré ici par ’(’ et ’>’ : ce qui donne par exemple ’(A>’ pour le premier cheval (vous pouvez laisser libre cours à vos talents d’artiste).

A chaque cheval est consacré une ligne de l’écran et la progression (aléatoire) de chaque cheval est affichée.

☞ Pour l’instant, ignorez les autres lignes affichées ("Best : .." et les suivantes). Ci-joint, une version basique de cette course pour 2 chevaux.

☞ Ce code ne devrait pas fonctionner sous Windows de Microsoft (qui ne dispose pas d’écran VT100 ou similaire).

☞ Pour en savoir plus sous Linux, reportez-vous à la page du manuel de "screen" (ou regarder sur le WEB).

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.011.png)


*# Nov 2021*

*# Course Hippique (version élèves)*

*# Version très basique, sans mutex sur l’écran, sans arbitre, sans annoncer le gagnant, ... ...*

*# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−*

*# VT100 : Actions sur le curseur*

*# Quelques codes d’échappement (tous ne sont pas utilisés) CLEARSCR="\x1B[2J\x1B[;H"	# Clear SCReen*

*CLEAREOS = "\x1B[J"	# Clear End Of Screen CLEARELN = "\x1B[2K"		# Clear Entire LiNe CLEARCUP = "\x1B[1J"		# Clear Curseur UP*

*GOTOYX = "\x1B[%.2d;%.2dH"	# (’H’ ou ’f’) : Goto at (y,x), voir le code*

*DELAFCURSOR = "\x1B[K"	# effacer après la position du curseur CRLF = "\r\n"	# Retour à la ligne*

*CURSON = "\x1B[?25h"	# Curseur visible CURSOFF = "\x1B[?25l"	# Curseur invisible*

*# VT100 : Actions sur les caractères affichables NORMAL = "\x1B[0m"	# Normal*

*BOLD = "\x1B[1m"	# Gras UNDERLINE = "\x1B[4m"		# Souligné*

*# VT100 : Couleurs : "22" pour normal intensity*

*CL\_BLACK="\033[22;30m"		# Noir. NE PAS UTILISER. On verra rien !! CL\_RED="\033[22;31m"	# Rouge*

*CL\_GREEN="\033[22;32m"	# Vert*

*CL\_BROWN = "\033[22;33m"	#  Brun*

*CL\_BLUE="\033[22;34m"	# Bleu CL\_MAGENTA="\033[22;35m"		# Magenta CL\_CYAN="\033[22;36m"	# Cyan*

*CL\_GRAY="\033[22;37m"	# Gris*

*# "01" pour quoi ? (bold ?) CL\_DARKGRAY="\033[01;30m"			# Gris foncé CL\_LIGHTRED="\033[01;31m"		# Rouge clair CL\_LIGHTGREEN="\033[01;32m"				# Vert clair CL\_YELLOW="\033[01;33m"	# Jaune*

*CL\_LIGHTBLU= "\033[01;34m"		# Bleu clair CL\_LIGHTMAGENTA="\033[01;35m"				# Magenta clair CL\_LIGHTCYAN="\033[01;36m"			# Cyan clair CL\_WHITE="\033[01;37m"	# Blanc*

*#−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−*

*# Juin 2019*

*# Cours hippique*

*# Version très basique, sans mutex sur l’écran, sans arbitre, sans annoncer le gagant, ... ...*

*# Quelques codes d’échappement (tous ne sont pas utilisés) CLEARSCR="\x1B[2J\x1B[;H"	# Clear SCReen*

*CLEAREOS = "\x1B[J"	# Clear End Of Screen CLEARELN = "\x1B[2K"		# Clear Entire LiNe CLEARCUP = "\x1B[1J"		# Clear Curseur UP*

*GOTOYX = "\x1B[%.2d;%.2dH"	# (’H’ ou ’f’) : Goto at (y,x), voir le code*

*DELAFCURSOR = "\x1B[K"	# effacer après la position du curseur CRLF = "\r\n"	# Retour à la ligne*

*# VT100 : Actions sur le curseur*

*CURSON = "\x1B[?25h"	# Curseur visible CURSOFF = "\x1B[?25l"	# Curseur invisible*

*# VT100 : Actions sur les caractères affichables NORMAL = "\x1B[0m"	# Normal*

*BOLD = "\x1B[1m"	# Gras UNDERLINE = "\x1B[4m"		# Souligné*

*# VT100 : Couleurs : "22" pour normal intensity*

*CL\_BLACK="\033[22;30m"		# Noir. NE PAS UTILISER. On verra rien !! CL\_RED="\033[22;31m"	# Rouge*

*CL\_GREEN="\033[22;32m"	# Vert*

*CL\_BROWN = "\033[22;33m"	#  Brun*

*CL\_BLUE="\033[22;34m"	# Bleu CL\_MAGENTA="\033[22;35m"		# Magenta*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.012.png)

*CL\_CYAN="\033[22;36m"	# Cyan*

*CL\_GRAY="\033[22;37m"	# Gris*

*# "01" pour quoi ? (bold ?) CL\_DARKGRAY="\033[01;30m"			# Gris foncé CL\_LIGHTRED="\033[01;31m"		# Rouge clair CL\_LIGHTGREEN="\033[01;32m"				# Vert clair CL\_YELLOW="\033[01;33m"	# Jaune*

*CL\_LIGHTBLU= "\033[01;34m"		# Bleu clair CL\_LIGHTMAGENTA="\033[01;35m"				# Magenta clair CL\_LIGHTCYAN="\033[01;36m"			# Cyan clair CL\_WHITE="\033[01;37m"	# Blanc*

*#−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−*

*import multiprocessing as mp*

*import os, time,math, random, sys, ctypes*

*# Une liste de couleurs à affecter aléatoirement aux chevaux*

*lyst\_colors=[CL\_WHITE, CL\_RED, CL\_GREEN, CL\_BROWN , CL\_BLUE, CL\_MAGENTA, CL\_CYAN, CL\_GRAY,*

*CL\_DARKGRAY, CL\_LIGHTRED, CL\_LIGHTGREEN, CL\_LIGHTBLU, CL\_YELLOW, CL\_LIGHTMAGENTA, CL\_LIGHTCYAN]*

*def effacer\_ecran() : print(CLEARSCR,end=’’)*

*def erase\_line\_from\_beg\_to\_curs() : print("\033[1K",end=’’) def curseur\_invisible() : print(CURSOFF,end=’’)*

*def curseur\_visible() : print(CURSON,end=’’)*

*def move\_to(lig, col) : print("\033[" + str(lig) + ";" + str(col) + "f",end=’’)*

*def en\_couleur(Coul) : print(Coul,end=’’)*

*def en\_rouge() : print(CL\_RED,end=’’) # Un exemple !*

*# La tache d’un cheval*

*def un\_cheval(ma\_ligne : int, keep\_running) : # ma\_ligne commence à 0 col=1*

*while col < LONGEUR\_COURSE and keep\_running.value : move\_to(ma\_ligne+1,col)	# pour effacer toute ma ligne erase\_line\_from\_beg\_to\_curs() en\_couleur(lyst\_colors[ma\_ligne%len(lyst\_colors)]) print(’(’+chr(ord(’A’)+ma\_ligne)+’>’)*

*col+=1*

*time.sleep(0.1 \* random.randint(1,5))*

*#−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−*

*# La partie principale :*

*def course\_hippique(keep\_running) :*

*Nb\_process=20*

*mes\_process = [0 for i in range(Nb\_process)]*

*effacer\_ecran() curseur\_invisible()*

*for i in range(Nb\_process): # Lancer	Nb\_process processus mes\_process[i] = mp.Process(target=un\_cheval, args= (i,keep\_running,)) mes\_process[i].start()*

*move\_to(Nb\_process+10, 1) print("tous lancés")*


*for i in range(Nb\_process): mes\_process[i].join()*

*move\_to(24, 1) curseur\_visible() print("Fini")*

*# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−*

*# La partie principale :*

*if  name  == " main   " :*

*LONGEUR\_COURSE = 100 # Tout le monde aura la même copie (donc no need to have a ’value’) keep\_running=mp.Value(ctypes.c\_bool, True)*

*course\_hippique(keep\_running)*

Travail à réaliser

#11
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.013.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.014.png)

1. **Travail à réaliser**

Compléter ce code pour réaliser les points suivants :

0. Vous constatez que les affichages à l’écran ne sont pas en exclusion mutuelle. Réglez ce problème en utilisant un mutex.
0. Ajouter un processus *arbitre* qui affiche en permanence le cheval qui est en tête ainsi que celui qui est dernier comme dans la figure ci-dessus. A la fin de la course, il affichera les éventuels canassons ex aequos.

← Pour cela, créer un processus supplémentaire et lui associer la fonction "arbitre"

0. Éventuellement, permettre dès le départ de la course, de prédire un gagnant (au clavier)
0. Essayer d’améliorer le dessin de chaque cheval en utilisant seulement des caractères du clavier (pas de symbole graphiques).

Par exemple, un cheval peut être représenté par (on dirait une vache !) :

` 	`*\/*

*/−−−− \_.\*

*/|	/*

*/\ /\*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.015.png)

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)

1. *Exercice : faites des calculs*

Difficulté : \*\*/\*\*\*\*\*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.016.png), **(3 à 5 points)**

Problème traité sous forme simple en cours : échange entre un client demandeur, un serveur calculateur. Consulter les pdfs du cours.

On souhaite réaliser **plusieurs calculs en parallèle** demandés par un à plusieurs demandeurs.

- **Version 1 : Un demandeur,** *n* **calculteurs.** (**3 points**)

Le processus demandeur dépose une expression arithmétique (par exemple 2 + 3) dans une file d’attente (*multiprocessing.Queue*) des demandes. Par ailleurs, chaque processus calculateur récu- père une expression, évalue l’expression et dépose le résultat dans une file d’attente des résultats.

Réalisez cette version.

- **Version 2 :** *m* **demandeurs,** *n* **calculteurs.** (**5 points**) Dans cette version, on a plusieurs demandeurs *di, i* = 1*..m*.

Dans ce cas, pour que les demandeurs récupèrent leurs propres résultats, il faudra identifier les demandes par le demandeur *di*.

Lorsque le résultat est calculé et déposé par un processus calculateur, il ajoute l’identifiant *di* du demandeur. Ainsi, le demandeur peut filtrer la Queue des résultats pour trouver les réponses à ses demandes.

Réaliser cette version en créant plusieurs demandeurs et plusieurs calculateurs capables de traiter des demandes de calculs fréquentes.

- Ajouter une variante où au lieu d’une expression, le demandeur communique une **fonction**

particulière à appliquer (*lambda function*) (**2 points**).

☞ L’exemple suivant donne une version avec **os.fork()** ou un demandeur (père) et un seul cal- culateur (le fils) communiquent via un **os.pipe()**. Rappelez-vous que les pipes sont utilisés pour la communication entre deux processus. Vous devez utiliser *multiprocessing.Queue* pour pouvoir établir une communication indifférenciée entre de multiples processus. Voir le cours pour des exemples de Queue.

*import time,os,random*

*def fils\_calculette(rpipe\_commande, wpipe\_reponse): print(’Bonjour du Fils’, os.getpid())*

*while True:*

*cmd = os.read(rpipe\_commande, 32) print("Le fils a recu ", cmd) res=eval(cmd)*

*print("Dans fils, le résultat =", res) os.write(wpipe\_reponse, str(res).encode()) print("Le fils a envoyé", res)*

- ![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.017.png)Le fils (qui fait les calculs)




*time.sleep(1)*

*os.\_exit(0)*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.018.png)

- Le père :
  - Prépare une opération arithmétique (p. ex. 2+3) ; la transmet au fils

*if  name  == " main   " :*

*rpipe\_reponse, wpipe\_reponse = os.pipe() rpipe\_commande, wpipe\_commande = os.pipe()*

*pid = os.fork() if pid == 0:*

*fils\_calculette(rpipe\_commande, wpipe\_reponse)*

*assert False, ’fork du fils n a pas marché !’ # Si échec, on affiche un message*

*else :*

*# On ferme les "portes" non utilisées os.close(wpipe\_reponse) os.close(rpipe\_commande)*

*while True :*

*# Le pere envoie au fils un calcul aléatoire à faire et récupère le résultat opd1 = random.randint(1,10)*

*opd2 = random.randint(1,10)*

*operateur=random.choice([’+’, ’−’, ’\*’, ’/’]) str\_commande = str(opd1) + operateur + str(opd2)*

*os.write(wpipe\_commande, str\_commande.encode()) print("Le père va demander à faire : ", str\_commande) res = os.read(rpipe\_reponse, 32)*

*print("Le Pere a recu ", res)*

*print(’−’\* 60) time.sleep(1)*
  - ![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.019.png)Récupère le résultat sur un *pipe*.

*Le père va demander à faire : 5/9 Bonjour du Fils 12851*

*Le fils a recu 5/9*

*Dans fils, le résultat = 0.5555555555555556 Le fils a envoyé 0.5555555555555556*

*Le Pere a recu 0.5555555555555556*

*−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−*

*Le père va demander à faire : 5/2 Le fils a recu 5/2*

*Dans fils, le résultat = 2.5 Le fils a envoyé 2.5*

*Le Pere a recu 2.5*

*−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−*

*Le père va demander à faire : 8\*6 Le fils a recu 8\*6*

*Dans fils, le résultat = 48*

*Le fils a envoyé 48 Le Pere a recu 48*

*−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−*

*...*
- ![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.020.png)Trace :


1. *Gestionnaire de Billes*

Difficulté : \*\*\*/\*\*\*\*\*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.021.png), **(5 points)**

On souhaite réaliser l’exemple suivant (lire à la fi de ce sujet à propos des variables de condition).

- N processus (p. ex. *N* = 4) ont besoin chacun d’un nombre *k* d’une ressource (p. ex. des Billes) pour avancer leur travail
- Cette ressource existe en un nombre limité : on ne peut satisfaire la demande de tout le monde en même temps.

Par exemple, la demande de *Processi*=1*..*4 est de (4*,* 3*,* 5*,* 2) billes et on ne dispose que de

*nb*\_*max*\_*billes* = 9 billes

- Chaque Processus répète la séquence (p. ex. *m* fois) :

"demander k ressources, utiliser ressources, rendre k ressources"

- Le "main" crée les 4 processus.

Il crée également un processus *controleur* qui vérifie en permanence si le nombre de Billes disponible est dans l’intervalle [0*..nb*\_*max*\_*billes*]

- Pour chaque *Pi*, l’accès à la ressource se fait par une fonction "demander(k)" qui doit bloquer le demandeur tant que le nombre de billes disponible est inférieur à k
- *Pi* rend les *k* billes acquises après son travail et recommence sa séquence

**Psoeudo algorithmes** :

*MAIN :*

*Creer 4 processus travailleurs (avec mp.Process) Lancer ces 4 processus*

*Creer un processus controleur Lancer controleur*

*... tourner les pouces un peu ... Attendre les fin des 4 orocessus Terimer le processus controleur*

- ![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.022.png)Main :

- Travailleur :

*Travailleur(k\_bills):*

*Iterer m fois :*

*demander k\_bills*

*simuler le travail avec un delai (sleep s sec.) renre k\_bills*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.023.png)

- Demander k billes :

*Demander(k\_bills): # Dans ce psoeudo−code, la gestion deu verrou/sémaphore est absente Tantque nbr\_disponible\_billes < k\_bills :	# Ce test doit être fait dans une Section Critique (SC)*

*se bloquer (sur un semaphore d’attente) <– Ne pas oublier de libérer le verrou avant de vous mettre en attente ! nbr\_disponible\_billes = nbr\_disponible\_billes − k\_bills*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.024.png)

- rendre k billes :




*rendre(k\_bills):*

*Dans une SC :*

*nbr\_disponible\_billes = nbr\_disponible\_billes + k\_bills*

*libérer ceux qui sont bloqués (sur un semaphore d’attente) # voir "demander"*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.025.png)

☞ Noter que **Demander(k\_bills)** sera équivalent à **sem.acquire(k\_jetons)** (fonction qui n’existe pas dans le package multiprocessing ) !

☞ De même pour **rendre** et **release()**

- Contrôleur :

*Controleur(max\_billes):*

*Iterer toujours :*

*Dans une SC :*

*Verifier que 0 <= nbr\_disponible\_billes <= max\_billes delai(1 sec)*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.026.png)

☞ A propos de demander() / rendre() :

- Dans *demander()*, un *if* à la place de *while* ne suffit pas.

Lorsqu’on sera réveillé (depuis *rendre()*) sur le sémaphore d’attente, il se pourrait que le nombre de billes libérées soit encore insuffisant pour satisfaire notre demande. Le *while* permet de refaire ce test.

- CeE mode de fonctionnement (se bloquer sur le sémaphore d’attente) est une **attente pas- sive** : on ne consomme pas du temps CPU et on attend que l’on nous réveille. [1](#_bookmark7)

*Demander\_attente\_active (k\_bills): # Dans ce psoeudo−code, la gestion deu verrou/sémaphore est absente demander verrou sur nb\_billes*

*Tantque nbr\_disponible\_billes < k\_bills : libérer verrou sur nb\_billes*

*attednre un peu # sleep(0.5) par exemple demander verrou sur nb\_billes*

*nbr\_disponible\_billes = nbr\_disponible\_billes − k\_bills*
- ![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.027.png)Dans une version différente avec une **attente active**, on peut écrire (code détaillé) :

*rendre\_attente\_active(k\_bills):*

*Dans une SC :*

*nbr\_disponible\_billes = nbr\_disponible\_billes + k\_bills*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.028.png)Dans cette version, il n’y a plus de sémaphore d’attente et par conséquent, la fonction *rendre()* ne contiendra plus une libération sur le même sémaphore d’attente.

☞ Voir cours : il existe également les **variables de condition** qui réalisent l’effet d’une attente passive (avec les primitive *attendre(condition) / signaler(condition) / signaler\_à\_tous(condition)* où p. ex. *condition = nbr\_disponible\_billes >= k\_billes*)




![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.029.png)

\1. Un exemple équivalent : supposons attendre un paquet par la poste. Dans une attente active, on regarde sans cesse par la fenêtre pour savoir si le facteur passe ! Dans une attente passive, on se met d’accord avec le facteur pour qu’il sonne quand il passe (pour nous réveiller).

Exemple : Calcul de PI par un cercle unitaire

#12
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.030.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.031.png)

1. *Estimation de PI*

☞ Ci-dessous, la version séquentielle. Voir le barème sur l’exercice qui vient ensuite..

- La valeur de PI peut être estimée de multiples manières. Nous en exposons une ci-dessous. D’autres méthodes sont exposées plus loin.
- Nous étudions ci-dessous la méthode qui utilise un cercle unitaire par une méthode séquentielle avant de donner (exercice) une solution parallèle (de la même méthode).

1. **Exemple : Calcul de PI par un cercle unitaire**

On peut calculer une valeur approché de PI à l’aide d’un cercle unitaire et la méthode Monte- Carlo (MC).

∈

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.032.png)**Principe** : on échantillonne un point (couple de réels (*x, y*)	[0*.*0*,* 1*.*0]) qui se situe dans 1 du

4

cercle unitaire et on examine la valeur de *x*2 + *y*2 ≤ 1 (équation de ce cercle).

c Si "vrai", le point est dans le quart du cercle unitaire (on a un *hit*)

c Sinon (cas de *miss*), ...

1
- ![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.033.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.034.png)Après *N* (grand) itérations, le nombre de *hits* approxime 4 de la surface du cercle unitaire, d’où

*N*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.035.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.036.png)la valeur de *π*. Notez que l’erreur de ce calcul peut être estimée à *√*1 .

- On programmera cette méthode, d’abord en Mono-processus (voir ci-dessous) puis en multi- processus. On comparera ensuite les temps de calculs.

1. **Principe Hit-Miss (Monte Carlo)**

*import random, time*

*# calculer le nbr de hits dans un cercle unitaire (utilisé par les différentes méthodes) def frequence\_de\_hits\_pour\_n\_essais(nb\_iteration):*

*count = 0*

*for i in range(nb\_iteration):*

*x = random.random() y = random.random()*

*# si le point est dans l’unit circle if x \* x + y \* y <= 1: count += 1*

*return count*

*# Nombre d’essai pour l’estimation nb\_total\_iteration = 10000000*

*nb\_hits=frequence\_de\_hits\_pour\_n\_essais(nb\_total\_iteration)*

*print("Valeur estimée Pi par la méthode Mono−Processus : ", 4 \* nb\_hits / nb\_total\_iteration) #TRACE :*

*# Calcul Mono−Processus : Valeur estimée Pi par la méthode Mono−Processus : 3.1412604*
- ![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.037.png)Le code Python suivant permet de calculer Pi selon le principe de hit-miss ci-dessus.

☞ Ajouter la mesure du temps du calcul (pour une comparaison ultérieure).

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)
Principe Hit-Miss (Monte Carlo)

#13
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.038.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.039.png)

1. *Exercice : Estimation parallèle de Pi*

Difficulté : \*/\*\*\*\*\*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.040.png), **(3 points)**

**Exercice-3 :** modifier le code précédent pour effectuer le calcul à l’aide de plusieurs Processus.

☞ Mesurer le temps et comparer.

**N.B.** : dans la méthode envisagée, on fixe un nombre (p. ex. *N* = 106) d’itérations.

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.041.png)Si on décide de faire ce calcul par *k* processus, chaque processus effectuera *N*

*k*

itérations.

Utiliser la fonction *time.time*() pour calculer le temps total nécessaire pour ce calcul. Vous consta- terez que ce temps se réduira lors d’utilisation des processus dans un calcul parallèle.

- Variantes de cette méthode : d’une des manières suivantes :

c 4 Processus où chacun effectue ces calculs sur un quart du cercle unitaire.

c Plusieurs Processus calculent sur le même quart du cercle et on prend la moyenne

c etc.


- Voir le section [III-H ](#_bookmark16)en page [17 ](#_bookmark16)pour les autres méthodes de calcul de Pi.

Version séquentielle de base

#14
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.042.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.043.png)

1. *Exercice : Calcul parallèle du Merge Sort*

Difficulté : \*\*\*/\*\*\*\*\*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.044.png), **(5 points)**

Le principe du tri fusion : pour trier un tableaux *T* de *N* éléments,

- Scinder *T* en deux sous-tableaux *T* 1 et *T* 2
- Trier *T* 1 et *T* 2
- Reconstituer *T* en fusionnant *T* 1 et *T* 2

c *T* 1 et *T* 2 sont chacun trié et leur fusion tient compte de cela.

1. **Version séquentielle de base**

*import math, random from array import array*

*def merge(left, right):*

*tableau = array(’i’, []) # tableau vide qui reçoit les résultats while len(left) > 0 and len(right) > 0:*

*if left[0] < right[0]: tableau.append(left.pop(0)) else: tableau.append(right.pop(0))*

*tableau += left + right return tableau*

*def merge\_sort(Tableau):*

*length\_Tableau = len(Tableau)*

*if length\_Tableau <= 1: return Tableau mid = length\_Tableau // 2*

*tab\_left = Tableau[0:mid] tab\_right = Tableau[mid:] tab\_left = merge\_sort(tab\_left)*

*tab\_right = merge\_sort(tab\_right) return merge(tab\_left, tab\_right)*

*def version\_de\_base(N):*

*Tab = array(’i’, [random.randint(0, 2 \* N) for \_ in range(N)]) print("Avant : ", Tab)*

*start=time.time()*

*Tab = merge\_sort(Tab) end=time.time() print("Après : ", Tab)*

*print("Le temps avec 1 seul Process = %f pour un tableau de %d eles " % ((end−start)\*1000, N))*

*print("Vérifions que le tri est correct −−> ", end=’’) try :*

*assert(all([(Tab[i] <= Tab[i+1]) for i in range(N−1)])) print("Le tri est OK !")*

*except : print(" Le tri n’a pas marché !")*
- ![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.045.png)Pour commencer, voyons la version de base du tri-fusion

Les résultats pour un tableau de 1000 éléments :

*N = 1000*

*version\_de\_base(N)*

*# Le temps avec 1 seul Process = 10.593414 pour un tableau de 1000 eles # Le tableau puis*

*# Vérifions que le tri est correct −−> Le tri est OK !*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.046.png)

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)
Exercice

#17
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.047.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.048.png)

1. **Exercice**

**Exercice-4 :** transformer cette version de base en une version de tri sur-place :

← Ne pas découper le tableau à trier en sous tableaux mais travailler avec des ’tranches’ de ce dernier. Par conséquent, un sous tableau de la version de base ci-dessus sera repéré par deux indices début - fin (= une zone du tableau global).

**Exercice-5 :** Écrire une version avec des Processus de cette méthode de tri : version parallèle de l’exercice 4.

☞ En général, chaque Processus sous-traite à un processus fils la moitié du tableau qui lui est assigné et s’occupe

lui-même de l’autre moitié.

☞ Au total, ne dépassez pas 8 processus pour un processeur Intel I7, 4 pour les modèles I5 ou I3.

☞ Pour représenter le tableau à trier, vous pouvez utiliser un ’Array’ mais le gain de performance ne sera pas sensible. Par contre, l’utilisation d’un *SharedArray* vous garantira un gain substantiel.

Pour une information plus complète sur ce module, voir le site https ://pypi.python.org/pypi/SharedArray

Extrait de ce site : un exemple d’utilisation de *SharedArray*.

*import numpy as np import SharedArray as sa*

*# Create an array in shared memory a = sa.create("shm://test", 10)*

*# Attach it as a different array. This can be done from another # python interpreter as long as it runs on the same computer. b = sa.attach("shm://test")*

*# See how they are actually sharing the same memory block a[0] = 42*

*print(b[0])*

*# Destroying a does not affect b. del a*

*print(b[0])*

*# See how "test" is still present in shared memory even though we # destroyed the array a.*

*sa.list()*

*# Now destroy the array "test" from memory. sa.delete("test")*

*# The array b is not affected, but once you destroy it then the # data are lost.*

*print(b[0])*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.049.png)

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)

1. *Exercice : tri-rapide*

Difficulté : \*\*/\*\*\*\*\*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.050.png), (5 points)

**Exercice-6 :** Faites de même avec la méthode de Tri Quick-Sort dont le principe et la version séquentielle de base sont rappelés ci-dessous.

**Principe de la méthode** :

Pour trier un tableaux *T* de *N* éléments,

- Désigner une valeur du tableau (dit le *Pivot p*)
- Scinder *T* en deux sous-tableaux *T* 1 et *T* 2 tels que les valeurs de *T* 1 soient ≤ *p* et celles de

*T* 2 soient *> p*

- Trier *T* 1 et *T* 2
- Reconstituer *T* en y plaçant *T* 1 puis *p* puis *T* 2

☞ Pour trier chacun des sous-tableaux, procéder de la même manière

☞ Pour le choix du pivot, on désigne en général le premier élément du tableau (sans garantie d’équité en tailles de *T* 1 et *T* 2)

☞ Au lieu de créer autant de processus que de sous tableaux, une gestion plus modérée des processus (pour ne pas en créer beaucoup) est recommandée. On se limitera à 8 sur un I7.

**Algorithme de la version de base**

*def qsort\_serie\_sequentiel\_avec\_listes(liste): if len(liste) < 2: return liste*

*# Pivot = liste[0]*

*gche = [X for X in liste[1:] if X <= liste[0]] drte = [X for X in liste[1:] if X > liste[0]]*

*# Trier chaque moitié "gauche" et "droite" pour regrouper en plaçant "gche" "Pivot" "drte"*

*return qsort\_serie\_sequentiel\_avec\_listes(gche) + [liste[0]] + qsort\_serie\_sequentiel\_avec\_listes(drte)*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.051.png)


1. *Autres méthodes de calcul de PI*

Pour indication et complément : il existe de multiples méthodes de calcul de PI. En voici quelques unes. Un seul exercice d’estimation de Pi peut-être rendu. Les méthodes ci-dessous sont informa- tives et n’ont donc pas de barème.


1. *PI par la méthode arc-tangente*

☞ Vu en cours.

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.052.jpeg)

☞ Une fois pour toutes, vérifier et donner la bonne formule.

← En bas, redonner 1/N, les élèves l’oublient !

*def arc\_tangente(n): pi = 0*

*for i in range(n):*

*pi += 4/(1+ ((i+0.5)/n)\*\*2) return (1/n)\*pi*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.053.png)**Indication** : pour vous aider, voilà l’exemple partiel du code (séquentiel) pour *n* donné qui met en place la formule ci-dessus :

Exercice

#19
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.054.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.055.png)

1. *Par la méthode d’espérance*

Difficulté : \*/\*\*\*\*\*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.056.png)

On tire *N* valeurs de l’abscisse *X* d’un point *M* dans [0; 1]

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.057.png)On calcule la somme *S* de *N* valeurs prises par *f* (*X*) = √1 − *X*2

La moyenne des ces *N* valeurs de *f* (*X*) est une valeur approchée de la moyenne de *f* et donc de

*N*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.058.png)l’aire du quart de cercle : *S* = *π/*4.

c La division par *N* (= nombre de *pas*) pour obtenir la surface des battons


1. ![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.059.png)*Par la loi Normale*

Difficulté : \*/\*\*\*\*\*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.060.png)

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)

Pour *x* centrée (*µ* = 0) suivant une loi *Normale*, *f* (*x*) = *σ*√2*π*

*x*2 *e−* 2*σ*2

Si	+*∞*

*−∞*



1

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.061.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.062.png)*f* (*x*) *dx* = 1

, on peut approximer la valeur de *π*

∫
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.063.png)☞ On peut utiliser une variable centrée réduite (*σ* = 1, *µ* = 0) pour simplifier les calculs avec

∫

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.064.png)*x*2

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.065.png)   1  *−*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.066.png)*f* (*x*) = √2*πe*	2

d’où

*∞*	1

*f* (*x*)*dx* =

0	2


1. *Approximation de PI par les Aiguilles de Buffon*

A

l

d

l sin(Q )

Q

d > l

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.067.png)On lance un certain nombre de fois une aiguille sur une feuille cadriée et l’on observe si elle croise des lignes horizontales. On peut également utiliser des stylos sur les lattes d’un parquet.

FIGURE 1 – Problème des Aiguilles de Buffon

Si la pointe est supposée fixe, la condition pour que l’aiguille croise une des lignes sera :

*A < l sin*(*θ*)

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.068.png)

La position de l’aiguille relative à la ligne la plus proche est un vecteur aléatoire

*V*(*Aθ*) *A* ∈ [0*, d*]	et	*θ* ∈ [0*, π*]

V est distribué uniformément sur [0*, d*] × [0*, π*]

*d.π*

*d*

*π*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.069.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.070.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.071.png)La fonc. de densité de probabilité (PDF) de *V* : 1   (= 1 × 1 )

← N.B. : *A* et *θ* sont indépendants (d’où la multiplication). La probabilité pour que l’aiguille croise une des lignes sera :

*π	lsin*(*θ*)   1  

∫	∫

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.072.png)*p* =



*dA dθ* =

 2*l*



[1]

0	0	*d.π*

*d.π*


**Détails de la formulation de** *p* **précédente :**

Le nombre de cas possibles pour la position du couple (*A, θ*) est représenté par l’aire du pavé :

*U* = [0*, d*] × [0*, π*]

Le nombre de cas où l’aiguille coupe une ligne horizontale est représenté par l’aire du domaine :

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.073.jpeg)*V* = {(*A, θ*) ∈ [0*, d*] × [0*, π*] : *A < l sin*(*θ*)}

∫

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.074.png)"L’aiguille coupe une ligne horizontale" avec la probabilité *Pr*\_*croisement* :


*Pr*\_*croisement* =

*aire*(*V* )

  1	*π*

\=



*l.sin*(*θ*) *dθ* =

 2*l*

*aire*(*U* )

*π.d*   0

*d.π*


☞ Mais le problème est que pour estimer *π*, on a besoin de *π* (pour les tirages aléatoires) !

Travail à réaliser

#20
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.075.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.076.png)

1. **Travail à réaliser**

Difficulté : \*\*/\*\*\*\*\*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.077.png)

1. Écrire le code séquentiel d’estimation de *π* (en utilisant *π* lui même pour les tirages !)

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.078.png)

◦

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.079.png)Prévoir une fonction **frequence\_hits(n)** qui procède au tirages par Monte Carlo et renvoie

*aire*(*V* )

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)

*Pr*\_*croisement* =



![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.080.png)

*aire*(*U* )

avec *n* tirages

0. Comme indiqué ci-dessus, la condition de croisement est *A < l sin*(*θ*) où

*A* ∈ [0*, d*] uniformément réparti

*θ* ∈ [0*, π*] uniformément réparti (oui, on utilise encore ici *π*)

*l* et *d* (avec *l* ≤ *d*) sont nos paramètres (resp. longueur aiguille et écart lattes parquet)

1. ![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.081.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.082.png)Estimer *π* =		2*.n	. l Pr*\_*croisement d*

☞ **Nous allons maintenant éviter l’utilisation de** *π* en faisant des tirages de l’angle *θ*.









A



dy = l sin(q )


l=longueur aiguille

dy

q

dx





d > l

d

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.083.png)Pour cela, procédez comme suit :

0. Quand on lance notre aiguille, on imagine un cercle de rayon *l* dont le centre est la pointe de l’aiguille.

Il nous reste à trouver les coordonnées (*dx, dy*) de son autre extrémité pour pouvoir obtenir l’angle *θ*. (la pointe centre se déplace) de sorte que (*dx, dy*) soit bien son autre extrémité !

1. Remplacer dans votre code l’usage de *sin*(*θ*) de la manière suivante :
- Prévoir une fonction *sin\_theta()* qui procède au tirage d’un couple (*dx, dy*)  ∈ [0*, l*] × [0*, l*], un point dans le cercle supposé être centré sur la pointe de l’aiguille.

c Il faut bien vérifier que (*dx, dy*) est bien dans le cercle (certains de ces points sont dans le carrée *l* × *l* et pas dans le cercle.)

- A l’aide de ces valeurs qui définissent une aiguille lancée, calculer *h* l’hypoténuse du tri-

angle droit dont les côtes sont *dx, dy, h* ; on comprend que *h* est "porté" par l’aiguille sur sa longueur *l* (*h* ≤ *l*) : par abus de notation, les vecteurs →−*h*  et →−*l*  sont confondus.

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.084.png)On peut alors calculer *sin*(*θ*) = *dy* que l’on notera *sin*\_*theta*.

*h*

1. Générer *A* ∈ [0*, d*], ce qui place l’aiguille sur le parquet !

← N.B. : on peut penser qu’il aurait fallu tirer (*dx, dy*) après le tirage aléatoire de *A* qui définirait les coordonnées de la tête (*tips*) de l’aiguille. Mais on peut aussi bien faire le tirage de (*dx, dy*) dans un repère avec tête de l’aiguille placée en (0*,* 0) avant de translater ce repère après le tirage de *A* (une homothétie).

1. Si on a *A < l . sin*\_*theta*, on un *hit* de plus.
1. On procède à *n* itération des étapes (3) à (6) pour obtenir *Pr*\_*croisement*

☞ N.B. : au lieu du cercle de rayon *l*, on peut aussi bien utiliser un cercla unitaire (accélère légè- rement les calculs) comme ci-après.

Travail à réaliser

#21
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.085.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.086.png)



*def calcul\_PI\_OK\_selon\_mes\_slides\_on\_evite\_use\_of\_PI\_version\_sequentielle() : L\_lg\_needle=10 # cm*

*D\_dist\_parquet= 10 # distance entre 2 lattes du parquet Nb\_iteration=10\*\*6*

*def tirage\_dans\_un\_cercle\_unitaire\_et\_sinus\_evite\_PI() :*

*def tirage\_un\_point\_dans\_cercle\_unitaire\_et\_calcul\_sinus\_theta() : while True :*

*dx = random.uniform(0,1) dy = random.uniform(0,1)*

*if dx\*\*2 + dy\*\*2 <= 1 : break sinus\_theta = dy/(math.sqrt(dx\*dx+dy\*dy)) return sinus\_theta*

*nb\_hits=0*

*for i in range(Nb\_iteration) :*

*# Theta=random.uniform(0,180) ne marche pas, il faut PI à la place de 180*

*# Mais puisqu’on veut le sinuus(theta), on se passe de theta et on caclcule sinus(theta) à # l’ancienne = (cote\_opposé / hypothenuse)*

*sinus\_theta = tirage\_un\_point\_dans\_cercle\_unitaire\_et\_calcul\_sinus\_theta() A=random.uniform(0,D\_dist\_parquet)*

*if A < L\_lg\_needle \* sinus\_theta : nb\_hits+=1*

*return nb\_hits nb\_hits=tirage\_dans\_un\_cercle\_unitaire\_et\_sinus\_evite\_PI()*

*print("nb\_hits : ", nb\_hits, " sur ", Nb\_iteration , " essais")*

*Proba=(nb\_hits)/Nb\_iteration # +1 pour éviter 0*

*print("Pi serait : ", (2\*L\_lg\_needle)/(D\_dist\_parquet\*Proba)) calcul\_PI\_OK\_selon\_mes\_slides\_on\_evite\_use\_of\_PI\_version\_sequentielle() # Trace :*

*# nb\_hits : 636512 sur 1000000 essais*

*# Pi serait : 3.1421245789553067*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.087.png)

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)
Addendum aux aiguilles de Buffon

#22
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.088.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.089.png)

1. **Addendum aux aiguilles de Buffon**

**Une autre formulation de** *p* **précédente :**

On repère le point milieu de l’aiguille (facilite la formulation).

A

X = l/2 sin( q )

q

d

d > l

l=longueur aiguille

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.090.png)Comme dans le cas précédent, Θ ∈ [0*, π*] mais *A* ∈ [0*, d*] représente la distance entre le milieu et la ligne horizontale (le plus proche).

- Cette fois, au lieu d’une double intégrale, nous utilisons une probabilité conditionnelle. Dans un lancer donné, supposons Θ = *θ* un angle particulier.

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.091.png)c L’aiguille croisera une ligne horizontale si la distance *A* est plus petite que	*X* = *l.sin*(*θ*) par

2

rapport à une des 2 lignes horizontales limitrophes.

Soit *E* l’événement : "l’aiguille croise une ligne". On a :

*l.sin*(*θ*)	*l.sin*(*θ*)

*d*

*d*

*d*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.091.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.092.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.093.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.094.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.095.png)*P* (*E*|Θ = *θ*) =	2	+	2	= *l.sin*(*θ*)

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.092.png)c Chaque *l.sin*(*θ*) est la proba pour une des 2 lignes horizontales,

2

c la division par *d* permet de normaliser (nécessaire dans le cas d’une probabilité).


![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)

On a alors la formulation de probabilité "totale" : où *f*Θ est la proba de *θ* = 1*/π*



*P* (*E*) =

*π*

∫

|

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.096.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.097.png)*P* (*E* Θ = *θ*) *f*Θ(*θ*) *dθ*

0

La probabilité de *E* est la loi de probabilité totale (équivalente à la double intégrale sur *θ* et *A*).


On a



*P* (*E*) =

∫ *π l.sin*(*θ*) 1



*dθ*	=

 1 ∫ *π*



*sin*(*θ*) *dθ* =

2*.l*

0	*d	π	πd*   0	*πd*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.098.jpeg)Pour estimer *P* (*E*) par la méthode Monte Carlo, on pourrait procéder à un tirage aléatoire dans le rectangle [0*, π*] × [0*, d*] du rectangle de côtés *d* × *π* (lire *a* = *d*) :

Estimation Laplacienne de pi

#23
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.099.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.100.png)

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.101.png)

1. **Estimation Laplacienne de pi**

Laplace (pour s’amuser !) a calculé une approximation de la valeur de *π* par ce résultat.

Soit *M* la variable aléatoire représentant le nombre de fois où l’aiguille a croisé une ligne (*E*(*M* )

l’espérence de M) :


![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.102.png)→ Probabilité de croiser une ligne =   *E*(*M* )

*n*

[2]

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.103.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.104.png)Les expressions [1] (vue ci-dessus) et [2] représentent la même probabilité : *E*(*M* ) = 2*l*



d’où :

*π* =

*n*

*E*(*M* )	*d*

*.*

2*l*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.105.png)*n	dπ*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.103.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.106.png)qui est un estimateur statistique de la valeur de *π*.

**Estimation de** *π* :

Si on lance l’aiguille *n* fois, elle touchera une ligne *m* fois.

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.107.png)← Dans  *π* =	2*.l.n*

*E*(*M* )*.d*

on peut remplacer la variable aléatoire *M* par *m* pour obtenir une esti-

mation de *π* :

2*.l.n π*ˆ ≈  *m.d*

En 1864, pendant sa convalescence, un certain Capitaine Fox a fait des tests et obtenu le tableau suivant :


|**n**|**m**|**l** (cm)|**d** (cm)|**Plateau**|**estimation** (*π*)|
| :-: | :- | :-: | :-: | :-: | :-: |
|500|236|7.5|10|stationnaire|3.1780|
|530|253|7.5|10|tournant|3.1423|
|590|939|12.5|5\*|tournant|3.1416|

Deux résultats importants à tirer de cette expérience :

1) La première ligne du tableau : résultats pauvre

0. Fox a fait tourner le plateau (son assise ?) entre les essais
0. Cette action (confirmée par les résultats) élimine le **biais** de sa position (dans le tirages).
0. Il est important d’éliminer le biais dans l’implantation de la méthode MCL. Le biais vient souvent des générateurs de nombres aléatoires utilisés (équivalent à la position du lanceur dans ces lancers).

1) Dans ses expériences, Fox a aussi utilisé le cas *d < l* (dernière ligne du tableau).

   0. L’aiguille a pu croiser plusieurs lignes (le cas \* du tableau : n=590, m=939).
   0. Cette technique est aujourd’hui appelée la technique de **réduction de variance**.

Estimation Laplacienne de pi

#24
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.108.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.109.png)

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.004.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.110.png)






**Table des matières**
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.111.png)


1. [Plan (de ce document)](#_bookmark0)	2
1. [Quelques fonctions utiles](#_bookmark1)	3
1. [Exercices à réaliser](#_bookmark2)	4

[III-AExercice : Course Hippique](#_bookmark3) 	4

[III-A-T1ravail à réaliser](#_bookmark4) 	7

[III-BExercice : faites des calculs](#_bookmark5)	8

[III-CGestionnaire de Billes](#_bookmark6)	10

[III-DEstimation de PI](#_bookmark8) 	12

[III-D-1Exemple : Calcul de PI par un cercle unitaire](#_bookmark9) 	12

[III-D-2Principe Hit-Miss (Monte Carlo)](#_bookmark10) 	12

[III-EExercice : Estimation parallèle de Pi](#_bookmark11)	13

[III-FExercice : Calcul parallèle du Merge Sort](#_bookmark12)	14

[III-F-1Version séquentielle de base](#_bookmark13)	14

[III-F-2Exercice](#_bookmark14)	15

[III-GExercice : tri-rapide](#_bookmark15) 	16

3. [HAutres méthodes de calcul de PI](#_bookmark16) 	17
   9. [PI par la méthode arc-tangente](#_bookmark17)	17
   9. [Par la méthode d’espérance](#_bookmark18)	18

[III-KPar la loi Normale](#_bookmark19)	18

[III-LApproximation de PI par les Aiguilles de Buffon](#_bookmark20)	19

[III-L-1Travail à réaliser](#_bookmark21)	20

[III-L-2Addendum aux aiguilles de Buffon](#_bookmark22)	22

[III-L-3Estimation Laplacienne de pi](#_bookmark23)	23

[**Table des matières](#_bookmark23)	**23**




25

















Partie 2 : Exercices

Contrôleur de température (& Pression) Déplacements d’un Robot

Game of Life CPE - Mai 2022


(Version élèves)

ASG


Projets CPE : Python Concurrent

#1
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.112.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.113.png)

1. Projets CPE : Python Concurrent
- Ce document contient 3 sujets :
  - Contrôleur de température / Pression
  - Simulation des déplacements d’un Robot
  - Simulation des serveurs/client/cuisiniers d’un restaurant
  - Game of life


Réalisation d’une système muti-tâche de contrôle de Température et Pression

#2
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.114.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.115.png)

1. Réalisation d’une système muti-tâche de contrôle de Tempéra- ture et Pression

Difficulté : \*\*/\*\*\*\*\*

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.116.png), **(4 points)**




On considère le système (*temps réel embarqué*) simple suivant :

- Un **processus T** lit les valeurs d’un ensemble de thermocouples (par l’intermédiaire d’un convertisseur analogique-numérique, CDA).

c T commande les changements appropriés à un chauffage (par l’in- termédiaire d’un commutateur à commande numérique).

- Le **processus P** a une fonction similaire pour la pression (il emploie un au convertisseur numérique-analogique, DAC).
- T et P doivent communiquer des données au **processus S**, qui pré- sente des mesures à un opérateur par l’intermédiaire d’un écran.
- Notez que P et T sont les entités actives ; S est une ressource (il ré- pond juste aux demandes de T et de P) : il peut être mis en application comme ressource protégée ou serveur s’il agit plus intensivement avec l’utilisateur (avec différents réglages et *consignes* possibles).
- L’objectif global de ce système temps réel embarqué est de maintenir la température et la pression d’un certain processus chimique dans des limites définies.








Thermocouple	A

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.117.png)/ D


![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.118.png)**Switches**



**T**




**S**

**Chauffage**



Ecran
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.119.png)






A	Capteurs

/	Pression

D








**P**






D	**Pompe/Valve**

/ A

- Un vrai système de ce type serait clairement plus complexe, permettant par exemple à l’opérateur de modifier les limites (consignes).
- Le but de ce système est de conserver la température et la pression d’un processus chimique dans des limites spécifiées.
- Un vrai système sera plus complexe, par exemple, permettre à un opérateur de modifier ces limites.
- Deux approches : synchrone (cyclique) et asynchrone. T : Thermocouple

P : Pression

S : Écran (screen)

- On distingue plusieurs entités concurrentes :
  - Gestionnaire de la température (T)
  - Gestionnaire de la pression(P)
  - Gestionnaire du Chauffage
  - Gestionnaire de la Pompe
  - La tâche Ecran (S)
  - Un contrôleur pour coordonnée l’ensemble
- Par ailleurs, nous utiliserons une zone mémoire partagée pour ...

et protégée par un verrou (un sémaphore est également possible).

Réalisation d’une système muti-tâche de contrôle de Température et Pression

#3
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.120.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.121.png)






**Déclarations :**

Ver : Verrou – cf. TAS Seuil\_T, Seuil\_P : réel *←* .. go\_pompe : bool *←* faux go\_chauffage : bool *←* faux *mem*\_*xx* : mémoire partagée

————————————-

☞ mémoire partagée :

si *thread* (ou task ADA) utilisés alors une variable globale si non un *shmem*. c Certains langages proposent des va- riables **protégées** = variable globale + Verrou mutex

**Tâche Contrôleur :**

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.122.png)Répéter toutes les *X* secondes verrouiller(Ver) ;

*T ← MemT	P ← MemP*

libérer(Ver) ;

Si (*T > Seuil*\_*T* )

go\_chauffage *←* faux    – pour le chauffage Si (*P > Seuil*\_*P* )

go\_pompe *←* vrai    – pour la Pompe

Sinon go\_pompe *←* faux Sinon Si (*T < Seuil*\_*T* )

go\_pompe *←* vrai

go\_chauffage *←* vrai Sinon     – *T* = *Seuil*\_*T* go\_chauffage *←* faux

Si (*P > Seuil*\_*P* ) go\_pompe *←* vrai Sinon go\_pompe *←* faux

Fin Répéter








**Tâche Chauffage :**

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.122.png)Répéter toutes les *Z* secondes Si (go\_chauffage) Alors

"mettre en route" Sinon "arrêter"

Fin si Fin Répéter

- En général, le contrôleur crée les tâches après sa propre création.


**Tâche Température :**

Répéter toutes les *S* secondes lire la valeur *V* sur le capteur Convertir\_AD(*V* ,*T* ) verrouiller(Ver)     ; Ecrire(*T* ,*MemT* )

libérer(Ver) ; Fin Répéter

**Tâche Pression :**

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.123.png)Répéter toutes les *U* secondes lire la valeur *V* sur le capteur Convertir\_AD(*V* ,*P* ) verrouiller(Ver)     ; Ecrire(*P* ,*MemP* )

libérer(Ver) ; Fin Répéter

**Tâche Pompe :**

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.123.png)Répéter toutes les *Z* secondes Si (go\_pompe) Alors

"mettre en route" Sinon "arrêter"

Fin si

Fin Répéter

**Tâche Ecran :**

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.124.png)Répéter verrouiller(Ver) ; *T ← MemT*

*P  ← MemP*

libérer(Ver) ; écrire *T* et *P*

Fin Répéter

- La gestion par les booléennes *go\_pompe, go\_chauffage* peut être remplacée par le mécanisme d’évènement (*Attendre, Signaler*) :

c la tâche Pompe fera *Attendre(go\_pompe)* conjugué avec *Signaler(go\_pompe)* effectué par le Contrôleur.

- Ces booléennes n’ont pas besoin d’un accès en *mutex* car le *contrôleur* y écrit et Pompe (ou Chauffage) lisent.

Simulation des déplacements d’un Robot

#4
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.125.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.126.png)

1. Simulation des déplacements d’un Robot

Difficulté : \*\*\*/\*\*\*\*\*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.127.png), **(5 points)**

☞ La partie graphique doit impérativement être réalisée sous **TkInter**. Les versions qui existent sur le WEB ne sont pas acceptées (ne sont pas réalisées avec Tkinter) !

- Un robot avec les caractéristiques suivants
- Pas de but particulier : avancer et éviter les obstacles
- Plusieurs capteurs : infra rouge (IR) sur les 2 côtés, sonar (US) frontal, de contact (Bumper) frontal
- Les actions sur les servo moteurs : *avancer*, *reculer*, *tourner à gauche/droite*
- Le comportement par défaut est : *avancer*
- Un écran d’affichage de l’état
- Principes : lecture des capteurs








**Déclarations :**

Ver : Verrou – cf. TAS les Distances : réel *←* ..

les Drepeaux : bool *←* faux

*mem*\_*xx* : mémoire partagée

————————————-

☞ mémoire partagée :

si *thread* (ou task ADA) utilisés alors une variable globale si non un *shmem*. c Certains langages proposent des va- riables **protégées** = variable globale + Verrou mutex



**Tâche Controleur :**

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.128.png)Répéter toutes les *X* secondes Commande *←* "avancer" Drapeau *←* faux

Si (Drapeau\_IR) Alors Commande *←* Cmd\_IR Drapeau *←* Drapeau\_IR

Si (Drapeau\_US) Alors Commande *←* Cmd\_US Drapeau *←* Drapeau\_US

Si (Drapeau\_BU) Alors Commande *←* Cmd\_BU Drapeau *←* Drapeau\_BU

Transmettre *Commande* aux servos verrouiller(Ver) ;

*mem*\_*Cmd ← Commande mem*\_*Flag ← Drapeau* libérer(Ver) ;

Fin Répéter









**Tâche Ecran :**

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.128.png)Répéter tou sles *A* secondes verrouiller(Ver) ;

*C ← mem*\_*Cmd F ← mem*\_*Flag* libérer(Ver) ; écrire *C* et *F*

Fin Répéter

- En général, le contrôleur crée les tâches après sa propre création.

Simulation des déplacements d’un Robot

#5
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.129.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.130.png)




**Tâche IR :**

Répéter toutes les *S* secondes

lire la valeur *V g* sur le capteur gauche lire la valeur *V d* sur le capteur droit Convertir\_AD(*V  g*,*Dg*) Convertir\_AD(*V d*,*Dd*)

Si *Dg < d* OU *Dd < d* Alors Drapeau\_IR *←* vrai

Si *Dg < d* ET *Dd < d* Alors Cmd\_IR *←* "reculer"

Sinon  Si  *Dg  < d* Alors Cmd\_IR *←* "à gauche" Sinon Cmd\_IR *←* "à droite"

Sinon Drapeau\_IR *←* faux Fin Répéter

**Tâche US :**

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.131.png)Répéter toutes les *K* secondes

lire la valeur *V* sur le capteur Convertir\_AD(*V* ,*D*)

Si *D < d* Alors Drapeau\_US *←* vrai Cmd\_US *←* "reculer"

Sinon Drapeau\_US *←* faux Fin Répéter

**Tâche Bumper :**

Répéter toutes les *Z* secondes (*Z* petit) Si (contact=1) Alors

Drapeau\_BU *←* vrai Cmd\_BU *←* "reculer"

Sinon Drapeau\_BU *←* faux Fin Répéter

**Remarque** sur "Répéter toutes les *X* milli/micro/nanosecondes" : Un moyen simple d’implanter ce délai :

Next ← temps actuel (clock) Répéter

Actions

*Next* ← *Next* + *X*

*delay* until next Fin Répéter

- Si *delay* non disponible :

Temps ← temps actuel (clock) Répéter

Actions

Next ← temps actuel (clock) Reste ← X - (Next - Temps)

Attendre(Reste) – e.g. usleep/sleep Temps ← Next

Fin Répéter

c Bien entendu, *Reste >* 0 sinon, le système n’est pas RT ! !

Simulation des déplacements d’un Robot

#6
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.132.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.133.png)

Un système muti-tâches de simulation d’un restaurant

Difficulté : \*\*/\*\*\*\*\*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.134.png), **(5 points)**

On considère le système (*temps réel*) simple suivant qui :

1. simule des commandes de clients dans un restaurant
1. un certains nombre de serveurs en salle enregistrent ces commandes et les transmettent à la cuisine pour pré- paration
1. après leur préparation, les serveurs délivrent ces commandes aux clients

**Dans la version de base**, on n’identifie pas de cuisinier et ce sont les serveurs qui simulent la préparation des com- mandes (voir plus bas pour la version étendue).

**Prévoir :**

- *s* processus *serveur*. P. Ex. *s* = 5
- un processus *clients* qui simulera aléatoirement les commandes des clients selon une loi uniforme. Ce processus émettra une commande aléatoire toutes les p. ex. 3*..*10 *secondes* à l’adresse des serveurs.
- un processus *major\_dHomme* qui s’occupera des affichages à l’écran
- un tampon de taille (p. ex.) 50 contiendra les commandes des clients ; les serveurs prélèvent des commandes de ce tableau
- une commande d’un client sera constituée d’un identifiant client (un entier) et une lettre *A..Z* qui représentera le menu commandé

En l’absence d’interface graphique, on utilisera le module **curses** de Python que l’on a déjà utilisé dans l’exemple cours de chevaux. On affichera ainsi à l’écran les informations suivants :

- les commandes des clients (les paires *(id, menu)*) dès leur émission
- le serveur qui prend cette commande en charge et simule sa préparation (par un délai)
- le client qui reçoit sa commande préparée

**Le serveur** 1 **traite la commande** (*idi, Ci*)   (ou rien si pas de commande traité par ce serveur)

....

**Le serveur** *s* **traite la commande** (*idj, Cj*)

**Les commandes clients en attente : [**(*idi, Ci*) **,** (*idj, Cj*) **. . .** (*idk, Ck*) **] Nombres de commandes attente :** 5

**Commande** (*idu, U* ) **est servie au client**

![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.135.png)☞ Les informations sont affichées exclusivement par le processus *major\_dHomme*. Un exemple d’affichage à l’écran :


Simulation des déplacements d’un Robot

#7
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.136.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.137.png)

**Aller plus loin (Bonus) :**

Ajouter un certains nombre de cuisiniers (en cuisine) qui préparent ces commandes et avertissent les serveurs. Le serveur qui avait enregistré la commande la délivre au client qui a commandée.

**Ajouter à l aversion de base :**

- *c* processus *cuisto*. P. Ex. *c* = 2
- Modifier les affichage et présenter le cuisinier qui traite la commande. Le contenu de l’écran sera augmenté des lignes :

**Le cuisiner** 1 **prépare la commande** (*id*1*, A, serveur*1)   (ou rien si pas de commande traité par ce cuisinier)

....

**Le cuisiner** *c* **prépare la commande** (*idp, P, serveurp*)


Game of Life

#8
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.001.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.138.png)![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.139.png)

1. Game of Life

Difficulté : \*\*/\*\*\*\*\*
![](Aspose.Words.9ac306d7-c237-4f3e-969e-b99ad69ed175.140.png), **(5 points)**

Réaliser le jeu suivant dans une version **concurrente** avec les mécanismes de base graphique (*screen* comme dans la course Hippique).

Il s’agit d’une grille (matrice de taille d’au moins 15*x*15) dont les cases représentent soit un "être" vivant soit rien. L’état d’une case peut être modifié en fonction de son voisinage selon les règles décrites ci-dessous.

Extrait de l’énoncé d’origine :

- The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead.
- Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur :
  - Any live cell with fewer than two live neighbours dies, as if caused by under-population.
  - Any live cell with two or three live neighbours lives on to the next generation.
  - Any live cell with more than three live neighbours dies, as if by overcrowding.
  - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

- The initial pattern constitutes the seed of the system.
- The first generation is created by applying the above rules simultaneously to every cell in the seed-births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one).
- The rules continue to be applied repeatedly to create further generations.	


ASG, Novembre 2021


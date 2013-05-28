from plateau_de_jeu import *
from random import randint
import sys

#Paramètres de l'IA Negamax
depth = 0
maxdepth = 3

def set_maxdepth(n):
    global maxdepth
    maxdepth = n
#Joue un coup aléatoire parmi ceux possibles
def Aleatoire(t, joueur):
    l = liste_coups_possibles(t, joueur)
    coup = randint(0, len(l) -1)
    jouer(l[coup][0], l[coup][1], joueur)

def Maximiser(t, joueur):
    print(joueur)
    plus_grand_nombre_retournes = 0
    meilleur_coup = None
    for i in range(Dim):
        for j in range(Dim):
            retournes = 0
            for dir in range(8):
                retournes += tester_position(t,i,j,dir,joueur)
            if retournes > plus_grand_nombre_retournes:
                plus_grand_nombre_retournes = retournes
                meilleur_coup = (i,j)
    jouer(meilleur_coup[0], meilleur_coup[1], joueur)

def Negamax(t, joueur, depth, maxdepth):
    if depth == maxdepth:
        return evaluer(t, joueur) #TODO créer une fonction evaluer
    else:
        meilleur_valeur = -sys.maxint
        l = liste_coups_possibles(t,joueur)
        for i in range(len(l)):
            jouer(l[i][0], l[i][0], joueur)
            valeur_courante = Negamax(Matrice, -joueur, depth + 1, maxdepth)
            undo #TODO faire une fonction undo
            valeur_courante = -valeur_courante
            if meilleure_valeur < valeur_courante:
                meilleur_valeur = valeur_courante
                meilleur_coup = l[i]
        if len(l) == 0:
            Negamax(Matrice -joueur, depth + 1, maxdepth)
    return meilleur_coup

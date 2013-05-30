from plateau_de_jeu import *
from random import randint
import sys

#Paramètres de l'IA Negamax
depth = 0
maxdepth = None

def set_maxdepth(n):
    global maxdepth
    maxdepth = n

def get_maxdepth():
    return maxdepth

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

def Negamax(t, joueur, depth,maxdepth): #Je pense pas qu'elle soit juste, mais
    meilleur_coup = None # ça joue
    if depth == maxdepth:
        return (evaluer(t, joueur), 0)
    else:
        meilleure_valeur = -20000
        l = liste_coups_possibles(t,joueur)
        for i in range(len(l)):
            jouer(l[i][0], l[i][1], joueur)
            ajouter_tableau_sauvegarde(Matrice)
            tupl = Negamax(Matrice, -joueur, depth + 1, maxdepth)
            valeur_courante = tupl[0]
            print("la valeur_courant après Negamax est:" + str(valeur_courante))
            undo(1)
            valeur_courante = -valeur_courante
            if meilleure_valeur < valeur_courante:
                meilleure_valeur = valeur_courante
                meilleur_coup = l[i]
        if len(l) == 0:
            tupl = Negamax(Matrice, -joueur, depth + 1, maxdepth)
            meilleure_valeur = tupl[0]
            meilleure_coup = tupl[1]
    return (meilleure_valeur, meilleur_coup)

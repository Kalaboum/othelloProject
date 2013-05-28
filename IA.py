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

def Negamax(t, joueur, depth, maxdepth): #Observations valeur_courante toujours
    print("profondeur" + str(depth)) #locale, trouver une autre méthode
    if depth == maxdepth:
        valeur_courante = evaluer(t, joueur)
        return
    else:
        meilleure_valeur = -20000
        valeur_courante = -20000
        l = liste_coups_possibles(t,joueur)
        for i in range(len(l)):
            print("la valeur_courante est:" + str(valeur_courante))
            jouer(l[i][0], l[i][0], joueur)
            ajouter_tableau_sauvegarde(Matrice)
            Negamax(Matrice, -joueur, depth + 1, maxdepth)
            print("la valeur_courant après Negamax est:" + str(valeur_courante))
            undo(1)
            valeur_courante = -valeur_courante
            if meilleure_valeur < valeur_courante:
                meilleure_valeur = valeur_courante
                meilleur_coup = l[i]
        if len(l) == 0:
            Negamax(Matrice, -joueur, depth + 1, maxdepth)
    return meilleur_coup

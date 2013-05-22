from jeu import *
from random import *
#Joue un coup aléatoire parmi ceux possibles

def Aleatoire(t, joueur):
    listeCoupsPossibles = []
    for i in range(N):
        for j in range(N):
            if position_valide(t,i,j,joueur):
                listeCoupsPossibles.append((i,j))#ajoute les coordonnées d'un
#coup valide dans un tuple
    coup = random.randint(0, len(listeCoupsPossibles) -1)
    jouer(listeCoupsPossibles[coup][0], listeCoupsPossibles[coup][0], joueur)

from plateau_de_jeu import *
from random import randint

#Joue un coup aléatoire parmi ceux possibles
def Aleatoire(t, joueur):
    listeCoupsPossibles = []
    print(listeCoupsPossibles)
    for i in range(N):
        for j in range(N):
            if position_valide(t,i,j,joueur):
                listeCoupsPossibles.append((i,j))#ajoute les coordonnées d'un
#coup valide dans un tuple
    print (listeCoupsPossibles)
    coup = randint(0, len(listeCoupsPossibles) -1)
    print("coup joué par IA :" + str(listeCoupsPossibles[coup][0]) 
 + " " + str(listeCoupsPossibles[coup][0]))
    print("Joueur de l'IA :" + str(joueur))
    jouer(listeCoupsPossibles[coup][0], listeCoupsPossibles[coup][1], joueur)
    afficher_tableau(Matrice)

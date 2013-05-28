from plateau_de_jeu import *
from random import randint

#Joue un coup aléatoire parmi ceux possibles
def Aleatoire(t, joueur):
    listeCoupsPossibles = []
    #print(listeCoupsPossibles)
    for i in range(Dim):
        for j in range(Dim):
            if position_valide(t,i,j,joueur):
                listeCoupsPossibles.append((i,j))#ajoute les coordonnées d'un
#coup valide dans un tuple
    #print (listeCoupsPossibles)
    coup = randint(0, len(listeCoupsPossibles) -1)
   # print("coup joué par IA :" + str(listeCoupsPossibles[coup][0]) 
# + " " + str(listeCoupsPossibles[coup][0]))
    #print("Joueur de l'IA :" + str(joueur))
    jouer(listeCoupsPossibles[coup][0], listeCoupsPossibles[coup][1], joueur)
    #afficher_tableau(Matrice)

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

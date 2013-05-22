from grille_v2 import *

def main():
    global joueur_actif
    ### On paramètre arbitrairement des variables initiales avant que la personnalisation soit disponible
    typejoueur = ["Humain",None,"IA"] #Bricolage, voir comment faire mieux
    jeuFini = False
    dernierJoueurAJoue = True
#Attention à faire toujours jouer le bon joueur
    while jeuFini == False:
        if peut_jouer(Matrice, joueur_actif):
            if typejoueur[joueurActif + 1] == "Humain":
                HumainPeutJouer = True #Créer variable globale HumainPeutJouer
            elif typejoueur[joueur_actif + 1] == "Negamax":
                Negamax(Matrice, joueurActif)
            elif typejoueur[joueur_actif + 1] == "IAAleatoire":
                Aleatoire(Matrice, joueur_actif)
            dernierJoueurAJoue = True
        else:
            if not dernierJoueurAJoue:
                jeuFini = True
        joueur_actif = -joueur_actif
        
            

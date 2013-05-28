from plateau_de_jeu import *
from IA import *

#Passe la main aux IA avant le prochain tour humain
def attendre_tour_humain(t, joueur):
    prochain_joueur = joueur
    while True:
        prochain_joueur = trouver_prochain_joueur(t, prochain_joueur)
        if prochain_joueur == None:
            print("Jeu Fini")
            return
        set_joueur_actif(prochain_joueur)
        type_prochain_joueur = get_typejoueur(prochain_joueur)
        if type_prochain_joueur == "Humain":
            set_Humain_peut_jouer(True)
            return
        elif type_prochain_joueur == "IAAleatoire":
            Aleatoire(t, prochain_joueur)
        elif type_prochain_joueur == "IAMaximiser":
            Maximiser(t,prochain_joueur)
        elif type_prochain_joueur == "Negamax":
            tupl = Negamax(Matrice, prochain_joueur, 0, maxdepth)
            jouer(tupl[1][0],tupl[1][1],prochain_joueur)
        ajouter_tableau_sauvegarde(Matrice)

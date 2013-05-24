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
     #   elif type_prochain_joueur == "Negamax":
#Appeler fonction Negamax quand elle sera opé

from plateau_de_jeu import *
from IA import *
import time

total_temps = []
nbr_coups = 0

def moyenne(temps, coups):
    tot = 0.0
    for i in range (len(temps)):
        tot += temps[i]
    return tot/coups

IA_disponible=[("IAAleatoire",None),("IAMaximiser",None),("Negamax",2),("Negamax",4),("Negamax",6)]

#Passe la main aux IA avant le prochain tour humain
def attendre_tour_humain(t, joueur):
    global total_temps, nbr_coups
    prochain_joueur = joueur
    while True:
        prochain_joueur = trouver_prochain_joueur(t, prochain_joueur)
        if prochain_joueur == None:
            print("Jeu Fini")
            return
        set_joueur_actif(prochain_joueur)
        type_prochain_joueur = get_typejoueur(prochain_joueur)
        # start = time.time()
        if type_prochain_joueur == "Humain":
            set_Humain_peut_jouer(True)
            return
        elif type_prochain_joueur == "IAAleatoire":
            Aleatoire(t, prochain_joueur)
        elif type_prochain_joueur == "IAMaximiser":
            Maximiser(t,prochain_joueur)
        elif type_prochain_joueur == "Negamax":
            tupl = Negamax(Matrice, prochain_joueur, 0, get_maxdepth())
            jouer(tupl[1][0],tupl[1][1],prochain_joueur)
        elif type_prochain_joueur == "Negamax_alpha_beta":
            tupl = Negamax_alpha_beta(Matrice, prochain_joueur, 0, maxdepth,
                                      -10000000,10000000)
            jouer(tupl[1][0],tupl[1][1],prochain_joueur)
        elif type_prochain_joueur == "Negamax_alpha_beta_empowered":
            tupl = Negamax_alpha_beta_empowered(Matrice, prochain_joueur, 0, maxdepth,
                                      -10000000,10000000)
            jouer(tupl[1][0],tupl[1][1],prochain_joueur)
        ajouter_tableau_sauvegarde(Matrice)
        # elapsed = time.time() - start
        # print(" temps écoulé pour l'IA " + str(elapsed)) 
        # nbr_coups += 1
        # total_temps.append(elapsed)
        # moye = moyenne(total_temps, nbr_coups)
        # print(" la moyenne : " + str(moye))
        

def niveau_IA(n):
    ia_en_cour=get_typejoueur(-1)
    maxdepth_courant=get_maxdepth()
    indice_dans_IA_disponible=indice_occurence(IA_disponible,(ia_en_cour,maxdepth_courant))
    if 0 <= n+indice_dans_IA_disponible <= len(IA_disponible)-1:
        set_typejoueur(-1,IA_disponible[n+indice_dans_IA_disponible][0])
        set_maxdepth(IA_disponible[n+indice_dans_IA_disponible][1])
    print("IA : "+ str(get_typejoueur(-1))+" | maxdepth : "+ str(get_maxdepth()))
    print(maxdepth)

def changement_mode_de_jeu():
    if get_typejoueur(-1)=="Humain":
        set_typejoueur(-1,"IAMaximiser")
        set_maxdepth(None)
    else:
        set_typejoueur(-1,"Humain")

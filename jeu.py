from plateau_de_jeu import *
from IA import *
import time

total_temps = []
nbr_coups = 0

#Fonction utilisée pour calculer le temps d'execution du Negamax
def moyenne(temps, coups):
    tot = 0.0
    for i in range (len(temps)):
        tot += temps[i]
    return tot/coups

IA_disponible=[("IAAleatoire",None),("IAMaximiser",None),("Negamax_alpha_beta_empowered",2),\
               ("Negamax_alpha_beta_empowered",4),("Negamax_alpha_beta_empowered",6)]

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
            tupl = Negamax_alpha_beta(Matrice, prochain_joueur, 0,get_maxdepth(),
                                      -10000000,10000000)
            jouer(tupl[1][0],tupl[1][1],prochain_joueur)
        elif type_prochain_joueur == "Negamax_alpha_beta_empowered":
            tupl = Negamax_alpha_beta_empowered(Matrice, prochain_joueur, 0, get_maxdepth(),
                                      -10000000,10000000)
            jouer(tupl[1][0],tupl[1][1],prochain_joueur)
        ajouter_tableau_sauvegarde(Matrice)
        # elapsed = time.time() - start
        # print(" temps écoulé pour l'IA " + str(elapsed)) 
        # nbr_coups += 1
        # total_temps.append(elapsed)
        # moye = moyenne(total_temps, nbr_coups)
        # print(" la moyenne : " + str(moye))
        
#Les options du menu de modification du niveau de l'IA utilisent cette fonction
def niveau_IA(n):
    #On recupère les données de jeu utile pour identifier le niveau actuel de l'IA
    ia_en_cour=get_typejoueur(-1)
    maxdepth_courant=get_maxdepth()
    #On identifie le niveau de l'IA actuel 
    indice_dans_IA_disponible=indice_occurence(IA_disponible,(ia_en_cour,maxdepth_courant))
    #On change si c'est possible dans le sens choisi (+ ou -)
    if 0 <= n+indice_dans_IA_disponible <= len(IA_disponible)-1:
        set_typejoueur(-1,IA_disponible[n+indice_dans_IA_disponible][0])
        set_maxdepth(IA_disponible[n+indice_dans_IA_disponible][1])
        
def changement_mode_de_jeu():
    if get_typejoueur(-1)=="Humain":
        set_typejoueur(-1,"IAMaximiser")
        set_maxdepth(None)
    else:
        set_typejoueur(-1,"Humain")

#Calcul le nombre de matrice qu'il faut enlever du tableau de sauvegarde
#On reviens en effet d'un nombre differents de matrice en arrière suivant le mode de jeu
def n_coup_avant(): 
    joueur = get_joueur_actif()
    if get_typejoueur(joueur) == get_typejoueur(-joueur): #Cas de Humain vs Humain
        undo(1)
        if dernier_joueur() != joueur:
            set_joueur_actif(-joueur)
    else:
        n = coup_dernier_joueur_humain()
        undo(n)

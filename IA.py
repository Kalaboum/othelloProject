from plateau_de_jeu import *
from random import randint
import sys

#Paramètres de l'IA Negamax
depth = 0
maxdepth = 6

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
            retournes = nbr_retournes(t,i,j,joueur)
            if retournes > plus_grand_nombre_retournes:
                plus_grand_nombre_retournes = retournes
                meilleur_coup = (i,j)
    jouer(meilleur_coup[0], meilleur_coup[1], joueur)

def Negamax(t, joueur, depth, maxdepth): #Je pense pas qu'elle soit juste, mais
    meilleur_coup = None # ça joue
    if not (peut_jouer(t,joueur)) and not (peut_joueur(t,joueur)):
        return score_absolu(t,joueur)*20000
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

def Negamax_alpha_beta(t, joueur, depth, maxdepth, alpha, beta):
    meilleur_coup = None # ça joue
    if depth == maxdepth:
        return (evaluer(t, joueur), 0)
    else:
        meilleure_valeur = alpha
        l = liste_coups_possibles(t,joueur)
        for i in range(len(l)):
            jouer(l[i][0], l[i][1], joueur)
            ajouter_tableau_sauvegarde(Matrice)
            tupl = Negamax_alpha_beta(Matrice, -joueur, depth + 1, maxdepth, -beta, -meilleure_valeur)
            undo(1)
            valeur_courante = tupl[0]
            valeur_courante = -valeur_courante
            if meilleure_valeur < valeur_courante:
                meilleure_valeur = valeur_courante
                meilleur_coup = l[i]
            if meilleure_valeur >= beta:
                return (meilleure_valeur, meilleur_coup)
        if len(l) == 0:
            tupl = Negamax_alpha_beta(Matrice, -joueur, depth + 1, maxdepth, -beta, -meilleure_valeur)
            meilleure_valeur = tupl[0]
            meilleure_coup = tupl[1]
    return (meilleure_valeur, meilleur_coup)

def Negamax_alpha_beta_empowered(t, joueur, depth, maxdepth, alpha, beta):
    meilleur_coup = None # ça joue
    if depth == maxdepth:
        return (evaluer(t, joueur), 0)
    else:
        meilleure_valeur = alpha
        l = liste_coups_possibles(t,joueur)
        if depth <=2:
            trier_liste_pour_alpha_beta(l,t,joueur)
        for i in range(len(l)):
            jouer(l[i][0], l[i][1], joueur)
            ajouter_tableau_sauvegarde(Matrice)
            tupl = Negamax_alpha_beta_empowered(Matrice, -joueur, depth + 1, maxdepth, -beta, -meilleure_valeur)
            undo(1)
            valeur_courante = tupl[0]
            valeur_courante = -valeur_courante
            if meilleure_valeur < valeur_courante:
                meilleure_valeur = valeur_courante
                meilleur_coup = l[i]
            if meilleure_valeur >= beta:
                return (meilleure_valeur, meilleur_coup)
        if len(l) == 0:
            tupl = Negamax_alpha_beta_empowered(Matrice, -joueur, depth + 1, maxdepth, -beta, -meilleure_valeur)
            meilleure_valeur = tupl[0]
            meilleure_coup = tupl[1]
    return (meilleure_valeur, meilleur_coup)


def trier_liste_pour_alpha_beta(l,t, joueur):
    s = []
    for i in range(len(l)):
        s.append(nbr_retournes(t,l[i][0],l[i][1], joueur))
    triShaker_avec_alpha_beta(s,l)


def triShaker_avec_alpha_beta(s,l):
    hasChanged = True
    lastChange = 0
    i = 0
    while hasChanged:
        hasChanged=False
        if i%2 == 0:
            for k in range(len(s)-1, lastChange, -1):
                if s[k-1] > s[k]:
                    echange(s, k, k-1)
                    echange(l, k, k-1)
                    hasChanged=True
                    lastChange=k-1
        else:
            for k in range(lastChange, len(s)):
                if s[k-1] > s[k]:
                    echange(s, k, k-1)
                    echange(l, k, k-1)
                    hasChanged=True
                    lastChange=k-1
                    
def echange(t, i, j):
    c = t[i]
    t[i] = t[j]
    t[j] = c

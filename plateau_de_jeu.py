from tableaux import *
import sys

####### IMPORTANT ########

#J'ai changer en N en Dim, car c'étais une variable globale du module
#tkinter.filedialog, j'ai galerer comme un connard pendant 30min
#pour trouver que N='n' dans ce module xD

#############################

# TO DO: Pouvoir initialiser les variables par l'interface graphique
# Ps : sens trigo dans ordre croissant
Dim=8 #Cote du tableau, voila, changement ^^
di=[0,-1,-1,-1,0,1,1,1] 
dj=[1,1,0,-1,-1,-1,0,1]
joueur_actif = 1# Joueur blanc: -1 | Joueur noir: 1
Matrice=creer_tableau(Dim,Dim,0)
Humain_peut_jouer = True
type_joueur = ["Negamax",None,"Humain"] #Bricolage, voir comment faire
# mieux
tableau_sauvegarde = [] #Tableau contenant toutes les matrices de jeu

# Les accesseurs/mutateurs (c'pas ça l'encapsulation d'ailleurs ?)

def set_Humain_peut_jouer(boolean):
    global Humain_peut_jouer
    Humain_peut_jouer = boolean

def set_Dim(Taille):
    global Dim
    Dim = Taille

def get_Dim():
    global Dim
    return Dim

def get_Matrice():
    global Matrice
    return Matrice

def get_typejoueur(n):
    return type_joueur[n+1]

def set_typejoueur(n, string):
    global type_joueur
    type_joueur[n+1] = string

def get_joueur_actif():
    global joueur_actif
    return joueur_actif

def set_joueur_actif(n):
    global joueur_actif
    joueur_actif = n

def set_Matrice(t):
    global Matrice
    copier_tableau(t, Matrice)

def get_element_tableau_sauvegarde(indice):
    global tableau_sauvegarde
    return tableau_sauvegarde[indice]

def get_tableau_sauvegarde():
    global tableau_sauvegarde
    return tableau_sauvegarde

def set_tableau_sauvegarde(t):
    global tableau_sauvegarde
    tableau_sauvegarde = []
    for i in range (len(t)):
        ajouter_tableau_sauvegarde(t[i])

def ajouter_tableau_sauvegarde(t):
    global tableau_sauvegarde
    t_copie = creer_tableau(len(t),len(t),0)
    copier_tableau(t, t_copie)
    tableau_sauvegarde.append(t_copie)

def supprimer_n_elements_sauvegarde(n):
    global tableau_sauvegarde
    for i in range(n):
        tableau_sauvegarde.pop()
        
# les fontions
def avant_dernier_joueur():
    if len(get_tableau_sauvegarde()) >= 3:
        t1 = get_element_tableau_sauvegarde(-2)
        t2 = get_element_tableau_sauvegarde(-3)
        if score_absolu(t1,1) > score_absolu(t2,1):
            return 1
        return -1
    return get_joueur_actif()

def dernier_joueur():
    if len(get_tableau_sauvegarde()) >= 2:
        t1 = get_element_tableau_sauvegarde(-1)
        t2 = get_element_tableau_sauvegarde(-2)
        if score_absolu(t1,1) > score_absolu(t2,1):
            return 1
        return -1
    return get_joueur_actif()

def undo(n):
    if len(tableau_sauvegarde)> n:
        supprimer_n_elements_sauvegarde(n)
        set_Matrice(tableau_sauvegarde[-1])

def initialiser_Matrice():
    global Matrice
    set_joueur_actif(1)  
    Matrice[Dim//2][Dim//2]=-1
    Matrice[Dim//2 -1][Dim//2 -1]=-1
    Matrice[Dim//2 -1][Dim//2]=1
    Matrice[Dim//2][Dim//2 -1]=1
    tableau_sauvegarde=[]
    ajouter_tableau_sauvegarde(Matrice)

def score_absolu(t, joueur): 
    count = 0
    for i in t:
        for j in i:
            if j == joueur:
                count += 1
    return count

def score(t):
    score_blanc = nb_occurences_tableau(Matrice,-1)
    score_noir = nb_occurences_tableau(Matrice,1)
    return (score_blanc,score_noir)

def tester_position(t,i,j,dir,joueur):
    if t[i][j] == 0:
        i+=di[dir]
        j+=dj[dir]
        c=0
        while 0<=i<Dim and 0<=j<Dim and t[i][j]==-joueur:
            c+=1
            i+=di[dir]
            j+=dj[dir]
            if  i<0 or j<0 or j>=Dim or i>=Dim or t[i][j] == 0:
                return 0
        return c
    return 0

def position_valide(t,i,j,joueur):
    dir=0
    while dir<=7: # Test dans toutes les directions
        if tester_position(t,i,j,dir,joueur)>0:
            return True
        dir+=1
    return False

def peut_jouer(t,joueur):
    for i in range(Dim):
        for j in range(Dim):
           if position_valide(t,i,j,joueur):
                return True
    return False

def retourner_pions(t,i,j,dir,n,joueur):
    while n>0:
        i+=di[dir]
        j+=dj[dir]
        t[i][j]=joueur
        n-=1
        
def jouer(i,j,joueur):
    t= get_Matrice()
    if position_valide(t,i,j,joueur):
        for dir in range(8):
            nb_return= tester_position(t,i,j,dir,joueur)
            if nb_return >0:
                retourner_pions(t,i,j, dir,nb_return,joueur)
        t[i][j]=joueur
        joueur=-joueur
        return joueur
    return None

#Trouve le prochain joueur qui doit jouer sur le tableau en prenant en paramètre
# le dernier joueur qui a joué
def trouver_prochain_joueur(t, joueur):
    prochain_joueur = -joueur
    if not peut_jouer(t, prochain_joueur):
        prochain_joueur = -prochain_joueur
        if not peut_jouer(t, prochain_joueur):
            return None
    return prochain_joueur

def liste_coups_possibles(t, joueur):
    l = []
    for i in range(Dim):
        for j in range(Dim):
            if position_valide(t,i,j,joueur):
                l.append((i,j)) #ajoute les coordonnées d'un coup valide
# dans un tuple
    return l

def evaluer(t, joueur):
    score = 0
    for i in range(Dim):
        #Surpondération des coins et des bords
        for j in range(Dim):
            if (i == 0 or i == Dim-1) and (j == 0 or j == Dim-1):
                score += 4*t[i][j]
            elif i == 0 or i == Dim-1 or j == 0 or j == Dim -1:
                score += 2* t[i][j]
            else:
                score += t[i][j]
    return score * joueur
        

from tableaux import *

#Déclaration des variables globales et leurs valeurs par défaut


Dim=8 
di=[0,-1,-1,-1,0,1,1,1] 
>>>>>>> d2a3e5aa88fa831095ac5e5e6f72cb25e883cbf4
dj=[1,1,0,-1,-1,-1,0,1]
joueur_actif = 1# Joueur blanc: -1 | Joueur noir: 1
Matrice=creer_tableau(Dim,Dim,0)
Humain_peut_jouer = True
type_joueur = ["Negamax_alpha_beta_empowered",None,"Humain"] #Stocke le type des joueurs
tableau_sauvegarde = [] #Tableau contenant toutes les matrices de jeu

# Les accesseurs/mutateurs (Getters/Setters)
# Ils sont là à cause de la modularité des variables globales,
# de la difficulté de changer les listes (pointeurs)
# et pour garder une meilleure modularité dans le code 

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

def set_Matrice_Dim(t,n):
    global Dim, Matrice
    Dim = n
    Matrice = []
    for i in range (len(t)):
        Matrice.append(t[i])
    
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
        

# les fonctions

def coup_dernier_joueur_humain():
    joueur_humain = get_joueur_actif()
    n = 1
    t = get_tableau_sauvegarde()
    while n+1 <= len(t):
        t1 = t[-n]
        t2 = t[-(n+1)]
        if score_absolu(t1, joueur_humain) > score_absolu(t2, joueur_humain):
            return n
        n+= 1
        
def undo(n):
    if len(tableau_sauvegarde)> n:
        supprimer_n_elements_sauvegarde(n)
        set_Matrice(tableau_sauvegarde[-1])

def joueur_victorieux(t):
    if score_blanc(t)>score_noir(t):
        return "blancs"
    return "noirs"

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
            count += j
    return count*joueur

def score_blanc(t):
    return nb_occurences_tableau(t,-1)

def score_noir(t):
    return nb_occurences_tableau(t,1)

def score(t):
    return (score_blanc(t),score_noir(t))

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


#Fonctions utiles pour les IA types Negamax

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

def nbr_retournes(t, i, j, joueur):
    retournes = 0
    for dir in range(8):
        retournes += tester_position(t,i,j,dir,joueur)
    return retournes

#Pondération des cases pour evaluer_v2

def score_pos(t, i, j):
    if (i == 0 or i == Dim -1) and (j==0 or j == Dim -1):
        return 1000
    elif (i == 0 or i == 1 or i == Dim-1 or i == Dim-2)\
        and (j == 0 or j == 1 or j == Dim-1 or j  == Dim-2):
        return -100
    elif i == 0 or i == Dim-1 or j== 0 or j== Dim-1:
        return 100
    else:
        return 1
        
def evaluer_v2(t, joueur):
    score = 0
    for i in range(Dim):
        for j in range(Dim):
            score += score_pos(t,i,j) * t[i][j]
    return score*joueur


if __name__ == "__main__":
    tableau_scores = creer_tableau(Dim, Dim, 0)
    for i in range (Dim):
        for j in range(Dim):
            tableau_scores[i][j] = score_pos(tableau_scores,i,j)
    print("tableau de pondération pour Dim = 8")
    print()
    afficher_tableau(tableau_scores)
    print()
    print("On passe à Dim = 4")
    t = creer_tableau(4,4,0)
    for i in range (1,3):
        for j in range (1,3):
            if (i+j)%2 == 0:
                t[i][j] = 1
            else:
                t[i][j] = -1
    afficher_plateau(t)
    set_Matrice_Dim(t,4)
    afficher_plateau(Matrice)
    t2 = creer_tableau(4,4,0)
    for i in range(Dim):
        for j in range(Dim):
            t2[i][j] = score_pos(t2,i,j)
    print()
    print("tableau de pondération")
    afficher_tableau(t2)
    Matrice[0][0] = 1
    Matrice[0][1] = -1
    afficher_plateau(Matrice)
    print("evaluer_v2 de Matrice pour joueur 1 = " + str(evaluer_v2(Matrice, 1)))

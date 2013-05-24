from tableaux import *
import sys

# TO DO: Pouvoir initialiser les variables par l'interface graphique
# Ps : sens trigo dans ordre croissant
N=8 #Cote du tableau
di=[0,-1,-1,-1,0,1,1,1] 
dj=[1,1,0,-1,-1,-1,0,1]
joueur_actif = 1# Joueur blanc: -1 | Joueur noir: 1
Matrice=creer_tableau(N,N,0)
Humain_peut_jouer = True
type_joueur = ["IAMaximiser",None,"Humain"] #Bricolage, voir comment faire
# mieux

def set_Humain_peut_jouer(boolean):
    global Humain_peut_jouer
    Humain_peut_jouer = boolean

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

def initialiser_Matrice():
    set_joueur_actif(1)  
    Matrice[N//2][N//2]=-1
    Matrice[N//2 -1][N//2 -1]=-1
    Matrice[N//2 -1][N//2]=1
    Matrice[N//2][N//2 -1]=1
    
def afficher_ligne():
    for i in range(N):
        sys.stdout.write("---")

def afficher_plateau(t):
    afficher_ligne()
    print(" ")
    for i in range(N):
        for j in range(N):
            if t[i][j] == 0:
                sys.stdout.write("  ")
            elif t[i][j] == -1:
                sys.stdout.write("-1")
            else:
                sys.stdout.write(" 1")
            sys.stdout.write('|')
        print("")
        afficher_ligne()
        print('')

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
        while 0<=i<N and 0<=j<N and t[i][j]==-joueur:
            c+=1
            i+=di[dir]
            j+=dj[dir]
            if  i<0 or j<0 or j>=N or i>=N or t[i][j] == 0:
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
    for i in range(N):
        for j in range(N):
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
    global Matrice
    t= creer_tableau(N,N,0)
    copier_tableau(Matrice,t)
    if position_valide(t,i,j,joueur):
        for dir in range(8):
            nb_return= tester_position(t,i,j,dir,joueur)
            if nb_return >0:
                retourner_pions(t,i,j, dir,nb_return,joueur)
        t[i][j]=joueur
        print(joueur)
        joueur=-joueur
        print(joueur)
        copier_tableau(t,Matrice)
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

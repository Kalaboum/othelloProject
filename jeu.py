from tableaux import *
import sys
# Ps : sens trigo dans ordre croissant
N=8
di=[0,-1,-1,-1,0,1,1,1]
dj=[1,1,0,-1,-1,-1,0,1]
joueur=-1 # Joueur blanc: -1 | Joueur noir: 1
Matrice=creer_tableau(N,N,0)

def initialiser(): 
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
        

def score(t):
    score = 0
    for i in t:
        for j in i:
            score += j
    return score

def tester_position(t,i,j,dir):
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

def position_valide(t,i,j):
    dir=0
    while dir<=7: # Test dans toutes les directions
        if tester_position(t,i,j,dir)>0:
            return True
        dir+=1
    return False

def peut_jouer(t,joueur):
    for i in range(N):
        for j in range(N):
            if position_valide(t,i,j,joueur):
                return True
    return False

def retourner_pions(t,i,j,dir,n):
    while n>0:
        i+=di[dir]
        j+=dj[dir]
        t[i][j]=joueur
        n-=1
        
def jouer(i,j): 
    global joueur,Matrice
    t= creer_tableau(N,N,0)
    copier_tableau(Matrice,t)
    if position_valide(t,i,j):
        for dir in range(8):
            nb_return= tester_position(t,i,j,dir)
            if nb_return >0:
                retourner_pions(t,i,j, dir,nb_return)
        t[i][j]=joueur
        joueur=-joueur
        copier_tableau(t,Matrice)
        return 0
    return None

initialiser() # A remove des que le bouton renit est fait




                
        
            
    

            
        
        
        



                  
    
        
    


    

from tableaux import *
# Ps : sens trigo dans ordre croissant
N=8
di=[0,-1,-1,-1,0,1,1,1]
dj=[1,1,0,-1,-1,-1,0,1]
joueur=0 # Joueur blanc: 0 | Joueur noir: 1
Matrice=creer_tableau(N,N,-1)

def initialiser():
    Matrice[N//2][N//2]=0
    Matrice[N//2 +1][N//2 +1]=0
    Matrice[N//2 +1][N//2]=1
    Matrice[N//2][N//2 +1]=1
    
def afficher_ligne(n):
    while n>0:
        print(' - ',end='')
        n-=1
    print('')


def afficher_plateau(t,N):
    Cpt=1
    for i in range(len(t)):
        print(Cpt,end='')
        for j in range( len(t[i])):
            if t[i][j] == -1:
                print('| ',end='')
            else :
                print('|' + str(t[i][j]),end='')
        print('|',end='')
        Cpt+=1
        print('')
        
        afficher_ligne(N)

def score(t,N):
    if joueur == 0:
        return nb_occurences_tableau(t,0)
    return nb_occurences_tableau(t,1)

def tester_position(t,i,j,dir):
    if t[i][j] == -1:
        return recherche_direction(t,i,j,dir)
    afficher_plateau(Matrice,N)
    print("here")
    

def recherche_direction(t,i,j,dir):
    n=1
    while i+(n*di[dir])< N and i+(n*di[dir])>-1 and j+(n*dj[dir])>-1 and j+(n*dj[dir])< N:
            if t[i+(n*di[dir])][j+(n*dj[dir])] == -1:
                return 0
            elif t[i+(n*di[dir])][j+(n*dj[dir])] == joueur :
                return (n-1)
            n+=1
    return 0
    
def position_valide(t,i,j):
    dir=0
    while dir<7: # Test dans toutes les directions
        if tester_position(t,i,j,dir)>0:
            return True
        dir+=1
    return False

def peut_jouer(t,joueur):
    i=0
    j=0
    while i<N:
        while j<N:
            if position_valide(t,i,j,joueur):
                return True
            j+=1
        i+=1
        j=0
    return False

def retourner_pions(Matrice,i,j,dir,n):
    global joueur
    t=[]
    while n>0:
        Matrice[i][j]=-joueur+1
        t+=[(i,j)]
        n-=1
    return t
        
def jouer(Matrice,i,j): #Va renvoyer une liste des pions a retourner en plus de changer la Matrice
    global joueur
    if position_valide(Matrice,i,j):
        t=[]
        if joueur==1:
            Matrice[i][j]=1
        else:
            Matrice[i][j]=0
        for dir in range(8):
            nb_return= recherche_direction(Matrice,i,j,dir)
            if nb_return >0:
                t+=retourner_pions(Matrice,i,j,dir,nb_return)
        joueur=-joueur + 1
        return t
    return None

initialiser()


    


                
        
            
    

            
        
        
        



                  
    
        
    


    

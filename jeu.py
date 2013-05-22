from tableaux import *
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
            if t[i][j] == 0:
                print('| ',end='')
            else :
                print('|' + str(t[i][j]),end='')
        print('|',end='')
        Cpt+=1
        print('')
        
        afficher_ligne(N)

def score(t,N):
    if joueur == -1:
        return nb_occurences_tableau(t,-1)
    return nb_occurences_tableau(t,1)

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




                
        
            
    

            
        
        
        



                  
    
        
    


    

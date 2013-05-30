import sys
def afficher_ligne(n):
    for i in range(n):
        sys.stdout.write("---")

def afficher_plateau(t):
    n = len(t)
    afficher_ligne(n)
    print(" ")
    for i in range(n):
        for j in range(n):
            if t[i][j] == 0:
                sys.stdout.write("  ")
            elif t[i][j] == -1:
                sys.stdout.write("-1")
            else:
                sys.stdout.write(" 1")
            sys.stdout.write('|')
        print("")
        afficher_ligne(n)
        print('')

def creer_tableau(h, l, val):
    t = [None]*h 
    for i in range(h):
        t[i] = [val]*l
    return t

def copier_tableau(t1,t2):
    for i in range(0,len(t1)):
        for j in range(0,len(t1[i])):
            t2[i][j]=t1[i][j]
                           
def initialiser_tableau(t,val):
    for i in range(len(t)):
        for j in range(len(t[i])):
            t[i][j]=val

def afficher_tableau(t):
    for i in range(len(t)):
        print(t[i],end='\n')

def nb_occurences_tableau(t,val):
    cpt = 0
    for j in range(len(t)):
        for i in range(len(t[j])):
            if t[j][i] == val:
                cpt += 1
    return cpt

def indice_occurence(t,tupl): #renvoie l'indice de la premiere occurence de tupl dans t
    for i in range(len(t)):
        if t[i]==tupl:
            return i
    




if __name__ == "__main__":
    t = creer_tableau(4,4,2)
    print("création d'un tableau t de 4 par 4 initialisé à deux")
    afficher_tableau(t)
    s = creer_tableau(4,4,0)
    print("création d'un tableau s de 4 par 4 initialisé à 0")    
    print("affichage avec fonction afficher_plateau")
    afficher_plateau(s)
    print("On recopie t dans s")
    copier_tableau(t,s)
    afficher_tableau(s)
    print("on initialise s à 1")
    initialiser_tableau(s, 1)
    afficher_plateau(s)
    print("nombre de 1 dans s: " + str(nb_occurences_tableau(s, 1))\
          + " nombre de 0 dans s: " + str(nb_occurences_tableau(s,0)))





































































































































































































































































































































































































































































































    

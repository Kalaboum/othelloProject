def afficher_ligne():
    for i in range(Dim):
        sys.stdout.write("---")

def afficher_plateau(t):
    afficher_ligne()
    print(" ")
    for i in range(get_Dim()):
        for j in range(get_Dim()):
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












































































































































































































































































































































































































































































































    

def recopie_et_numerote_les_lignes(nom_fichier_entree,nom_fichier_sortie):
    fichier=open(nom_fichier_entree,"r") 
    fichier_d=open(nom_fichier_sortie,"w") 
    chaine=fichier.readline() 
    cpt=0
    while len(chaine) != 0 or chaine[0]:
        print(str(cpt)+' '+ chaine,file=fichier_d,end='')
        chaine=fichier.readline()
        cpt+=1
    fichier.close()

# Pour création du fichier, creer_fichier_jeu prend en parametre (N,jouer,tableau ( qui contient les matrices a chaque tour, le dernier element etant celui du dernier coup joué),nom du fichier de sauvegarde)

def creer_fichier_jeu(N, joueur_actuel, t_sauvegarde, nom_fichier):
    fichier_destination=open(nom_fichier,"w") #On charge/cree le fichier de destination
    chaine="{0}~{1}~{2}".format(N, joueur_actuel,t_sauvegarde) # On formate ce qu'il nous faut
    print(chaine,file=fichier_destination,end="~") # On met ce qu'il  nous faut dans le fichier
    fichier_destination.flush()

def lire_fichier_jeu(nom_fichier):
    global N, joueur_actuel, Matrice, tableau_sauvegarde
    fichier_a_charger=open(nom_fichier,"r") 
    for ligne in fichier_a_charger.readlines():
        variable_a_modif= (str(ligne).rstrip('\n').split("~")) 
        # On retourne un tableau contenant en 
        #indice 0 : la racine du nombre de cases 
        #indice 1 : le joueur_actuel
        #indice 2 : Un tableau de sauvegarde contenant mes matrices d'état de jeu 
        #(tableau de matrice)
    N= variable_a_modif[0]
    joueur_actuel= variable_a_modif[1]
    tableau_sauvegarge= variable_a_modif[2]
    Matrice= variable_a_modif[2][-1]
    




        
        


    

        


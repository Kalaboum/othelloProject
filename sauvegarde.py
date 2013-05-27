from jeu import *

#Certains com sont pour voir des truc a changer eventuellement

# J'ai fait un test avec les getters et setters, quand on a une fenêtre lancée
# sauvegarder_sous marche et ouvrir aussi. Il reste le problème de sauvegarder
# qui a une erreur type string has not readline attribut. Et un problème index
# out of range quand on charge une sauvegarde qui n'a pas été effectuée sur la
# même fenêtre. Je commit en attendant et je regarde si je peux avoir une version
# plus stable

mon_fichier= None # Nom du fichier qui a été import ou deja sauvegarder durant
# la partie (permet une option sauv. et sauv sous ..)

def set_mon_fichier(string):
    global mon_fichier
    mon_fichier= string

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

# Pour création du fichier, creer_fichier_jeu prend en parametre (N,jouer,tableau ( qui contient les matrices a chaque tour,
#le dernier element etant celui du dernier coup joué),nom du fichier de sauvegarde)

def delete(string): #Il existe sans doute mieux, mais j'ai ça en attendant
    for i in string:
        i.replace("i",'')

#classe de nom_fichier : string

def creer_fichier_jeu(_Dim_, _joueur_actif_, _tableau_sauvegarde_, nom_fichier): # Correspond a sauvegarder sous
    fichier_destination=open(nom_fichier,"w") #On charge/cree le fichier de destination
    chaine="{0}~{1}~{2}".format(_Dim_,_joueur_actif_,_tableau_sauvegarde_) # On formate ce qu'il nous faut
    print(chaine,file=fichier_destination,end="~") # On met ce qu'il  nous faut dans le fichier
    fichier_destination.flush()

def edit_fichier_jeu(_Dim_,_joueur_acti_f,_tableau_sauvegarde_, nom_fichier): # Difficile de faire mieux avec notre formatage de sauvegarde
    if mon_fichier != None: #Si on sauvegarde sur la partie, seul le joueur_actif et la matrice de sauvegarde sont a changer
        fichier_destination=open(mon_fichier,"w") #On charge/cree le fichier de destination
        for ligne in mon_fichier.readlines():
            delete(ligne)
        chaine="{0}~{1}~{2}".format(_Dim_, _joueur_actif_,_tableau_sauvegarde_) # On formate ce qu'il nous faut
        print(chaine,file=fichier_destination,end="~") # On met ce qu'il  nous faut dans le fichier
        fichier_destination.flush()
    else:
        return mon_fichier # return None, mais plus secure
    
def lire_fichier_jeu(nom_fichier):
    fichier_a_charger=open(nom_fichier,"r") 
    for ligne in fichier_a_charger.readlines():
        variable_a_modif= (str(ligne).rstrip('\n').split("~")) 
        # On retourne un tableau contenant en 
        #indice 0 : la racine du nombre de cases 
        #indice 1 : le joueur_actif
        #indice 2 : Un tableau de sauvegarde contenant mes matrices d'état de jeu 
        #(tableau de matrice)
    set_Dim(eval(variable_a_modif[0]))
    set_joueur_actif(eval(variable_a_modif[1]))
    set_tableau_sauvegarde(eval(variable_a_modif[2]))
    set_Matrice(get_element_tableau_sauvegarde(-1)) #indice négatif: problème ?
    fichier_a_charger.flush()
        
        


    

        


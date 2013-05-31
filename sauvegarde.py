from jeu import *
from subprocess import call

# from subprocess import call permet d'executer une commande de terminal
# c'est relativement pratique, notamment ici pour afficher l'aide.

mon_fichier= None # Nom du fichier qui a été import ou deja sauvegarder durant
# la partie (permet une option sauv. et sauv sous ..)

def set_mon_fichier(string):
    global mon_fichier
    mon_fichier= string

def get_mon_fichier():
    return mon_fichier

# Pour création du fichier, creer_fichier_jeu prend en parametre (N,jouer,tableau
#( qui contient les matrices a chaque tour,le dernier element etant celui du dernier coup joué)
#,nom du fichier de sauvegarde)

def delete(string): #Delete le contenu du fichier, pour reinscrire par dessus.
    for i in string:
        i.replace("i",'')

#classe de nom_fichier : string

def creer_fichier_jeu(_Dim_, _joueur_actif_, _tableau_sauvegarde_, nom_fichier):
     # Correspond a sauvegarder sous
    set_mon_fichier(nom_fichier) #On change mon_fichier, pour n'avoir a cliquer que sur sauvegarder.
    fichier_destination=open(nom_fichier,"w") #On charge/cree le fichier de destination
    chaine="{0}~{1}~{2}".format(_Dim_,_joueur_actif_,_tableau_sauvegarde_) # On formate ce qu'il nous faut
    #On aura donc Dim~joueur_actif~tableau_sauvegarde~
    print(chaine,file=fichier_destination,end="~") # On met ce qu'il  nous faut dans le fichier
    fichier_destination.flush() # On ferme

def edit_fichier_jeu(_Dim_,_joueur_actif_,_tableau_sauvegarde_, nom_fichier): 
    if get_mon_fichier() != None: #Si on sauvegarde sur la partie, seul le joueur_actif et la matrice de sauvegarde sont a changer
        fichier_destination=open(mon_fichier,"w") #On charge/cree le fichier de destination
        chaine="{0}~{1}~{2}".format(_Dim_, _joueur_actif_,_tableau_sauvegarde_) # On formate ce qu'il nous faut
        print(chaine,file=fichier_destination,end="~") # On met ce qu'il  nous faut dans le fichier
        fichier_destination.flush()
    else:
        return mon_fichier # return None, mais plus secure
    
def lire_fichier_jeu(nom_fichier):
    set_mon_fichier(nom_fichier)
    fichier_a_charger=open(nom_fichier,"r") 
    for ligne in fichier_a_charger.readlines(): #Permet de lire notre fichier de sauvegarde
        variable_a_modif= (str(ligne).rstrip('\n').split("~")) #Split permet de crée un tableau a partir de string
        # On retourne un tableau contenant en 
        #indice 0 : la racine du nombre de cases 
        #indice 1 : le joueur_actif
        #indice 2 : Un tableau de sauvegarde contenant mes matrices d'état de jeu 
        #(tableau de matrice)
    set_Dim(eval(variable_a_modif[0]))
    set_joueur_actif(eval(variable_a_modif[1])) 
    set_tableau_sauvegarde(eval(variable_a_modif[2])) 
    set_Matrice(get_element_tableau_sauvegarde(-1))
    #On met ce qu'il faut dans chaque variable. eval permet de changer la classe
    #du contenu de varaible_a_modif, qui sont avant l'appel de eval, de classe string.
    fichier_a_charger.flush()

def afficher_aide():
    call(["kdialog","--textbox","Help.text"])
    #On execute une commande shell via python, on utilise kdialog pour ouvrir
    #l'aide.
        
    
        


    

        


# -*- coding:utf-8 -*-

#LES IMPORT DE MODULES:##############################################################

#Permet l'affichage de la fenetre de fin de partie
from tkinter.messagebox import showinfo
from tkinter import *
from sauvegarde import *
#Permet l'ouverture des fenetres de dialogues
from tkinter.filedialog import *

#LES FENETRES: ########################################################################

#Fenetre principale
fen = Tk()
#Fenetre de selection du mode de jeu en debut de partie
fenetre=Toplevel()

#LES LABELS:##########################################################################

#Affiche la position du curseur, via l'indice de la case sous le curseur
Position= Label(fen,font='ChintzyCPUBRK')

#Affiche le score et le joueur_actuel.
Score= Label(fen,text=" Blanc : 2 | Noir : 2 , Joueur : Noir",relief="groove",font='ChintzyCPUBRK',height=2)

# LES VARIABLES GLOBALES : ##########################################################

TAILLE_CASE=400//Dim #Taille des cases 
r=25 # Rayon des pions
DELTA=3 # Marge pions cases pour aspect visuel
DB = 60 # Décalage lié a la bordure style "bois"
tableau_surbrillance=[None,None]

#FONCTION DE LANCEMENT DU JEU :########################################################

def lancer_le_jeu():
    global fen
    fen.mainloop()

#FONCTIONS DE DESSIN : #############################################################

#Dans notre version d'Othello, la taille de l'image de fond est fixe (zone de dessin de
#400*400, on peut cependant changer le nombre de cases.

#Cette fonction va crée les pions sur le canevas, l'expression est un peu dense,
#cela du au decalage lié a l'image de fond, et a la presence de delta, pour qu'il y ait
#un décalage visible entre les lignes et les pions.
def creer_pion(i,j,couleur,outline):
    return fond.create_oval((j*TAILLE_CASE+DELTA)+ DB,(i*TAILLE_CASE+DELTA)+ DB,
                     ((j+1)*TAILLE_CASE-1 - DELTA)+ DB,((i+1)*TAILLE_CASE-1 -DELTA)+ DB,
                     fill=couleur,outline=outline,width=DELTA-1)

#On donne en parametre a cette fonction le décalage lié a l'image de fond,
#On trace simplement les lignes a un intervalle lié a la taille des cases,
#dans la zone voulu.
def creation_grille(param):
    while param <= DB + (Dim * TAILLE_CASE):
        fond.create_line(param,DB,param,(Dim*TAILLE_CASE)+DB,fill='white',width=DELTA)
        param+=TAILLE_CASE
    param=DB
    while param <= DB+(Dim*TAILLE_CASE):
        fond.create_line(DB,param,(Dim*TAILLE_CASE)+DB,param,fill='white',width=DELTA)
        param+=TAILLE_CASE

#LES DIVERSES FONCTIONS D'ACTUALISATION : ##########################################

#La fonction actualiser nous permet de synchroniser la partie algorithmique avec
#l'interface après chaque coup, changeant les informations visibles a l'écran.
def actualiser():
    Copie=get_Matrice() # On stock get_matrice()
    #Si aucun des deux joueurs ne peut jouer, la partie est fini
    if peut_jouer(Copie,get_joueur_actif()) or peut_jouer(Copie,-get_joueur_actif()):
    #On parcours toute la matrice, et on synchonise avec la partie interface en posant
    #les pions sur le canevas
        for i in range(Dim):
            for j in range(Dim):
                if Copie[i][j]==-1:
                    creer_pion(i,j,"white","#3C3C3C")
                elif Copie[i][j]==1:
                    creer_pion(i,j,"black","#3C3C3C")
                #On met a jour le label score (affiche score + joueur_actif)
                score_actuel=score(Copie)
                if get_joueur_actif()==-1:
                    Score.config(text=" Blanc : " + str(score_actuel[0])+" | Noir : "
                                 + str(score_actuel[1]) + " , Joueur : Blanc")
                else :
                    Score.config(text=" Blanc : " + str(score_actuel[0])+" | Noir : "
                                 + str(score_actuel[1]) + " , Joueur : Noir")
    else:
            showinfo('Fin de partie','Le joueur avec les pions '+str(joueur_victorieux( get_Matrice() ))+' remporte la victoire !')
            #showinfo possible grace a l'import de filedialog.
                    
def actualiser_plus(): #Fonction necessaire au bouton reinitialiser
    set_joueur_actif(1)
    img=fond.create_image(largeur/2,hauteur/2,image=photo) #On replace l'image de fond.
    creation_grille(DB)                                 
    actualiser()

#Cette fonctions nous permet de réactualiser la surbrillance et des informations liées a
#la position du curseur.
def mouvement(event):
    global tableau_surbrillance, fond
    #On recupere l'indice des cases sous le curseur pour le joueur.
    j=(event.x - DB )//TAILLE_CASE
    i=(event.y - DB )//TAILLE_CASE
    #On rentre si la position est dans la zone de jeu du joueur.
    if 0<=i<=Dim-1 and 0<=j<=Dim-1:
        #On réactualise si la position sur les cases a changer depuis le dernier appel
        if (i,j) != (tableau_surbrillance[0]):
            #On detruit la zone de surbrillance (un pion) car la position a changer sur la grille pour
            #la partie algorithmique du jeu.
            fond.delete(tableau_surbrillance[1])
            tableau_surbrillance[0]=None
            #On actualise la position qui est affichée a l'écran.
            Position.configure(text="X : "+ str(j) + " - Y : " + str(i),font='ChintzyCPUBRK')
            #Si la position est valide, on pose un pion montrant que la position est affectivement valide
            #pour le joueur_actuel.
            if position_valide(get_Matrice(),i,j,get_joueur_actif()) and (tableau_surbrillance[0]) != (i,j):
                if get_typejoueur(get_joueur_actif())=="Humain":
                    surbrillance=creer_pion(i,j,"#85C692","#85C692")
                tableau_surbrillance=[(i,j),surbrillance]
    else:
        Position.configure(text="Vous etes hors zone de jeu.")

#Permet de reinitialiser une partie : on remet tout les paramètres a leurs valeurs initiales et on actualise.
def renitialiser():
    global Matrice ,joueur_actif
    set_joueur_actif(1)
    img=fond.create_image(largeur/2,hauteur/2,image=photo)
    creation_grille(DB)
    #On appelle des fonctions du module plateau pour la partie algorithmique.
    initialiser_tableau(Matrice,0)
    initialiser_Matrice()
    set_tableau_sauvegarde([get_Matrice()])
    #On applique les changements a l'aspect visuel du jeu.
    actualiser()

#FONCTION DE CLIC:#######################################################################

#On recupere la position du curseur, et on la fait correspondre aux indices i et j
#Si la position est sur la grille de jeu, on appelle la fonction jouer_coup
def clique_gauche(event):
    j=(event.x - DB )//TAILLE_CASE
    i=(event.y - DB )//TAILLE_CASE
    if 0<=i<=Dim-1 and 0<=j<=Dim-1 and Humain_peut_jouer:
        #Si la position est n'est pas valide, on remet Humain_peut_jouer a True
        set_Humain_peut_jouer(False)
        jouer_coup(Matrice,i,j)

#Si la position est valide, on modifie notre tableau de sauvegarde et on actualise
def jouer_coup(t,i,j):
    global Matrice
    joueur= get_joueur_actif()
    test=jouer(i,j, joueur)
    if  test == None:
        return
    ajouter_tableau_sauvegarde(Matrice)
    attendre_tour_humain(t,joueur)
    actualiser()

#FONCTIONS DE LIEN AVEC LE MODULE SAUVEGARDE:#############################################

def chargement_de_partie():# Au moment ou l'on charge, le jeu attend qu'un joueur joue
    nom_fichier=askopenfilename() #Ouverture de la fenetre de dialogue
    lire_fichier_jeu(nom_fichier)       
    actualiser_plus() #On actualise tout                      
    
def sauvegarde_de_partie_sous():
    nom_fichier=asksaveasfilename() #Ouverture de la fenetre de dialogue, pour la sauvegarde ici
    if mon_fichier != ():
        creer_fichier_jeu(get_Dim(),get_joueur_actif(),get_tableau_sauvegarde(),nom_fichier)
    
    
#Si on a deja ouvert ou lu un fichier sauvegarde dans la partie, il n'est plus necessaire
#d'ouvrir la fenetre de dialogue : la variable nom_fichier contient le nom du fichier
#en question au lieu de None
def sauvegarde_de_partie(nom_fichier):
    test=edit_fichier_jeu(get_Dim(),get_joueur_actif(),get_tableau_sauvegarde(), nom_fichier)
    if test == None:
        sauvegarde_de_partie_sous()

#LE UNDO: ################################################################################

def undo_interface():
        n_coup_avant()
        actualiser_plus()

#CHOIX DE LA DIFFICULTE ET MODE DE JEU:####################################################

#On joue desormais face a l'IA
def mode_IA():
    set_typejoueur(-1,"IAMaximiser")
    fenetre.destroy()
    
#On joue desormais face a un humain
def mode_1v1():
    set_typejoueur(-1,"Humain")
    fenetre.destroy()

#Cette fonction permet l'affichage de la fenetre de selection du mode de jeu a l'ouverture du jeu
def selection_parametres():
    fenetre.focus_set() # On passe le focus a notre nouvelle fenetre
    fenetre.title("Initialisation")
    texte=Label(fenetre,text="Mode de jeu : ",font='ChintzyCPUBRK')
    HumvHum =Button(fenetre,text= "Joueur vs Joueur",font='ChintzyCPUBRK',command=mode_1v1,width=15,height=2)
    IAvs1=Button(fenetre,text= "Joueur vs IA",font='ChintzyCPUBRK',command=mode_IA,width=15,height=2)
    texte.pack(side=TOP)
    IAvs1.pack()
    HumvHum.pack()
    texte.pack(side=TOP)

selection_parametres() #On appelle le contenu de la fenetre

#PARAMETRAGE DU CANEVAS####################################################################

#On lance le jeu via le shell, pour des problemes de chemins absolus/relatifs
photo=PhotoImage(file="grille.gif") # Ouverture de l'image de fond

largeur=photo.width() # Détermination de la largeur de l'image

hauteur=photo.height() # Détermination de la hauteur de l'image

fen.title("Othello Project - HOFER - DELMAS") # Titre de la fenêtre

fond=Canvas(fen,bg="white",width=largeur,height=hauteur) # définition du canvas qui va accueillir l'image

fond.pack() # placement du canvas

img=fond.create_image(largeur/2,hauteur/2,image=photo) # Positionnement de l'image à partir de son centre

renitialiser() #On met en place l'interface graphique du jeu

#LES BOUTONS ET LABELS:#####################################################################

bouton_undo=Button(fen,text="Undo",command=undo_interface,font='ChintzyCPUBRK',cursor="dotbox",height=3,relief="groove")
bouton_undo.pack(side=RIGHT)

bouton_renitialiser= Button(fen, text='Reinitialiser', command=renitialiser, font="ChintzyCPUBRK",height=3,cursor="dotbox",relief="groove")
bouton_renitialiser.pack(side=LEFT)

#LE MENU:###################################################################################

menubar = Menu(fen,font='ChintzyCPUBRK') #Pris dans l'exemple du cour
fen.config(menu=menubar)

filemenu = Menu(menubar)
menubar.add_cascade(label="Fichier", menu=filemenu) 
filemenu.add_command(label="Ouvrir...", command=lambda:chargement_de_partie())
filemenu.add_separator()
filemenu.add_command(label="Sauvegarder", command=lambda:sauvegarde_de_partie(get_mon_fichier()))
filemenu.add_separator()
filemenu.add_command(label="Sauvegarder sous ...", command=lambda:sauvegarde_de_partie_sous())
filemenu.add_separator()
filemenu.add_command(label="Quitter", command=fen.destroy)

optionmenu= Menu(menubar)
menubar.add_cascade(label="Option", menu=optionmenu)
optionmenu.add_command(label="Changer mode de jeu", command=lambda:changement_mode_de_jeu())
optionmenu.add_separator()
optionmenu.add_command(label="Niveau IA +", command=lambda:niveau_IA(1))
optionmenu.add_separator()
optionmenu.add_command(label="Niveau IA -", command=lambda:niveau_IA(-1))

helpmenu= Menu(menubar)
menubar.add_cascade(label="Aide", menu=helpmenu)
helpmenu.add_command(label='Aide',command=lambda:afficher_aide())

#LES CALLBACKS : ##########################################################################

#Lie une interaction du joueur a une action
fond.bind("<Button-1>",clique_gauche )
fond.bind("<Motion>", mouvement)

Position.pack()
Score.pack()
fond.pack()

#TEST:########################################################################################

if __name__ == "__main__":
    renitialiser()
    print("Affichage du jeu")
    creer_pion(0,0,"red","white")
    print("Affichage d'un pion rouge")
    print("Actualisation de la zone de surbrillance")
    fen.mainloop()
     


# -*- coding:utf-8 -*-
#V2 !

from tkinter.messagebox import showinfo
from tkinter import *
from sauvegarde import *
from tkinter.filedialog import *


#Les widgets:
fen = Tk()
Position= Label(fen,font='ChintzyCPUBRK')
Score= Label(fen,text=" Blanc : 2 | Noir : 2 , Joueur : Noir",relief="groove",font='ChintzyCPUBRK',height=2)

#Variables globales + Matrice du tableau:

TAILLE_CASE=400//Dim #Taille des cases 
r=25 # Rayon des pions
DELTA=3 # Marge pions cases pour aspect visuel
DB = 60 # Décalage lié a la bordure style "bois"
tableau_surbrillance=[None,None]

#Fonctions de l'interface graphique
def lancer_le_jeu():
    global fen
    fen.mainloop()

def actualiser_plus():
    set_joueur_actif(1)
    img=fond.create_image(largeur/2,hauteur/2,image=photo)
    creation_grille(DB)
    actualiser()

def n_coup_avant(): 
    joueur = get_joueur_actif()
    if get_typejoueur(joueur) == get_typejoueur(-joueur): #Cas de Humain vs Humain
        undo(1)
        if dernier_joueur() != joueur:
            set_joueur_actif(-joueur)
    else:
        n = coup_dernier_joueur_humain()
        undo(n)
    actualiser_plus()
        
def actualiser():
    Copie=get_Matrice()
    if peut_jouer(Copie,get_joueur_actif()) or peut_jouer(Copie,-get_joueur_actif()):
        for i in range(Dim):
            for j in range(Dim):
                if Copie[i][j]==-1:
                    creer_pion(i,j,"white","#3C3C3C")
                elif Copie[i][j]==1:
                    creer_pion(i,j,"black","#3C3C3C")
                score_actuel=score(Copie)
                if get_joueur_actif()==-1:
                    Score.config(text=" Blanc : " + str(score_actuel[0])+" | Noir : "
                                 + str(score_actuel[1]) + " , Joueur : Blanc")
                else :
                    Score.config(text=" Blanc : " + str(score_actuel[0])+" | Noir : "
                                 + str(score_actuel[1]) + " , Joueur : Noir")
    else:
        showinfo('Fin de partie','Le joueur avec les pions '+str(joueur_victorieux( get_Matrice() ))+' remporte la victoire !')

def clique_gauche(event):
    j=(event.x - DB )//TAILLE_CASE
    i=(event.y - DB )//TAILLE_CASE
    if 0<=i<=Dim-1 and 0<=j<=Dim-1 and Humain_peut_jouer:
        set_Humain_peut_jouer(False)
        jouer_coup(Matrice,i,j)
    
def creer_pion(i,j,couleur,outline):
    return fond.create_oval((j*TAILLE_CASE+DELTA)+ DB,(i*TAILLE_CASE+DELTA)+ DB,
                     ((j+1)*TAILLE_CASE -1 - DELTA)+ DB,((i+1)*TAILLE_CASE -1 -DELTA)+ DB,
                     fill=couleur,outline=outline,width=DELTA-1)

def mouvement(event):
    global tableau_surbrillance, fond
    j=(event.x - DB )//TAILLE_CASE
    i=(event.y - DB )//TAILLE_CASE
    if 0<=i<=Dim-1 and 0<=j<=Dim-1:
        if (i,j) != (tableau_surbrillance[0]):
            fond.delete(tableau_surbrillance[1])
            tableau_surbrillance[0]=None
            Position.configure(text="X : "+ str(j) + " - Y : " + str(i),font='ChintzyCPUBRK')
            if position_valide(get_Matrice(),i,j,get_joueur_actif()) and (tableau_surbrillance[0]) != (i,j):
                if get_typejoueur(get_joueur_actif())=="Humain":
                    surbrillance=creer_pion(i,j,"#85C692","#85C692")
                tableau_surbrillance=[(i,j),surbrillance]
    else:
        Position.configure(text="Vous etes hors zone de jeu.")


def creation_grille(param):
    while param <= DB + (get_Dim() * TAILLE_CASE):
        fond.create_line(param,DB,param,(Dim*TAILLE_CASE)+DB,fill='white',width=DELTA)
        param+=TAILLE_CASE
    param=DB
    while param <= DB+(get_Dim()*TAILLE_CASE):
        fond.create_line(DB,param,(Dim*TAILLE_CASE)+DB,param,fill='white',width=DELTA)
        param+=TAILLE_CASE

# fonction liée au module sauvegarde:

def chargement_de_partie():# Au moment ou l'on charge, le jeu attend qu'un joueur joue : peut etre faire
    nom_fichier=askopenfilename()
    lire_fichier_jeu(nom_fichier)       # attention a l'IA, je te laisse voir ça, dit moi si j'ai des choses a edit
    actualiser_plus()                       #Mais normalement c'est bon, car le joueur ne peut agir que si c'est a lui de jouer ;)
    
def sauvegarde_de_partie_sous():
    nom_fichier=asksaveasfilename()
    if mon_fichier != ():
        creer_fichier_jeu(get_Dim(),get_joueur_actif(),get_tableau_sauvegarde(),nom_fichier)
    print(mon_fichier)
    
    
def sauvegarde_de_partie(nom_fichier):
    test=edit_fichier_jeu(get_Dim(),get_joueur_actif(),get_tableau_sauvegarde(), nom_fichier)
    if test == None:
        sauvegarde_de_partie_sous()
    
def jouer_coup(t,i,j):
    global Matrice
    joueur= get_joueur_actif()
    test=jouer(i,j, joueur)
    if  test == None:
        return
    ajouter_tableau_sauvegarde(Matrice)
    attendre_tour_humain(t,joueur)
    actualiser()

#Choix du mode :

def mode_IA():
    set_typejoueur(-1,"IAMaximiser")
    fenetre.destroy()
    
def mode_1v1():
    set_typejoueur(-1,"Humain")
    fenetre.destroy()
    
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
    
#Mes Canvas + Fonction d'initialisation

def renitialiser():
    global Matrice ,joueur_actif
    set_joueur_actif(1)
    img=fond.create_image(largeur/2,hauteur/2,image=photo)
    creation_grille(DB)
    initialiser_tableau(Matrice,0)
    initialiser_Matrice()
    set_tableau_sauvegarde([get_Matrice()])
    actualiser()
    
photo=PhotoImage(file="grille.gif") # Ouverture de l'image de fond
largeur=photo.width() # Détermination de la largeur de l'image
hauteur=photo.height() # Détermination de la hauteur de l'image
fen.title("Othello Project - HOFER - DELMAS") # Titre de la fenêtre
fond=Canvas(fen,bg="white",width=largeur,height=hauteur) # définition du canvas qui va accueillir l'image
fond.pack() # placement du canvas
img=fond.create_image(largeur/2,hauteur/2,image=photo) # Positionnement de l'image à 
                                                       #partir de son centre
renitialiser()

#Mes Boutons:
bouton_undo=Button(fen,text="Undo",command=n_coup_avant,font='ChintzyCPUBRK',cursor="dotbox",height=3,relief="groove")
bouton_undo.pack(side=RIGHT)

bouton_renitialiser= Button(fen, text='Reinitialiser', command=renitialiser, font="ChintzyCPUBRK",height=3,cursor="dotbox",relief="groove")
bouton_renitialiser.pack(side=LEFT)

#Le Menu

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




#Mes Callbacks :

fond.bind("<Button-1>",clique_gauche )
fond.bind("<Motion>", mouvement)

Position.pack()
Score.pack()

fond.pack()

fenetre=Toplevel()
selection_parametres()

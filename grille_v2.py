# -*- coding:utf-8 -*-
#V2 !

from tkinter import *
from jeu import *
afficher_plateau(Matrice,N)

fen = Tk()
info= Label(fen)

#Variables globales + Matrice du tableau:

TAILLE_CASE=50 #Taille des cases
r=25 # Rayon des pions
DELTA=3 # Marge pions cases pour aspect visuel
DB = 60 # Décalage lié a la bordure style "bois"

#Foncions de l'interface graphique + manipulation naïve de la matrice:

def actualiser():
    for i in range(N):
        for j in range(N):
            if Matrice[i][j]==-1:
                creer_pion(i,j,"white","black")
            elif Matrice[i][j]==1:
                creer_pion(i,j,"black","white")
        
def clique_gauche(event):
    j=(event.x - DB )//TAILLE_CASE
    i=(event.y - DB )//TAILLE_CASE
    if 0<=i<=7 and 0<=j<=7:
        jouer_coup(Matrice,i,j)
    
def creer_pion(i,j,couleur,outline):
    fond.create_oval((j*TAILLE_CASE+DELTA)+ DB,(i*TAILLE_CASE+DELTA)+ DB,((j+1)*TAILLE_CASE -1 - DELTA)+ DB,((i+1)*TAILLE_CASE -1 -DELTA)+ DB,fill=couleur,outline=outline,width=DELTA-1)

def mouvement(event):
    x=event.x
    y=event.y
    info.configure(text="X : "+ str((x - DB)//TAILLE_CASE) + " - Y : " + str((y -DB)//TAILLE_CASE),font='arialblack')

def creation_grille(param):
    while param <= DB +(N*TAILLE_CASE):
        fond.create_line(param,DB,param,(N*TAILLE_CASE)+DB,fill='white',width=DELTA)
        param+=TAILLE_CASE
    param=DB
    while param <= DB+(N*TAILLE_CASE):
        fond.create_line(DB,param,(N*TAILLE_CASE)+DB,param,fill='white',width=DELTA)
        param+=TAILLE_CASE

def jouer_coup(t,i,j):
    global Matrice
    test=jouer(i,j)
    if  test.__class__.__name__ == "NoneType":
        return 
    afficher_plateau(Matrice,N)
    actualiser()

#Mes Canvas + Fonction d'initialisation

def renitialiser():
    global Matrice
    img=fond.create_image(largeur/2,hauteur/2,image=photo)
    creation_grille(DB)
    initialiser_tableau(Matrice,0)
    initialiser_Matrice()
    actualiser()
    
photo=PhotoImage(file="grille.gif") # Ouverture de l'image
largeur=photo.width() # Détermination de la largeur de l'image
hauteur=photo.height() # Détermination de la hauteur de l'image
fen.geometry(str(largeur+2)+"x"+str(hauteur+2)) # Redimensionnement de la fenêtre à partir de la taille de l'image
fen.title("Othello Project - HOFER - DELMAS") # Titre de la fenêtre
fond=Canvas(fen,bg="white",width=largeur,height=hauteur) # définition du canvas qui va accueillir l'image
fond.pack() # placement du canvas
img=fond.create_image(largeur/2,hauteur/2,image=photo) # Positionnement de l'image à partir de son centre
renitialiser()
creation_grille(DB)

#Mes Boutons:
bouton_quitter=Button(fen,text='Quitter',command=fen.destroy, font='ChintzyCPUBRK')
bouton_quitter.pack(side=LEFT)

bouton_renitialiser= Button(fen, text='Reinitialiser', command=renitialiser, font="ChintzyCPUBRK")
bouton_renitialiser.pack(side=LEFT)
creation_grille(DB)

#Mes Callbacks :
fond.bind("<Button-1>",clique_gauche )
fond.bind("<Motion>", mouvement)

info.pack()
fond.pack()
fen.mainloop()
# -*- coding:utf-8 -*-
#V2 !

from tkinter import *
from jeu import *

fen = Tk()
info= Label(fen)

#Mes Canvas

photo=PhotoImage(file="grille.gif") # Ouverture de l'image
largeur=photo.width() # Détermination de la largeur de l'image
hauteur=photo.height() # Détermination de la hauteur de l'image
fen.geometry(str(largeur+2)+"x"+str(hauteur+2)) # Redimensionnement de la fenêtre à partir de la taille de l'image
fen.title("Othello") # Titre de la fenêtre
fond=Canvas(fen,bg="white",width=largeur,height=hauteur) # définition du canvas qui va accueillir l'image
fond.pack() # placement du canvas
img=fond.create_image(largeur/2,hauteur/2,image=photo) # Positionnement de l'image à partir de son centre


#Variables globales + Matrice du tableau:
TAILLE_CASE=50
r=25 # Rayon des pions
DELTA=3 # Marge pions cases pour aspect visuel
pion=None
DB = 60 # Décalage lié a la bordure style "bois"

#Foncions de l'interface graphique + manipulation naïve de la matrice:

def retourner(i,j):
    if joueur==0:
        creer_pion(i,j,"white","black")
        return
    creer_pion(i,j,"black","white")

def clique_gauche(event):
    global DB, joueur
    j=(event.x - DB )//TAILLE_CASE
    i=(event.y - DB )//TAILLE_CASE
    if i>=0 and i<=7 and j<=7 and j>=0:
        jouer_coup(Matrice,i,j)


def config_depart():
    creer_pion(3,3,"white","black")
    creer_pion(4,4,"white","black")
    creer_pion(3,4,"black","white")
    creer_pion(4,3,"black","white")
    
def creer_pion(i,j,couleur,outline):
    fond.create_oval((j*TAILLE_CASE+DELTA)+ DB,(i*TAILLE_CASE+DELTA)+ DB,((j+1)*TAILLE_CASE -1 - DELTA)+ DB,((i+1)*TAILLE_CASE -1 -DELTA)+ DB,fill=couleur,outline=outline,width=DELTA-1)
    if couleur=="white":
        Matrice[i][j]=0
        return
    Matrice[i][j]=1

def mouvement(event):
    global TAILLE_CASE, DB
    x=event.x
    y=event.y
    info.configure(text="X : "+ str((x - DB)//TAILLE_CASE) + " - Y : " + str((y -DB)//TAILLE_CASE),font='arialblack')

def renitialiser():
    creation_grille(60)
    config_depart()

def creation_grille(param):
    while param <= DB +(N*TAILLE_CASE):
        fond.create_line(param,DB,param,(N*TAILLE_CASE)+DB,fill='white',width=DELTA)
        param+=TAILLE_CASE
    param=DB
    while param <= DB+(N*TAILLE_CASE):
        fond.create_line(DB,param,(N*TAILLE_CASE)+DB,param,fill='white',width=DELTA)
        param+=TAILLE_CASE
    param=DB

def jouer_coup(t,i,j):
    coup_jouer=jouer(Matrice,i,j)
    if coup_jouer.__class__.__name__ == "int":
        for a_retourner in coup_jouer:
                retourner(a_retourner)
        
# def retourner_pions(t,i,j,dir,n):
#     global di
#     global dj
#     while n>0:
#         retourner(i+(n*di[dir]),j+(n*dj[dir]))
#         n-=1

#Conditions de départ du jeu
renitialiser()

#Mes Boutons:
bouton_quitter=Button(fen,text='Quitter',command=fen.destroy, font='arialblack')
bouton_quitter.pack(side=LEFT)

renitialiser= Button(fen, text='Reinitialiser', command=renitialiser, font="arialblack")
renitialiser.pack(side=LEFT)
creation_grille(DB)

#Mes Callbacks :
fond.bind("<Button-1>",clique_gauche )
fond.bind("<Motion>", mouvement)

info.pack()
fond.pack()
fen.mainloop()

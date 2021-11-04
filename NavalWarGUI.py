import tkinter as tk
from NewBattleship import Bateau
from NewBattleship import check_around_boat
from NewBattleship import place_boat
from NewBattleship import check_and_place
from NewBattleship import final
from NewBattleship import co_bateaux

def create_grid(event=None):
    w = c.winfo_width() # longueur de la fenetre
    h = c.winfo_height() # largeur de la fenetre
    c.delete('grid_line') # suprime toutes les lignes avec le tag grid_line (clean workspace)

    # Creer toutes les lignes verticales de la grille 1
    for i in range(0, 333, 33):
        c.create_line([(i, 0), (i, 333)], tag='grid_line')
    

    # Creer toutes les lignes horizontales de la grille 1
    for i in range(0, 333, 33):
        c.create_line([(0, i), (333, i)], tag='grid_line')

    # Creer toutes les lignes verticales de la grille 2
    for i in range(500, 833, 33):
        c.create_line([(i, 0), (i, 333)], tag='grid_line')
    

    # Creer toutes les lignes horizontales de la grille 2
    for i in range(500, 833, 33):
        i=i-500
        c.create_line([(500, i), (833, i)], tag='grid_line')

def create_rectangle(x0, y0, x1,y1, canvasName,color): 
    """Crée un rectangle grace aux coordonées du point tt haut gauche et tt bas droite + couleur précise"""
    return canvasName.create_rectangle(x0, y0, x1, y1,fill=color)

root = tk.Tk() #creation de la fenetre gui

c = tk.Canvas(root, height=500, width=1000, bg='LightBlue1') #taille fenetre et couleur background
c.pack(fill=tk.BOTH, expand=False) #fait apparaitre les éléments sur le gui


c.bind('<Configure>', create_grid,)

def convertisseur_grille_1(x,y): 
    """Permet de convertir un tuple (x,y) en coordonées utilisables pour create_rectangle"""
    x0=x*33
    y0=y*33
    x1=x0+33
    y1=y0+33
    return x0,y0,x1,y1

def convertisseur_grille_2(x,y):
    """Permet de convertir un tuple (x,y) en coordonées utilisables pour create_rectangle"""
    x0=x*33 +500
    y0=y*33 
    x1=x0+33 
    y1=y0+33
    return x0,y0,x1,y1


liste_bateau=co_bateaux()
liste_bateau2=co_bateaux() #cree listes bateaux

couleurs=["black","maroon","blue","blue","dark green"]

def placer_bateau_gui_1(liste_bateau):
    """Place les bateaux sur le quadrillage 1"""
    for count,i in enumerate(liste_bateau):
        for f in i:
            create_rectangle(int(convertisseur_grille_1(f[0],f[1])[0]),int(convertisseur_grille_1(f[0],f[1])[1]),int(convertisseur_grille_1(f[0],f[1])[2]),int(convertisseur_grille_1(f[0],f[1])[3]),c,couleurs[count])

def placer_bateau_gui_2(liste_bateau2):
    """Place les bateaux sur le quadrillage 2"""
    for count,i in enumerate(liste_bateau2):
        for f in i:
            create_rectangle(int(convertisseur_grille_2(f[0],f[1])[0]),int(convertisseur_grille_2(f[0],f[1])[1]),int(convertisseur_grille_2(f[0],f[1])[2]),int(convertisseur_grille_2(f[0],f[1])[3]),c,couleurs[count])


placer_bateau_gui_1(liste_bateau)
placer_bateau_gui_2(liste_bateau2)

create_rectangle(30,350,195,383,c,"black")
create_rectangle(30,390,162,423,c,"maroon")
create_rectangle(30,430,129,463,c,"blue")
create_rectangle(139,430,238,463,c,"blue")
create_rectangle(30,470,96,503,c,"dark green")

tk.Label(root,text='Porte avion',font=('compact', 15, 'normal'),bg='LightBlue1').place(x=200, y=350)
tk.Label(root,text='Croiseur',font=('compact', 15, 'normal'),bg='LightBlue1').place(x=167, y=390)
tk.Label(root,text='Sous-marins',font=('compact', 15, 'normal'),bg='LightBlue1').place(x=242, y=430)
tk.Label(root,text='Torpilleur',font=('compact', 15, 'normal'),bg='LightBlue1').place(x=100, y=470)

root.mainloop() #Lance le GUI

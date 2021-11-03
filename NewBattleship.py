from pprint import pprint               #pprint pour les tests
import random as r

grille = [[0 for _ in range(10)] for _ in range(10)]    # créé la grille
len_boats = [5,4,3,3,2]                 # différentes longueurs de bateau

class Bateau:
    """ créé un objet Bateau avec les arguments de direction, longueur, positions"""
    def __init__(self, direction:int, length:int, positions=[], alive=True) -> None:
        self.positions = positions
        self.length = length
        self.direction = direction
        self.alive = alive

    def change_pos(self):
        """ créé des nouvelles positions pour le bateau """
        self.positions = []             # clear les positions
        if self.direction == 0:         # si horizontal
            self.positions.append( (r.randint(0,10-self.length) , r.randint(0,9) ) )    # premiere position
            for i in range(1,self.length):
                self.positions.append((self.positions[0][0]+i,self.positions[0][1]))    # les suivantes
        else:                           # sinon vertical
            self.positions.append( (r.randint(0,9) , r.randint(0,10-self.length) ) )    # same
            for i in range(1,self.length):
                self.positions.append((self.positions[0][0],self.positions[0][1]+i))    # same

def check_around_boat(boat:Bateau):
    """ vérifie les alentours de la position hypothétique du bateau """
    for x in range(
            max((boat.positions[0][0]-1),0),        #anti ListIndexOutOfRange pour min x
            min((boat.positions[-1][0]+2),9)        #anti ListIndexOutOfRange pour max x
        ):
        for y in range(
                max((boat.positions[0][1]-1), 0),   #anti ListIndexOutOfRange pour min y
                min((boat.positions[-1][1]+2), 9)   #anti ListIndexOutOfRange pour max y
            ):
            if grille[y][x] == 1:                   # check si deja bateau
                return False                        # nope ya deja bateau on skip
    return True                                     # il y a la place pour le bateau

def place_boat(boat:Bateau):
    """ place le bateau sur la grille """
    for x in range((boat.positions[0][0]), (boat.positions[-1][0]+1)):
        for y in range((boat.positions[0][1]), (boat.positions[-1][1]+1)):
            grille[y][x] = 1                        # place un '1' dans la grille à chaque position du bateau

def check_and_place(boat:Bateau):
    """ place le bateau s'il y a la place """
    if check_around_boat(boat):
        place_boat(boat)
    else:
        boat.change_pos()
        check_and_place(boat)

TEAM = [Bateau(r.randint(0,1), len) for len in len_boats]   # créé la liste contenant les bateaux de différentes longueurs

for boat in TEAM:           # pour chaque bateau
    boat.change_pos()       # position initiale
    check_and_place(boat)   # cest tipar

pprint(grille)                      # LEZGOOO CA MARCHE
print([boat.positions for boat in TEAM])

from pprint import pprint
import random as r
### aure

### HELP GRID 
### 0 => EAU
### 1 => BOAT
### 2 => BOAT TOUCHÉ

bateaux = {"carrier":5, "battleship":4, "cruiser":3, "submarine":3, "destroyer":2}
dirs = ['horz','vert']

grille = [[0 for _ in range(10)] for _ in range(10)]



class Bateau():
    def __init__(self, position, dir, alive=True) -> None:
        self.position = position
        self.dir = dir
        self.alive = alive
        self.length = len(position)

    def is_alive(self):           # WIP
        for i in range(len(self.position)):
            if grille[ self.position[0+i][1] ][ self.position[0+i][0] ] == 0:
                pass # TODO => check si ttes les pos sont vivant

    def __repr__(self) -> str:
        return f"Bateau de position : {self.position[0]}, de direction : {self.dir} et de longueur : {self.length}"

def create_pos(lenght:int, position:tuple, dir:str) -> list:
    """ créé la liste de tuples qui contient les positions de chacune des parties du navire
        lenght : longueur en cases du bateau
        position : coordonnées la case la plus haute ou la plus à gauche du bateau
        dir : 'horz' ou 'vert' 
    """
    if dir == 'horz':
        if position[0]+lenght-1 > 10 :
            return 'le bateau sort de la grille'
        return [tuple([position[0]+i-1, position[1]-1]) for i in range(lenght)]
    if dir == 'vert':
        if position[1]+lenght-1 > 10 :
            return 'le bateau sort de la grille'
        return [tuple([position[0]-1, position[1]+i-1]) for i in range(lenght)]
    else:
        return "argument dir invalide"



def check_around_boat(boat:Bateau):
    """ Check les cases autour du bateau :
        True si rien
        False si deja qqchose
    """
    if boat.dir == 'vert':
        for y in range(min(abs(boat.position[0][1]-1), 0), min(boat.position[-1][1]+2, 10)):
            for x in range(min(abs(boat.position[0][0]-1), 0), min(boat.position[0][0]+2, 10)):
                if grille[y][x] == 1:
                    return False # il y a deja un bateau
    if boat.dir == 'horz':
        for y in range(min(abs(boat.position[0][1]-1), 0), min(boat.position[0][1]+2, 10)):
            for x in range(min(abs(boat.position[0][0]-1), 0), min(boat.position[-1][0]+2, 10)):
                if grille[y][x] == 1:
                    return False # il y a deja un bateau
    return True # y a pas de bateau gogogo



def placeBoat(boat:Bateau):
    """ place le bateau dans la grille"""
    for pos in boat.position:
        grille[pos[1]][pos[0]] = 1

def check_place(boat:Bateau) -> bool:
    """ place le bateau si il y a la place
        return True si fait
        return False si Impossible
    """
    if check_around_boat(boat):
        placeBoat(boat)
        return True
    else:
        print('ya pas la place')
        return False



# pos_kats = create_pos(5,(6,1),'horz')
# katsuragi = Bateau(pos_kats,'horz')
# pos_aya = create_pos(4, (4,2), 'vert')
# ayanami = Bateau(pos_aya, 'vert')

# check_place(katsuragi)

# pprint(grille)


team1 = []

for boat in bateaux.items():
    leng = boat[1]
    name = boat[0]
    # create_pos(len, (r.randint(1,11-len),r.randint(1,11-len)), (temp_directiom := r.choice(dirs)))
    team1.append(Bateau((create_pos(leng, (r.randint(1,11-leng),r.randint(1,11-leng)), (temp_direction := r.choice(dirs)))),temp_direction))

for boat in team1 :
    i = 0
    while (not check_place(boat)) and  i < 1000:
        boat = Bateau((create_pos(leng, (r.randint(1,11-leng),r.randint(1,11-leng)), (temp_direction := r.choice(dirs)))),temp_direction)
        i += 1

print(team1)
pprint(grille)

# if check_around_boat(katsuragi):    # si ya la place
#     placeBoat(katsuragi)            # pose le bateau
#     pprint(grille)                  # affiche la grid
# else:
#     print('ya pas la place')

# print('\n')

# if check_around_boat(ayanami):
#     placeBoat(ayanami)
#     pprint(grille)
# else:
#     print('ya pas la place')


        

# def afficheGrille(grille):
#     pprint(grille)

# print(create_pos(5, (1,1), 'horz'))
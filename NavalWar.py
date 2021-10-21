from pprint import pprint
### aure

### HELP GRID 
### 0 => EAU
### 1 => BOAT
### 2 => BOAT TOUCHÉ


grille = [[0 for _ in range(10)] for _ in range(10)]



class Bateau():
    def __init__(self, position, dir, alive=True) -> None:
        self.position = position
        self.dir = dir
        self.alive = alive

    def is_alive(self):           # WIP
        for i in range(len(self.position)):
            if grille[ self.position[0+i][1] ][ self.position[0+i][0] ] == 0:
                pass # TODO => check si ttes les pos sont vivant
    
    def place_boat(self):
        pass # TODO => placer avec self.position



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
        for y in range(boat.position[0][1]-1, boat.position[-1][1]+1):
            for x in range(boat.position[0][0]-1,boat.position[0][0]+1):
                if grille[y][x] == 1:
                    return False # il y a deja un bateau
    if boat.dir == 'horz':
        for y in range(boat.position[0][1]-1, boat.position[0][1]+1):
            for x in range(boat.position[0][0]-1,boat.position[-1][0]+1):
                if grille[y][x] == 1:
                    return False # il y a deja un bateau
    return True # y a pas de bateau gogogo



def placeBoat(boat:Bateau):
    """ place le bateau dans la grille"""
    for pos in boat.position:
        grille[pos[1]][pos[0]]= 1



pos_kats = create_pos(5,(3,3),'horz')
katsuragi = Bateau(pos_kats,'horz')
pos_aya = create_pos(4, (4,2), 'vert')
ayanami = Bateau(pos_aya, 'vert')



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
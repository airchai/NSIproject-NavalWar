from pprint import pprint
### aure
grille = [['O' for _ in range(10)] for _ in range(10)]


class Bateau():
    def __init__(self, position, alive=True) -> None:
        self.position = position
        self.alive = alive

    def is_alive(self):           # WIP
        for i in range(len(self.position)):
            if grille[ self.position[0+i][1] ][ self.position[0+i][0] ] == 0:
                pass


def create_pos(lenght:int, position:tuple, dir:str) -> list:
    """ créé la liste de tuples qui contient les positions de chacune des parties du navire
        lenght : longueur en cases du bateau
        position : coordonnées la case la plus haute ou la plus à gauche du bateau
        dir : 'horz' ou 'vert' 
    """
    if dir == 'horz':
        if position[0]+lenght-1 > 10 :
            return 'le bateau sort de la grille'
        return [tuple([position[0]+i, position[1]]) for i in range(lenght)]
    if dir == 'vert':
        if position[1]+lenght-1 > 10 :
            return 'le bateau sort de la grille'
        return [tuple([position[0], position[1]+i]) for i in range(lenght)]
    else:
        return "argument dir invalide"


# def afficheGrille(grille):
#     pprint(grille)

# def placeBoat(len:int, pos:tuple, dir=None):
    
#     assert pos[0] or pos[1] <= len(grille[0]), "position hors de la grille"
#     assert pos[0]+len-1 or pos[1]+len-1 <= len(grille[0]), "le beateau sors de la grille"

#     if dir =='horz':
#         for i in range(len):
#             grille[pos[1]-1][pos[0]-1+i] = 'X'
#     elif dir == 'vert':
#         for i in range(len):
#             grille[pos[1]-1+i][pos[0]-1] = 'X'
        

# print(create_pos(5, (1,1), 'horz'))
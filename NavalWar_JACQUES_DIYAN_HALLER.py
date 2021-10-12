from pprint import pprint
### aure
grille = [['O' for _ in range(10)] for _ in range(10)]




def afficheGrille(grille):
    pprint(grille)

def placeBoat(len:int, pos:tuple, dir=None):
    
    assert pos[0] or pos[1] <= len(grille[0]), "position hors de la grille"
    assert pos[0]+len-1 or pos[1]+len-1 <= len(grille[0]), "le beateau sors de la grille"

    if dir =='horz':
        for i in range(len):
            grille[pos[1]-1][pos[0]-1+i] = 'X'
    elif dir == 'vert':
        for i in range(len):
            grille[pos[1]-1+i][pos[0]-1] = 'X'
        

placeBoat(3, (2,2),'vert')

afficheGrille(grille)

### tibo
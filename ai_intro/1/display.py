import numpy as np
from rule import *

def Display(display_map):
    posy = display_map.posy
    posx = display_map.posx
    matrix = display_map.matrix.copy()
    matrix[posy][posx] = 3
    if  display_map.dimension == 'x':
        matrix[posy][posx + 1] = 3

    elif  display_map.dimension == 'z':
        matrix[posy + 1 ][posx ] = 3
    print(matrix)
    print("count child is: ",len(display_map.child))
    print()


def Display_child(root):
    print('Display child')
    for i in root.child:
        Display(i)

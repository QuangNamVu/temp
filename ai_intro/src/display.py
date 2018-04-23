import numpy as np
from rule import *

def Display(display_map,targety,targetx):
    posy = display_map.posy
    posx = display_map.posx
    matrix = display_map.matrix.copy()
    matrix[posy][posx] = 4
    matrix[targety][targetx] = 8
    if  display_map.dimension == 'x':
        matrix[posy][posx + 1] = 4

    elif  display_map.dimension == 'z':
        matrix[posy + 1 ][posx ] = 4

    # print(matrix)
    display_symbol(matrix)
    print("count child is: ",len(display_map.child))
    print()


def Display_child(root,targety,targetx):
    print('Display child')
    for idx,i in enumerate(root.child):
        print("SUBROOT NUMBER :", idx)
        Display(i, targetx,targety)

def display_symbol(matrix):
    for i in matrix:
        for j in i:
            if j == 0:
                print(end=".\t")
            elif j ==1:
                print("■", end='\t')
            elif j == 8:
                print("○", end='\t')
            elif j == 4:
                print("△", end='\t')
        print()


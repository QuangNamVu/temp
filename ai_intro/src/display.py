import numpy as np
from rule import *
import time

def Display(display_map,targety,targetx, message = None):
    if message:
        print("---------------\t", message)
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
    display_symbol(matrix,display_map.dimension)
    # print("count child is: ",len(display_map.child))
    print("------------------------------------------")

def Display_child(root,targety,targetx,message = None):
    print(message)
    for idx,i in enumerate(root.child):
        # print("SUBROOT NUMBER :", idx)
        Display(i, targety,targetx, message +" move " + i.last_move +" NUMBER " + str(idx) )


def display_symbol(matrix,dimension):
    end_symbol = '\t'
    sym = "X"
    if dimension is 'y':
        sym = "Y"
    elif dimension is 'z':
        sym = "Z"

    for i in matrix:
        for j in i:
            if j == 0:
                print(end=end_symbol)
            elif j ==1:
                print("⚫", end=end_symbol)
# ☑
            elif j == 8:
                print("⚐", end=end_symbol)

            elif j == 4:
                print(sym, end=end_symbol)
        print()

def TraceBack(target_node, ty, tx):
    stack = []
    while(target_node.parrent !=None):
        stack.append(target_node)
        target_node = target_node.parrent
    for i in reversed(stack):
        print(i.last_move)
        Display(i,ty, tx)

        # clear man hinh
        for j in range(20):
            print()
        time.sleep(0.8)

    print("It took ", len(stack), " steps")

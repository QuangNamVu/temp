from add_move import *
from load import *
from rule import *
from generate import *
from display import *


def tree_bfs(root, targety, targetx, path_table):
    thislevel = [root]
    count = 0
    while thislevel and count < 5:
        count += 1
        nextlevel = list()
        for sub_node in thislevel:

            # TODO:
            # neu o vi tri dich return

            if sub_node.posx == targetx and sub_node.posy == targety:
                print('success')
                return

            Generate(sub_node, path_table)
            for i in sub_node.child:
                nextlevel.append(i)
        print()
        thislevel = nextlevel

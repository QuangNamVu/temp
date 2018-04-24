from generate import *
import sys
from exitstatus import ExitStatus


def tree_bfs(root, targety, targetx, path_table):
    thislevel = [root]
    max_step = 20
    count = 0
    while thislevel and count < max_step:
        count += 1
        nextlevel = list()
        for sub_node in thislevel:

            # TODO:
            # neu o vi tri dich return

            if sub_node.posx == targetx and sub_node.posy == targety and sub_node.dimension is 'y':
                print('SUCCESS')
                # sys.exit(ExitStatus.success)
                return sub_node

            Generate(sub_node, path_table)
            for i in sub_node.child:
                nextlevel.append(i)
        print()
        thislevel = nextlevel

    print("CANNOT FIND")


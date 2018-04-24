from generate import *
import sys
from exitstatus import ExitStatus


def tree_dfs(sub_node, targety, targetx, path_table):

    if sub_node.posx == targetx and sub_node.posy == targety and sub_node.dimension is 'y':
        print('SUCCESS')
        return sub_node
    Generate(sub_node, path_table)

    for i in sub_node.child:
        tree_dfs(i,targety,targetx, path_table)



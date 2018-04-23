from add_move import *
from load import *
from rule import *
from generate import *
from display import *
from BFS import *

#display de in truc tiep se khong ton RAM +CPU neu khong chay
#======================================================================


root = Load_map("../data/input.txt")
tx = root.target_x
ty = root.target_y

# status_table()
path_table = root.status_table()


Display(root,root.target_y,root.target_x)

Generate(root, path_table)
child1 = root.child[2]
Generate(child1, path_table)

print('------------------------------------')
Display(child1,ty,tx)
Display_child(child1,ty,tx)
# tree_bfs(root, root.target_y, root.target_x, path_table)

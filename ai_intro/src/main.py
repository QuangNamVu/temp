from add_move import *
from load import *
from rule import *
from generate import *
from display import *
from BFS import *

input = "2.txt"
#display de in truc tiep se khong ton RAM +CPU neu khong chay
#======================================================================
root = Load_map("../map/" + input)
tx = root.target_x
ty = root.target_y
# ty tx la vi tri dich
# khi chay dich se o vi tri nen
#======================================================================



# status_table()
if __name__ == "__main__":
    path_table = root.status_table()

    Generate(root, path_table)
    Display(root,ty,tx, "MAP")

    target_Node = tree_bfs(root,ty,tx,path_table)


    TraceBack(target_Node, ty, tx)

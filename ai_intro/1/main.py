import imp
import math
import numpy as np
from add_move import *

from load import *
from rule import *
from generate import *
from display import *

#display de in truc tiep se khong ton RAM +CPU neu khong chay
#======================================================================


root = Load_map("../data/input.txt")

# status_table()
path_table = root.status_table()


Display(root)

Generate(root, path_table)

Display_child(root)


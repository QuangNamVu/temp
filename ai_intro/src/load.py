import numpy as np
from rule import NODE

class Load_map(NODE):
    def __init__(self,path):
        matrix = np.loadtxt(path, dtype='i', delimiter=' ')
        pos_begin = np.argwhere(matrix == 3 )
        posy = pos_begin[0][0]
        posx = pos_begin[0][1]
        target = np.argwhere(matrix == 2 )

        self.target_y = target[0][0]
        self.target_x = target[0][1]

        matrix[posy][posx] = 1
        matrix[self.target_y][self.target_x] = 1

        NODE.__init__(self, matrix,posy,posx,'y',False)

    def status_table(self):
        m,n = self.matrix.shape
        table = np.zeros((m,n,3), dtype=int)
        table[self.posy][self.posx][1] = 1
        return table

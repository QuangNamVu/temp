import numpy as np
from rule import NODE

class Load_map(NODE):
    def __init__(self,path):
        matrix = np.loadtxt(path, dtype='i', delimiter=' ')
        pos_begin = np.argwhere(matrix == 3 )
        posy = pos_begin[0][0]
        posx = pos_begin[0][1]
        matrix[posy][posx] = 1

        NODE.__init__(self, matrix,posy,posx,'y',False)

    def status_table(self):
        m,n = self.matrix.shape
        return np.zeros((m,n,3))

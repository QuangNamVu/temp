import copy
# from tree import NODE

class NODE(object):
    def __init__(self,m,y,x,d,is_split):
        self.matrix = m.copy()
        self.posy = y
        self.posx = x
        self.dimension= d
        self.is_split = is_split
        self.child = []
        self.last_move = None
        self.parrent = None

    def available_rotate_left(self):
        y = self.posy
        x = self.posx


        if self.is_split and self.matrix[y][x-1] == 1:
            return True

        if self.dimension is 'x' and self.matrix[y][x-1] == 1:
            return True

        if self.dimension is 'y' and self.matrix[y][x-1] == 1 and self.matrix[y][x-2] == 1:
            return True

        if self.dimension is 'z' and self.matrix[y+1][x-1] == 1  and self.matrix[y][x-1] == 1:
            return True

        return False


    def available_rotate_right(self):
        y = self.posy
        x = self.posx
        if self.is_split and self.matrix[y][x+1] == 1:
            return True

        if self.dimension is 'x' and self.matrix[y][x+2] == 1:
            return True

        if self.dimension is 'y' and self.matrix[y][x+1] == 1 and self.matrix[y][x+2] == 1:
            return True

        if self.dimension is 'z' and self.matrix[y+1][x+1] == 1  and self.matrix[y][x+1] == 1:
            return True

        return False


    def available_rotate_up(self):
        y = self.posy
        x = self.posx
        # display_mapension = self.dimension
        if self.is_split and self.matrix[y-1][x] == 1:
            return True

        if self.dimension is 'x' and self.matrix[y-1][x] == 1 and self.matrix[y-1][x+1]:
            return True

        if self.dimension is 'y' and self.matrix[y-1][x] == 1 and self.matrix[y-2][x] == 1:
            return True

        if self.dimension is 'z' and self.matrix[y-1][x] == 1:
            return True

        return False

    def available_rotate_down(self):
        y = self.posy
        x = self.posx
        # print(self.dimension)
        if self.is_split and self.matrix[y+1][x] == 1:
            return True

        if self.dimension is 'x' and self.matrix[y+1][x] == 1 and self.matrix[y+1][x+1]:
            return True

        if self.dimension is 'y' and self.matrix[y+1][x] == 1 and self.matrix[y+2][x] == 1:
            return True

        if self.dimension is 'z' and self.matrix[y+2][x] == 1:
            return True

        return False

from rule import NODE

def move_left(self, path_table):
    child_new = None

    x = self.posx - 1

    # truong hop split 2 cuc nam cham
    if self.is_split:
        child_new = NODE(root.matrix, map_.posy, map_.posx, True, root.dimension)
        self.child.append(child_new)
        return

    dimension = 'z'
    if self.dimension is 'y':
        dimension = 'x'
        x-=1
    elif self.dimension is 'x':
        dimension = 'y'

    if dimension is 'x' and path_table[self.posy][x][0] is 1:
        return
    if dimension is 'y' and path_table[self.posy][x][1] == 1:
        return
    if dimension is 'z' and path_table[self.posy][x][2] == 1:
        return

    if dimension is 'x':
        path_table[self.posy][x][0] = 1
    elif dimension is 'y':
        path_table[self.posy][x][1] = 1
    else:
        path_table[self.posy][x][2] = 1

    child_new = NODE(self.matrix, self.posy, x, dimension, True)
    self.child.append(child_new)

def move_right(self,path_table):
    child_new = None
    # self.child.append(1)

    x = self.posx + 1

    # truong hop split 2 cuc nam cham
    if self.is_split:
        child_new = NODE(root.matrix, map_.posy, map_.posx, True, root.dimension)
        self.child.append(child_new)
        return

    dimension = 'z'
    if self.dimension is 'y':
        dimension = 'x'
    elif self.dimension is 'x':
        dimension = 'y'

    if dimension is 'x' and path_table[self.posy][x][0] is 1:
        return
    if dimension is 'y' and path_table[self.posy][x][1] == 1:
        return
    if dimension is 'z' and path_table[self.posy][x][2] == 1:
        return

    if dimension is 'x':
        path_table[self.posy][x][0] = 1
    elif dimension is 'y':
        path_table[self.posy][x][1] = 1
    else:
        path_table[self.posy][x][2] = 1

    child_new = NODE(self.matrix, self.posy, x, dimension, True)
    self.child.append(child_new)

def move_up(self,path_table):
    child_new = None
    # self.child.append(1)

    y = self.posy - 1

    # truong hop split 2 cuc nam cham
    if self.is_split:
        child_new = NODE(root.matrix, map_.posy, map_.posx, True, root.dimension)
        self.child.append(child_new)
        return

    dimension = 'x'
    if self.dimension is 'z':
        dimension = 'y'
        x-=1
    elif self.dimension is 'y':
        dimension = 'z'

    if dimension is 'x' and path_table[y][self.posx][0] is 1:
        return
    if dimension is 'y' and path_table[y][self.posx][1] == 1:
        return
    if dimension is 'z' and path_table[y][self.posx][2] == 1:
        return

    if dimension is 'x':
        path_table[y][self.posx][0] = 1
    elif dimension is 'y':
        path_table[y][self.posx][1] = 1
    else:
        path_table[y][self.posx][2] = 1

    child_new = NODE(self.matrix, self.posy, x, dimension, True)
    self.child.append(child_new)

def move_down(self,path_table):
    child_new = None
    # self.child.append(1)

    y = self.posy + 1

    # truong hop split 2 cuc nam cham
    if self.is_split:
        child_new = NODE(root.matrix, map_.posy, map_.posx, True, root.dimension)
        self.child.append(child_new)
        return

    dimension = 'x'
    if self.dimension is 'z':
        dimension = 'y'
    elif self.dimension is 'y':
        dimension = 'z'

    if dimension is 'x' and path_table[y][self.posx][0] is 1:
        return
    if dimension is 'y' and path_table[y][self.posx][1] == 1:
        return
    if dimension is 'z' and path_table[y][self.posx][2] == 1:
        return

    if dimension is 'x':
        path_table[y][self.posx][0] = 1
    elif dimension is 'y':
        path_table[y][self.posx][1] = 1
    else:
        path_table[y][self.posx][2] = 1

    child_new = NODE(self.matrix, y, self.posx, dimension, True)
    self.child.append(child_new)

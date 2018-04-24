from rule import NODE

def move_left(self, path_table):
    child_new = None

    x = self.posx - 1

    # truong hop split 2 cuc nam cham
    if self.is_split:
        child_new = NODE(self.matrix, self.posy, self.posx, self.dimension, True)
        self.child.append(child_new)
        return

    dimension = 'z'
    if self.dimension is 'y':
        dimension = 'x'
        x-=1
    elif self.dimension is 'x':
        dimension = 'y'

    if dimension is 'x' and path_table[self.posy][x][0] == 1:
        return
    if dimension is 'y' and path_table[self.posy][x][1] == 1:
        return
    if dimension is 'z' and path_table[self.posy][x][2] == 1:
        return

    if self.dimension is 'x':
        path_table[self.posy][self.posx][0] = 1
    elif self.dimension is 'y':
        path_table[self.posy][self.posx][1] = 1
    else:
        path_table[self.posy][self.posx][2] = 1

    child_new = NODE(self.matrix, self.posy, x, dimension, False)

    child_new.last_move = 'Left'
    child_new.parrent = self
    self.child.append(child_new)

def move_right(self,path_table):
    child_new = None
    # self.child.append(1)

    x = self.posx + 1

    # truong hop split 2 cuc nam cham
    if self.is_split:
        child_new = NODE(self.matrix, self.posy, self.posx, self.dimension, True)
        self.child.append(child_new)
        return

    dimension = 'z'
    if self.dimension is 'y':
        dimension = 'x'
    elif self.dimension is 'x':
        dimension = 'y'
        x+=1

    if dimension is 'x' and path_table[self.posy][x][0] == 1:
        return
    if dimension is 'y' and path_table[self.posy][x][1] == 1:
        return
    if dimension is 'z' and path_table[self.posy][x][2] == 1:
        return

    if self.dimension is 'x':
        path_table[self.posy][self.posx][0] = 1
    elif self.dimension is 'y':
        path_table[self.posy][self.posx][1] = 1
    else:
        path_table[self.posy][self.posx][2] = 1

    child_new = NODE(self.matrix, self.posy, x, dimension, False)
    self.child.append(child_new)
    child_new.last_move = 'Right'
    child_new.parrent = self

def move_up(self,path_table):
    child_new = None
    # self.child.append(1)

    y = self.posy - 1

    # truong hop split 2 cuc nam cham
    if self.is_split:
        child_new = NODE(self.matrix, self.posy, self.posx, self.dimension, True)
        self.child.append(child_new)
        return

    dimension = 'x'
    if self.dimension is 'z':
        dimension = 'y'
    elif self.dimension is 'y':
        dimension = 'z'
        y-=1

    if dimension is 'x' and path_table[y][self.posx][0] == 1:
        return
    if dimension is 'y' and path_table[y][self.posx][1] == 1:
        return
    if dimension is 'z' and path_table[y][self.posx][2] == 1:
        return

    if self.dimension is 'x':
        path_table[self.posy][self.posx][0] = 1
    elif self.dimension is 'y':
        path_table[self.posy][self.posx][1] = 1
    else:
        path_table[self.posy][self.posx][2] = 1

    child_new = NODE(self.matrix, y, self.posx, dimension, False)
    self.child.append(child_new)
    child_new.last_move = 'Up'
    child_new.parrent = self

def move_down(self,path_table):
    child_new = None
    # self.child.append(1)

    y = self.posy + 1

    # truong hop split 2 cuc nam cham
    if self.is_split:
        child_new = NODE(self.matrix, self.posy, self.posx, self.dimension, True)
        self.child.append(child_new)
        return

    dimension = 'x'
    if self.dimension is 'z':
        dimension = 'y'
        y+=1
    elif self.dimension is 'y':
        dimension = 'z'

    if dimension is 'x' and path_table[y][self.posx][0] == 1:
        return
    if dimension is 'y' and path_table[y][self.posx][1] == 1:
        return
    if dimension is 'z' and path_table[y][self.posx][2] == 1:
        return

    if self.dimension is 'x':
        path_table[self.posy][self.posx][0] = 1
    elif self.dimension is 'y':
        path_table[self.posy][self.posx][1] = 1
    else:
        path_table[self.posy][self.posx][2] = 1

    child_new = NODE(self.matrix, y, self.posx, dimension, False)
    self.child.append(child_new)

    child_new.last_move = 'Down'
    child_new.parrent = self

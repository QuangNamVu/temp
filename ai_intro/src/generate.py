from rule import *
from add_move import *

# class Generate(NODE):
def Generate(self, path_table):
        if self.available_rotate_left():
                # print('can move left')
                move_left(self, path_table)
        if self.available_rotate_right():
                # print('can move right')
                move_right(self, path_table)
        if self.available_rotate_up():
                # print('can move up')
                move_up(self, path_table)
        if self.available_rotate_down():
                # print('can move down')
                move_down(self, path_table)

import math
import random

infinity = float("inf")
maxDepth = 5


def insert_r(node, posX, posY):
    node.state[posX][posY] = 'r'


def insert_R(node, posX, posY):
    node.state[posX][posY] = 'R'


def insert_b(node, posX, posY):
    node.state[posX][posY] = 'b'


def insert_B(node, posX, posY):
    node.state[posX][posY] = 'B'


def delete(node, posX, posY):
    node.state[posX][posY] = '.'


def clearState(node):
    for j in range(8):
        for i in range(8):
            node.state[i][j] = '.'


def getValuer(state):
    total = 0
    for i in range(8):
        for j in range(8):
            if state[i][j] == 'r':
                total += 10
            elif state[i][j] == 'R':
                total += 30
            elif state[i][j] == 'b':
                total -= 10
            elif state[i][j] == 'B':
                total -= 30

    return total


# ======================== Print tree=======================================
def PrintNode(node):
    if not node:
        print("This node has been deleted")
        return
    board = node.state
    print("Print node")
    for i in [7, 6, 5, 4, 3, 2, 1, 0]:
        print(i, ":", end=" ")
        for j in range(8):
            print(board[i][j], end=" ")
        print()
    print("   ", 0, 1, 2, 3, 4, 5, 6, 7)
    print("")


def PrintSubroot(root):
    count = 0;
    for i in root.children:
        count += 1
        print("Print subtree ", count, "value is ", i.value)
        PrintNode(i)


# ======================== Copy funtion =======================================
def BoardCopy(board):
    new_board = [[]] * 8
    for i in range(8):
        new_board[i] = [] + board[i]
    return new_board


# ======================== Class Node =======================================
class Node(object):
    def __init__(self, state, move):
        self.move = move
        self.children = []
        new_state = BoardCopy(state)
        self.value = -1
        if not move:
            self.state = new_state
            return
        elif len(move) == 2 and abs(move[1][0] - move[0][0]) == 1:
            new_state[move[0][0]][move[0][1]] = '.'
            if state[move[0][0]][move[0][1]] == 'b' and move[1][0] == 7:
                new_state[move[1][0]][move[1][1]] = 'B'
            elif state[move[0][0]][move[0][1]] == 'r' and move[1][0] == 0:
                new_state[move[1][0]][move[1][1]] = 'R'
            else:
                new_state[move[1][0]][move[1][1]] = state[move[0][0]][move[0][1]]
                # Jump
                # example: [(1,1),(3,3),(5,5)] or [(1,1),(3,3),(5,1)]
        else:
            step = 0
            new_state[move[0][0]][move[0][1]] = '.'
            while step < len(move) - 1:
                new_state[int(math.floor((move[step][0] + move[step + 1][0]) / 2))][
                    int(math.floor((move[step][1] + move[step + 1][1]) / 2))] = '.'
                step = step + 1
            if state[move[0][0]][move[0][1]] == 'b' and move[step][0] == 7:
                new_state[move[step][0]][move[step][1]] = 'B'
            elif state[move[0][0]][move[0][1]] == 'r' and move[step][0] == 0:
                new_state[move[step][0]][move[step][1]] = 'R'
            else:
                new_state[move[step][0]][move[step][1]] = state[move[0][0]][move[0][1]]
        self.state = new_state

    def add_child(self, move):
        # print("Adding child move is ", move)
        child = Node(self.state, move)
        self.children.append(child)
        return child


def delete_Recursive(root):
    if not root:
        return
    for i in root.children:
        delete_Recursive(i)
    root.delete()


def PrintTree(root, blankspace):
    if not root:
        print("__")
    numChild = len(root.children)
    # mid = math.floor(numChild / 2)
    for i in range(numChild):
        PrintTree(root.children[i], blankspace + 1)
    for i in range(blankspace):
        print("         ", end="")
    print(root.move, getValuer(root.state))
    # for i in range(mid,numChild):
    #     PrintTree(root.children[i],blankspace+1)


# ======================== Check cycle return boolean ==========================
# ======================== Return true if have cycle default lengthPath =1
def isCycle(path, destination, lengthPath):
    if lengthPath < 2:
        return False
    xuoi = [destination, path[lengthPath - 1]]
    nguoc = [path[lengthPath - 1], destination]
    for i in range(lengthPath - 2, -1, -1):
        if path[i:i + 2] == xuoi:
            return True
    for i in range(lengthPath - 1):
        if path[i:i + 2] == nguoc:
            return True
    return False


def isCycle2(path, destination, lengthPath):
    for i in path:
        if i == destination:
            return True
    return False


# ======================== funtion generate moving ====================================
def move_r(root, posX, posY):
    if posX < 1:
        return
    posX1 = posX - 1
    posY1 = posY - 1
    posY2 = posY + 1
    if posY1 >= 0 and root.state[posX1][posY1] == '.':
        move = [posX, posY], [posX1, posY1]
        root.add_child(move)
    if posY2 < 8 and root.state[posX1][posY2] == '.':
        move = [posX, posY], [posX1, posY2]
        root.add_child(move)


def move_b(root, posX, posY):
    if posX > 6:
        return
    posX1 = posX + 1
    posY1 = posY - 1
    posY2 = posY + 1
    # left
    if posY1 >= 0 and root.state[posX1][posY1] == '.':
        move = [posX, posY], [posX1, posY1]
        root.add_child(move)
    # right
    if posY2 < 8 and root.state[posX1][posY2] == '.':
        move = [posX, posY], [posX1, posY2]
        root.add_child(move)


def xuongtraimove(root, x, y, posX, posY):
    while x > 0 and y > 0:
        x -= 1;
        y -= 1
        if root.state[x][y] != ".":
            break
        root.add_child([[posX, posY], [x, y]])


def xuongphaimove(root, x, y, posX, posY):
    while x > 0 and y < 7:
        x -= 1;
        y += 1
        if root.state[x][y] != ".":
            break
        root.add_child([[posX, posY], [x, y]])


def lentraimove(root, x, y, posX, posY):
    while x < 7 and y > 0:
        x += 1;
        y -= 1
        if root.state[x][y] != ".":
            break
        root.add_child([[posX, posY], [x, y]])


def lenphaimove(root, x, y, posX, posY):
    while x < 7 and y < 7:
        x += 1;
        y += 1
        if root.state[x][y] != ".":
            break
        root.add_child([[posX, posY], [x, y]])


# ___________________________________KIEM TRA CO JUMP QUEEN_____________________________________________________________
def checklentraiR(root, x, y, pos):
    while x < 6 and y > 1:
        if root.state[x + 1][y - 1] != '.' and root.state[x + 2][y - 2] != '.':
            return False
        if (root.state[x + 1][y - 1] == 'b' or root.state[x + 1][y - 1] == 'B') and root.state[x + 2][y - 2] == '.':
            pos += [x + 2, y - 2, x + 1, y - 1]
            return True
        x += 1
        y -= 1
    return False


def checkxuongtraiR(root, x, y, pos):
    while x > 1 and y > 1:
        if root.state[x - 1][y - 1] != '.' and root.state[x - 2][y - 2] != '.':
            return False
        if (root.state[x - 1][y - 1] == 'b' or root.state[x - 1][y - 1] == 'B') and root.state[x - 2][y - 2] == '.':
            pos += [x - 2, y - 2, x - 1, y - 1]
            return True
        x -= 1
        y -= 1
    return False


def checklenphaiR(root, x, y, pos):
    while x < 6 and y < 6:
        if root.state[x + 1][y + 1] != '.' and root.state[x + 2][y + 2] != '.':
            return False
        if (root.state[x + 1][y + 1] == 'b' or root.state[x + 1][y + 1] == 'B') and root.state[x + 2][y + 2] == '.':
            pos += [x + 2, y + 2, x + 1, y + 1]

            return True
        x += 1
        y += 1
    return False


def checkxuongphaiR(root, x, y, pos):
    while x > 1 and y < 6:
        if root.state[x - 1][y + 1] != '.' and root.state[x - 2][y + 2] != '.':
            return False
        if (root.state[x - 1][y + 1] == 'b' or root.state[x - 1][y + 1] == 'B') and root.state[x - 2][y + 2] == '.':
            pos += [x - 2, y + 2, x - 1, y + 1]
            return True
        x -= 1
        y += 1
    return False


def checklentraiB(root, x, y, pos):
    while x < 6 and y > 1:
        if root.state[x + 1][y - 1] != '.' and root.state[x + 2][y - 2] != '.':
            return False
        if (root.state[x + 1][y - 1] == 'r' or root.state[x + 1][y - 1] == 'R') and root.state[x + 2][y - 2] == '.':
            pos += [x + 2, y - 2, x + 1, y - 1]
            return True
        x += 1
        y -= 1
    return False


def checkxuongtraiB(root, x, y, pos):
    while x > 1 and y > 1:
        if root.state[x - 1][y - 1] != '.' and root.state[x - 2][y - 2] != '.':
            return False
        if (root.state[x - 1][y - 1] == 'r' or root.state[x - 1][y - 1] == 'R') and root.state[x - 2][y - 2] == '.':
            pos += [x - 2, y - 2, x - 1, y - 1]
            return True
        x -= 1
        y -= 1
    return False


def checklenphaiB(root, x, y, pos):
    while x < 6 and y < 6:
        if root.state[x + 1][y + 1] != '.' and root.state[x + 2][y + 2] != '.':
            return False
        if (root.state[x + 1][y + 1] == 'r' or root.state[x + 1][y + 1] == 'R') and root.state[x + 2][y + 2] == '.':
            pos += [x + 2, y + 2, x + 1, y + 1]

            return True
        x += 1
        y += 1
    return False


def checkxuongphaiB(root, x, y, pos):
    while x > 1 and y < 6:
        if root.state[x - 1][y + 1] != '.' and root.state[x - 2][y + 2] != '.':
            return False
        if (root.state[x - 1][y + 1] == 'r' or root.state[x - 1][y + 1] == 'R') and root.state[x - 2][y + 2] == '.':
            pos += [x - 2, y + 2, x - 1, y + 1]
            return True
        x -= 1
        y += 1
    return False


def moveQueen(root, posX, posY):
    xuongtraimove(root, posX, posY, posX, posY)
    xuongphaimove(root, posX, posY, posX, posY)
    lenphaimove(root, posX, posY, posX, posY)
    lentraimove(root, posX, posY, posX, posY)


# ======================== funtion generate jumping ====================================

def jump_Queen_R(root, posX, posY, move, lengthMove, path, listMove):
    if posX < 0 or posX > 7 or posY < 0 or posY > 7:
        if lengthMove > 1:
            root.add_child(move)
        return
    isLeaf = True

    des = []
    if checkxuongtraiR(root, posX, posY, des):
        if not isCycle2(path, [des[2], des[3]], lengthMove - 1):
            while des[0] > -1 and des[1] > -1 and root.state[des[0]][des[1]] == '.':
                jump_Queen_R(root, des[0], des[1], move + [[des[0], des[1]]], lengthMove + 1, path + [[des[2], des[3]]],
                             listMove)
                des[0] -= 1
                des[1] -= 1
            isLeaf = False
    des = []
    if checkxuongphaiR(root, posX, posY, des):
        if not isCycle2(path, [des[2], des[3]], lengthMove - 1):
            while des[0] > -1 and des[1] < 8 and root.state[des[0]][des[1]] == '.':
                jump_Queen_R(root, des[0], des[1], move + [[des[0], des[1]]], lengthMove + 1, path + [[des[2], des[3]]],
                             listMove)
                des[0] -= 1
                des[1] += 1
            isLeaf = False
    des = []
    if checklenphaiR(root, posX, posY, des):  # khong duoc return
        if not isCycle2(path, [des[2], des[3]], lengthMove - 1):
            while des[0] < 8 and des[1] < 8 and root.state[des[0]][des[1]] == '.':
                jump_Queen_R(root, des[0], des[1], move + [[des[0], des[1]]], lengthMove + 1, path + [[des[2], des[3]]],
                             listMove)
                des[0] += 1
                des[1] += 1
            isLeaf = False
    des = []
    if checklentraiR(root, posX, posY, des):
        if not isCycle2(path, [des[2], des[3]], lengthMove - 1):
            while des[0] < 8 and des[1] > -1 and root.state[des[0]][des[1]] == '.':
                jump_Queen_R(root, des[0], des[1], move + [[des[0], des[1]]], lengthMove + 1, path + [[des[2], des[3]]],
                             listMove)
                des[0] += 1
                des[1] -= 1
            isLeaf = False

    if lengthMove > 1 and isLeaf:
        listMove.append(move)


def jump_r_Recursion(root, posX, posY, move, lengthMove, list):
    if posX < 0 or posY < 0 or posX > 7 or posY > 7:
        if lengthMove > 1:  # co truong hop node subroot
            print(lengthMove)
            root.add_child(move)
        return
    isLeaf = True
    tren1 = posX + 1
    tren2 = posX + 2
    duoi1 = posX - 1
    duoi2 = posX - 2
    trai1 = posY - 1
    trai2 = posY - 2
    phai1 = posY + 1
    phai2 = posY + 2
    # Tren trai
    if tren2 < 8 and trai2 >= 0 and root.state[tren2][trai2] == '.':
        if root.state[tren1][trai1] == 'B' or root.state[tren1][trai1] == 'b':
            if not isCycle(move, [tren2, trai2], lengthMove):
                jump_r_Recursion(root, tren2, trai2, move + [[tren2, trai2]], lengthMove + 1, list)
                isLeaf = False
    # Tren phai
    if tren2 < 8 and phai2 < 8 and root.state[tren2][phai2] == '.':
        if root.state[tren1][phai1] == 'B' or root.state[tren1][phai1] == 'b':
            if not isCycle(move, [tren2, phai2], lengthMove):
                jump_r_Recursion(root, tren2, phai2, move + [[tren2, phai2]], lengthMove + 1, list)
                isLeaf = False
    # Duoi phai
    if duoi2 >= 0 and phai2 < 8 and root.state[duoi2][phai2] == '.':
        if root.state[duoi1][phai1] == 'B' or root.state[duoi1][phai1] == 'b':
            if not isCycle(move, [duoi2, phai2], lengthMove):
                jump_r_Recursion(root, duoi2, phai2, move + [[duoi2, phai2]], lengthMove + 1, list)
                isLeaf = False
    # Duoi trai
    if duoi2 >= 0 and trai2 >= 0 and root.state[duoi2][trai2] == '.':
        if root.state[duoi1][trai1] == 'B' or root.state[duoi1][trai1] == 'b':
            if not isCycle(move, [duoi2, trai2], lengthMove):
                jump_r_Recursion(root, duoi2, trai2, move + [[duoi2, trai2]], lengthMove + 1, list)
                isLeaf = False
    # node
    if lengthMove > 1 and isLeaf:
        list.append(move)


def jump_r(root, posX, posY):
    bestmove = []
    jump_r_Recursion(root, posX, posY, [[posX, posY]], 1, bestmove)
    max = 0
    for i in bestmove:
        if max < len(i):
            max = len(i)
    for i in bestmove:
        if len(i) == max:
            root.add_child(i)


def jump_R(root, posX, posY):
    bestmove = []
    jump_Queen_R(root, posX, posY, [[posX, posY]], 1, [], bestmove)
    max = 0
    for i in bestmove:
        if max < len(i):
            max = len(i)
    for i in bestmove:
        if len(i) == max:
            root.add_child(i)


def generate_r(root):
    for i in range(8):
        for j in range(i % 2, 8, 2):
            if root.state[i][j] == 'r':
                jump_r(root, i, j)
            elif root.state[i][j] == 'R':
                path = []
                jump_R(root, i, j)

    if root.children:
        return
    for i in range(8):
        for j in range(i % 2, 8, 2):
            if root.state[i][j] == 'r':
                move_r(root, i, j)
            elif root.state[i][j] == 'R':
                moveQueen(root, i, j)


# ______________________________________________________________#
# _____________________________B________________________________#
# ______________________________________________________________#
def jump_Queen_B(root, posX, posY, move, lengthMove, path, listMove):
    if posX < 0 or posX > 7 or posY < 0 or posY > 7:
        if lengthMove > 1:
            root.add_child(move)
        return
    isLeaf = True

    des = []
    if checkxuongtraiB(root, posX, posY, des):
        if not isCycle2(path, [des[2], des[3]], lengthMove - 1):
            while des[0] > -1 and des[1] > -1 and root.state[des[0]][des[1]] == '.':
                jump_Queen_B(root, des[0], des[1], move + [[des[0], des[1]]], lengthMove + 1, path + [[des[2], des[3]]],
                             listMove)
                des[0] -= 1
                des[1] -= 1
            isLeaf = False
    des = []
    if checkxuongphaiB(root, posX, posY, des):
        if not isCycle2(path, [des[2], des[3]], lengthMove - 1):
            while des[0] > -1 and des[1] < 8 and root.state[des[0]][des[1]] == '.':
                jump_Queen_B(root, des[0], des[1], move + [[des[0], des[1]]], lengthMove + 1, path + [[des[2], des[3]]],
                             listMove)
                des[0] -= 1
                des[1] += 1
            isLeaf = False
    des = []
    if checklenphaiB(root, posX, posY, des):  # khong duoc return
        if not isCycle2(path, [des[2], des[3]], lengthMove - 1):
            while des[0] < 8 and des[1] < 8 and root.state[des[0]][des[1]] == '.':
                jump_Queen_B(root, des[0], des[1], move + [[des[0], des[1]]], lengthMove + 1, path + [[des[2], des[3]]],
                             listMove)
                des[0] += 1
                des[1] += 1
            isLeaf = False
    des = []
    if checklentraiB(root, posX, posY, des):
        if not isCycle2(path, [des[2], des[3]], lengthMove - 1):
            while des[0] < 8 and des[1] > -1 and root.state[des[0]][des[1]] == '.':
                jump_Queen_B(root, des[0], des[1], move + [[des[0], des[1]]], lengthMove + 1, path + [[des[2], des[3]]],
                             listMove)
                des[0] += 1
                des[1] -= 1
            isLeaf = False

    if lengthMove > 1 and isLeaf:
        listMove.append(move)


def jump_b_Recursion(root, posX, posY, move, lengthMove, list):
    if posX < 0 or posY < 0 or posX > 7 or posY > 7:
        if lengthMove > 1:  # co truong hop node subroot
            print(lengthMove)
            root.add_child(move)
        return
    isLeaf = True
    tren1 = posX + 1
    tren2 = posX + 2
    duoi1 = posX - 1
    duoi2 = posX - 2
    trai1 = posY - 1
    trai2 = posY - 2
    phai1 = posY + 1
    phai2 = posY + 2
    # Tren trai
    if tren2 < 8 and trai2 >= 0 and root.state[tren2][trai2] == '.':
        if root.state[tren1][trai1] == 'R' or root.state[tren1][trai1] == 'r':
            if not isCycle(move, [tren2, trai2], lengthMove):
                jump_b_Recursion(root, tren2, trai2, move + [[tren2, trai2]], lengthMove + 1, list)
                isLeaf = False
    # Tren phai
    if tren2 < 8 and phai2 < 8 and root.state[tren2][phai2] == '.':
        if root.state[tren1][phai1] == 'R' or root.state[tren1][phai1] == 'r':
            if not isCycle(move, [tren2, phai2], lengthMove):
                jump_b_Recursion(root, tren2, phai2, move + [[tren2, phai2]], lengthMove + 1, list)
                isLeaf = False
    # Duoi phai
    if duoi2 >= 0 and phai2 < 8 and root.state[duoi2][phai2] == '.':
        if root.state[duoi1][phai1] == 'R' or root.state[duoi1][phai1] == 'r':
            if not isCycle(move, [duoi2, phai2], lengthMove):
                jump_b_Recursion(root, duoi2, phai2, move + [[duoi2, phai2]], lengthMove + 1, list)
                isLeaf = False
    # Duoi trai
    if duoi2 >= 0 and trai2 >= 0 and root.state[duoi2][trai2] == '.':
        if root.state[duoi1][trai1] == 'R' or root.state[duoi1][trai1] == 'r':
            if not isCycle(move, [duoi2, trai2], lengthMove):
                jump_b_Recursion(root, duoi2, trai2, move + [[duoi2, trai2]], lengthMove + 1, list)
                isLeaf = False
    # node
    if lengthMove > 1 and isLeaf:
        list.append(move)


def jump_b(root, posX, posY):
    bestmove = []
    jump_b_Recursion(root, posX, posY, [[posX, posY]], 1, bestmove)
    max = 0
    for i in bestmove:
        if max < len(i):
            max = len(i)
    for i in bestmove:
        if len(i) == max:
            root.add_child(i)


def jump_B(root, posX, posY):
    bestmove = []
    jump_Queen_B(root, posX, posY, [[posX, posY]], 1, [], bestmove)
    max = 0
    for i in bestmove:
        if max < len(i):
            max = len(i)
    for i in bestmove:
        if len(i) == max:
            root.add_child(i)


def generate_b(root):
    for i in range(8):
        for j in range(i % 2, 8, 2):
            if root.state[i][j] == 'b':
                jump_b(root, i, j)
            elif root.state[i][j] == 'B':
                jump_B(root, i, j)

    if root.children:
        return
    for i in range(8):
        for j in range(i % 2, 8, 2):
            if root.state[i][j] == 'b':
                move_b(root, i, j)
            elif root.state[i][j] == 'B':
                moveQueen(root, i, j)


def getmaxr(root, alpha, beta, depth):
    root.visit = True
    if depth == maxDepth:
        return getValuer(root.state)
    v = -infinity
    generate_r(root)
    for i in root.children:
        temp = getminr(i, alpha, beta, depth + 1)
        if temp > v:
            v = temp
            if v >= beta:
                root.value = v
                return v
            if v > alpha:
                alpha = v
    root.value = v
    return v


def getminr(root, alpha, beta, depth):  # depth =1,3
    root.visit = True
    if depth == maxDepth:
        return getValuer(root.state)
    v = infinity
    generate_b(root)
    for i in root.children:
        temp = getmaxr(i, alpha, beta, depth + 1)
        if temp < v:
            v = temp
            if v <= alpha:
                root.value = v
                return v
            if v < beta:
                beta = v
    root.value = v
    return v


def alphabeta(player, root):
    if player.str == 'b':
        min = getminr(root, -infinity, infinity, 0)
        for i in root.children:
            if i.value == min:
                return i.move
        return []
    max = getmaxr(root, -infinity, infinity, 0)
    for i in root.children:
        if i.value == max:
            return i.move
    return []

# ======================== Class Player =======================================
class Player:
    def __init__(self, str_name):
        self.str = str_name

    def __str__(self):
        return self.str

    def nextMove(self, state):
        root = Node(state, [])

        return alphabeta(self, root)

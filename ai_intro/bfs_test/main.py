class Node():
    def __init__(self, value):
        self.value = value
        self.child = []

    def add_child(self, value):
        child = Node(value)
        self.child.append(child)
        return child


def tree_bfs(rootnode):
    thislevel = [rootnode]
    while thislevel:
        nextlevel = list()
        for child in thislevel:

            # TODO:
            # neu o vi tri dich return

            print(child.value)

            for i in child.child:
                nextlevel.append(i)
        print()
        thislevel = nextlevel

if __name__ == '__main__':
    root = Node(0)
    child2 = root.add_child(2)
    child6 = root.add_child(6)
    child2.add_child(1)
    child3 = child2.add_child(3)
    child3.add_child(9)
    child6 = child2.add_child(7)
    child6 = child2.add_child(8)

    # import pdb
    # pdb.set_trace()

    tree_bfs(root)

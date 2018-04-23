
# ======================== Class Player =======================================
class Player:
    def __init__(self, str_name):
        self.str = str_name

    def __str__(self):
        return self.str


    # Student MUST implement this function
    # The return value should be a move that is denoted by a list of tuples
    def nextMove(self, state):
        result = [(1,1),(2,2)]
        return result
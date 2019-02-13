from entity.Card import Card

# Board class
class Board:
    # total number of rows
    ROW_NUM = 12
    # total number of columns
    COLUMN_NUM = 8
    # board (12 x 8 matrix of Card objects)
    board = []

    # constructor
    def __init__(self):
        for i in range(self.ROW_NUM):
            list = []
            for j in range(self.COLUMN_NUM):
                list.append(None)
            self.board.append(list)

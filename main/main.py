from entity.Board import Board

'''
check validation of the configuration after placing the new card
    board         : board configuration
    card_rotation : card rotation
    coordinate_x  : horizontal position of left/bottom segment of card
    coordinate_y  : vertical position of left/bottom segment of card
'''
def illegal_configuration(board, card_rotation, coordinate_x, coordinate_y):
    if (card_rotation % 2 == 0) and (coordinate_x == len(board) - 1):
        # upper segment overflow
        return False
    if (card_rotation % 2 == 1) and (coordinate_y == len(board[0]) - 1):
        # right segment overflow
        return False
    if (card_rotation % 2 == 0) and (coordinate_x < len(board) - 1) \
            and (board[coordinate_x + 1][coordinate_y] == None):
        # bottom segment hangs over an empty cell
        return False
    if (card_rotation % 2 == 1) and (coordinate_x < len(board) - 1) \
            and (board[coordinate_x + 1][coordinate_y] == None):
        # right segment hangs over an empty cell
        return False
    if (card_rotation % 2 == 0) and (board[coordinate_x - 1][coordinate_y] != None):
        # position of upper segment is not an empty cell
        return False
    if (card_rotation % 2 == 1) and (board[coordinate_x][coordinate_y + 1] != None):
        # position of right segment is not an empty cell
        return False
    return True

'''
check input validation during regular moves
    zero         : first input has to be 0
    card_rotation: range from 1 to 8
    coordinate_x : horizontal position of left/bottom segment of card
    coordinate_y : vertical position of left/bottom segment of card
    board        : board configuration
'''
def check_input_validation_for_regular_moves(zero, card_rotation,
        coordinate_x, coordinate_y, board):
    if zero != 0:
        return False
    if card_rotation < 1 or card_rotation > 8:
        return False
    if coordinate_x < 0 or coordinate_x >= board.ROW_NUM:
        return False
    if coordinate_y < 0 or coordinate_y >= board.COLUMN_NUM:
        return False
    if illegal_configuration(board, card_rotation, coordinate_x, coordinate_y):
        return False
    return True

def print_board(board):
    for i in range(board.ROW_NUM):
        for j in range(board.COLUMN_NUM):
            print(board.board[i][j], end=' ')
        print()

def main():
    board = Board()
    regular_moves = True
    card_num = 0
    print(board.board)

    while regular_moves:
        if card_num > 24:
            break

        zero = input()              # for regular moves, should be 0
        card_rotation = input()     # demonstrate the card rotation
        coordinate_x = input()      # card position x
        coordinate_y = input()      # card position y
        if not check_input_validation_for_regular_moves(zero, card_rotation, coordinate_x, coordinate_y, board.board):
           break

        

    if card_num != 24:
        return -1

    recycle_moves = True

if __name__ == '__main__':
    main()
# import numpy as np
#
# ROW_COUNT = 12
# COLUMN_COUNT = 8
#
# def create_board():
#     board = np.zeros((12, 8))
#     return board
#
# def drop_piece(board, row, col, piece):
#     board[row][col] = piece
#
# def is_valid_location(board, col):
#     return board[8][col] == 0
#
# def get_next_open_row(board, col):
#     for r in range(ROW_COUNT):
#         if board[r][col] == 0:
#             return r
#
# def print_board(board):
#     print(np.flip(board, 0))
#
# def main():
#     board = create_board()
#     print_board(board)
#
#     game_over = False
#     turn = 0
#
#     while not game_over:
#         # ask for player 1 input
#         if turn == 0:
#             col = int(input("Player 1 make your selection: "))
#
#             if is_valid_location(board, col):
#                 row = get_next_open_row(board, col)
#                 drop_piece(board, row, col, 1)
#
#         # ask for player 2 input
#         else:
#             col = int(input("Player 2 make your selection: "))
#
#             if is_valid_location(board, col):
#                 row = get_next_open_row(board, col)
#                 drop_piece(board, row, col, 2)
#
#         turn += 1
#         turn = turn % 2
#
#         print_board(board)
#
# if __name__ == "__main__":
#     main()
from card import Card
ROW_COUNT = 8
COL_COUNT = 12


def create_board():
    board = [['□□' for _ in range(ROW_COUNT)] for _ in range(COL_COUNT)]
    #board = np.zeros((ROW_COUNT,COL_COUNT))
    return board
def drop_piece(board,row,col,piece):
    if(piece is Card.card1):
        if row==11:
            if board[row][col] == '□□' and board[row][col+1] == '□□':
                board[row][col] = piece.left
                board[row][col + 1] = piece.right
                return True
            else:
                print("already fill up")
                return False
        else:
            if board[row][col] == '□□' and board[row][col+1] == '□□':
                if board[row+1][col] == '□□' or board[row+1][col+1]=='□□':
                    print("empty below")
                    return False
                else:
                    board[row][col] = piece.left
                    board[row][col+1]=piece.right
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card2):
        if row+1==11:
            if board[row][col] == '□□' and board[row + 1][col] == '□□':
                board[row][col] = piece.top
                board[row + 1][col] = piece.below
                return True
            else:
                print("already fill up")
                return False
        else:

            if board[row][col] == '□□' and board[row+1][col] == '□□':
                if board[row+2][col] == '□□':
                    print("empty below")
                    return False
                else:
                    board[row][col] = piece.top
                    board[row+1][col]=piece.below
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card3):
        if row==11:
            if board[row][col] == '□□' and board[row][col+1] == '□□':
                board[row][col] = piece.left
                board[row][col + 1] = piece.right
                return True
            else:
                print("already fill up")
                return False
        else:
            if board[row][col] == '□□' and board[row][col+1] == '□□':
                if board[row+1][col] == '□□' or board[row+1][col+1]=='□□':
                    print("empty below")
                    return False
                else:
                    board[row][col] = piece.left
                    board[row][col+1]=piece.right
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card4):
        if row+1==11:
            if board[row][col] == '□□' and board[row + 1][col] == '□□':
                board[row][col] = piece.top
                board[row + 1][col] = piece.below
                return True
            else:
                print("already fill up")
                return False
        else:

            if board[row][col] == '□□' and board[row+1][col] == '□□':
                if board[row+2][col] == '□□':
                    print("empty below")
                    return False
                else:
                    board[row][col] = piece.top
                    board[row+1][col]=piece.below
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card5):
        if row==11:
            if board[row][col] == '□□' and board[row][col+1] == '□□':
                board[row][col] = piece.left
                board[row][col + 1] = piece.right
                return True
            else:
                print("already fill up")
                return False
        else:
            if board[row][col] == '□□' and board[row][col+1] == '□□':
                if board[row+1][col] == '□□' or board[row+1][col+1]=='□□':
                    print("empty below")
                    return False
                else:
                    board[row][col] = piece.left
                    board[row][col+1]=piece.right
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card6):
        if row+1==11:
            if board[row][col] == '□□' and board[row + 1][col] == '□□':
                board[row][col] = piece.top
                board[row + 1][col] = piece.below
                return True
            else:
                print("already fill up")
                return False
        else:

            if board[row][col] == '□□' and board[row+1][col] == '□□':
                if board[row+2][col] == '□□':
                    print("empty below")
                    return False
                else:
                    board[row][col] = piece.top
                    board[row+1][col]=piece.below
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card7):
        if row==11:
            if board[row][col] == '□□' and board[row][col+1] == '□□':
                board[row][col] = piece.left
                board[row][col + 1] = piece.right
                return True
            else:
                print("already fill up")
                return False
        else:
            if board[row][col] == '□□' and board[row][col+1] == '□□':
                if board[row+1][col] == '□□' or board[row+1][col+1]=='□□':
                    print("empty below")
                    return False
                else:
                    board[row][col] = piece.left
                    board[row][col+1]=piece.right
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card8):
        if row+1==11:
            if board[row][col] == '□□' and board[row + 1][col] == '□□':
                board[row][col] = piece.top
                board[row + 1][col] = piece.below
                return True
            else:
                print("already fill up")
                return False
        else:

            if board[row][col] == '□□' and board[row+1][col] == '□□':
                if board[row+2][col] == '□□':
                    print("empty below")
                    return False
                else:
                    board[row][col] = piece.top
                    board[row+1][col]=piece.below
                    return True
            else:
                print("already fill up")
                return False
def is_valid(move,card,cindex):
    if 0 > int(move) or int(move) > COL_COUNT:
        return False
    else:
        if(card is Card.card1):
            if cindex ==7:
                return False
        elif(card is Card.card2):
            if 12-int(move)==11 :
                return False
        elif(card is Card.card3):
            if cindex ==7:
                return False
        elif(card is Card.card4):
            if 12-int(move)==11:
                return False
        elif(card is Card.card5):
            if cindex ==7:
                return False
        elif(card is Card.card6):
            if 12-int(move)==11:
                return False
        elif(card is Card.card7):
            if cindex ==7:
                return False
        elif(card is Card.card8):
            if 12-int(move)==11:
                return False
    return True
# def next_free_row(board,col):
#     for r in range(ROW_COUNT):
#         if board[r][col]==0:
#             return r
#     return
#def print_board(board):
 #   print(np.flip(board,0))
def winning_move(board,user):
    for c in range(ROW_COUNT-3):
        for r in range(COL_COUNT):
            if user==1:
                if board[r][c][1] == 'O' and board[r][c+1][1] == 'O' and board[r][c+2][1] == 'O' and board[r][c+3][1] == 'O':
                    return 1
                elif board[r][c][1] == 'X' and board[r][c+1][1] == 'X' and board[r][c+2][1] == 'X' and board[r][c+3][1] == 'X':
                    return 1
            elif user==2:
                if board[r][c][0]=='W' and board[r][c+1][0]=='W' and board[r][c+2][0]=='W' and board[r][c+3][0]=='W':
                    return 0
                elif board[r][c][0]=='R' and board[r][c+1][0]=='R' and board[r][c+2][0]=='R' and board[r][c+3][0]=='R':
                    return 0


    for c in range(ROW_COUNT):
        for r in range(COL_COUNT-3):
            if str==1:
                if board[r][c][1] == 'O' and board[r+1][c][1] == 'O' and board[r+2][c][1] == 'O' and board[r+3][c][1] == 'O':
                    return 1
                elif board[r][c][1] == 'X' and board[r+1][c][1] == 'X' and board[r+2][c][1] == 'X' and board[r+3][c][1] == 'X':
                    return 1
            elif str==2:

                if board[r][c][0]=='W' and board[r+1][c][0]=='W' and board[r+2][c][0]=='W' and board[r+3][c][0]=='W':
                    return 0
                elif board[r][c][0]=='R' and board[r+1][c][0]=='R' and board[r+2][c][0]=='R' and board[r+3][c][0]=='R':
                    return 0

    for c in range(ROW_COUNT-3):
        for r in range(COL_COUNT-3):
            if str==1:
                if board[r][c][1] == 'O' and board[r+1][c+1][1] == 'O' and board[r+2][c+2][1] == 'O' and board[r+3][c+3][1] == 'O':
                    return 1
                elif board[r][c][1] == 'X' and board[r+1][c+1][1] == 'X' and board[r+2][c+2][1] == 'X' and board[r+3][c+3][1] == 'X':
                    return 1
            elif str==2:
                if board[r][c][0]=='W' and board[r+1][c+1][0]=='W' and board[r+2][c+2][0]=='W' and board[r+3][c+3][0]=='W':
                    return 0
                elif board[r][c][0]=='R' and board[r+1][c+1][0]=='R' and board[r+2][c+2][0]=='R' and board[r+3][c+3][0]=='R':
                    return 0

    for c in range(ROW_COUNT-3):
        for r in range(0,COL_COUNT-2):
            if str == 1:
                if board[r][c][1] == 'O' and board[r - 1][c + 1][1] == 'O' and board[r + 2][c + 2][1] == 'O' and board[r + 3][c + 3][1] == 'O':
                    return 1
                elif board[r][c][1] == 'X' and board[r - 1][c + 1][1] == 'X' and board[r + 2][c + 2][1] == 'X' and board[r + 3][c + 3][1] == 'X':
                    return 1
            elif str==2:
                if board[r][c][0]=='W' and board[r-1][c+1][0]=='W' and board[r+2][c+2][0]=='W' and board[r+3][c+3][0]=='W':
                    return 0
                if board[r][c][0]=='R' and board[r-1][c+1][0]=='R' and board[r+2][c+2][0]=='R' and board[r+3][c+3][0]=='R':
                    return 0



def which_card(move):
    try:
        if (move == '1'):
            card = Card().card1
        elif (move == '2'):
            card = Card().card2
        elif (move == '3'):
            card = Card().card3
        elif (move == '4'):
            card = Card().card4
        elif (move == '5'):
            card = Card().card5
        elif (move == '6'):
            card = Card().card6
        elif (move == '7'):
            card = Card().card7
        elif (move == '8'):
            card = Card().card8
        else:
            print('invalid input:', move)
        return card
    except UnboundLocalError:
        return UnboundLocalError


def which_cindex(move):
    index = 0
    try:
        if (move == 'A'):
            index = 0
        elif (move == 'B'):
            index = 1
        elif (move == 'C'):
            index = 2
        elif (move == 'D'):
            index = 3
        elif (move == 'E'):
            index = 4
        elif (move == 'F'):
            index = 5
        elif (move == 'G'):
            index = 6
        elif (move == 'H'):
            index = 7
        else:
            print('invalid input:', move)
        return index
    except UnboundLocalError:
        return UnboundLocalError
def play(user1,user2,turn,game_over,str):
    while not game_over:
        if turn == 0:
            move = input("Input a slot player {0}: ".format(user1))
            move = move.split(' ')
            if (move[0] == '0'):
                card = which_card(move[1])
                cindex = which_cindex(move[2])
                if card==UnboundLocalError:
                    continue
                elif cindex==UnboundLocalError:
                    continue
                if is_valid(move[3],card,cindex):
                    rindex = 12-int(move[3])
                    drop = drop_piece(board, rindex, cindex, card)
                    if drop==False:
                        print("try again")
                        continue
                    if user1==1:
                        win = winning_move(board, user1)
                        if win==1:
                            print(*board, sep='\n')
                            print("player {0} winning".format(user1))
                            break
                    elif user1==2:
                        win = winning_move(board, user1)
                        if win==0:
                            print(*board, sep='\n')
                            print("player {0} winning".format(user1))
                            break
                else:
                    print("try again")
                    continue

            # else:
            #     pass

            # if is_valid(board,col):
            #     row = next_free_row(board,col)
            #     drop_piece(board,row,col,1)
            #
            #     if winning_move(board,1):
            #         print("1 winning")
            #         game_over =True
            #         sys.exit()

        else:
            move = input("Input a slot player {0}: ".format(user2))
            move = move.split(' ')
            if (move[0] == '0'):

                card = which_card(move[1])
                cindex = which_cindex(move[2])
                if card==UnboundLocalError:
                    continue
                elif cindex==UnboundLocalError:
                    continue

                if is_valid(move[3],card,cindex):
                    rindex = 12-int(move[3])
                    drop= drop_piece(board, rindex, cindex, card)
                    if drop==False:
                        print("try again")
                        continue
                    if user2==1:
                        win = winning_move(board, user2)
                        if win==1:
                            print(*board, sep='\n')
                            print("player {0} winning".format(user2))
                            break
                    elif user2==2:
                        win = winning_move(board, user2)
                        if win==0:
                            print(*board, sep='\n')
                            print("player {0} winning".format(user2))
                            print("*****GAME END*****")
                            break
                else:
                    print("try again")
                    continue
            # else:
            #     pass
            # if is_valid(board,col):
            #     row = next_free_row(board,col)
            #     drop_piece(board,row,col,2)
            #
            #     if winning_move(board,2):
            #         print("2 winning")
            #         game_over =True
            #         break
        print(*board, sep='\n')
        turn +=1
        turn=turn % 2
if __name__ == '__main__':
    print("*****WELCOME TO DOUBLE-CARD GAME*****")
    print("SUPPORT: "
          "W: White "
          "R: Red "
          "X: Solid "
          "O: Hollow")
    str = input("Player 1 will play dots or colors?" )
    if str=="dots":
        print("Player1 choose dots")
        print("Player2 choose colors")
        user1=1
        user2=2
        turn =0
    elif(str=="colors"):
        print("Player1 choose colors")
        print("Player2 choose dots")
        user1=2
        user2=1
        turn =1
    else:
        print("try again")
        str = input("Player 1 will play dots or colors?")
    game_over = False
    board = create_board()
    print(*board, sep='\n')
    play(user1,user2,turn,game_over,str)


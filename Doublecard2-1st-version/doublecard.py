from card import Card
from point import Point
ROW_COUNT = 8
COL_COUNT = 12
DEPTH = 3
search_count=0
cut_count = 0
def create_board():
    board = [['□□' for _ in range(ROW_COUNT)] for _ in range(COL_COUNT)]
    return board
def create_board2():
    point = Point.point
    board2 = [[point for _ in range(ROW_COUNT)] for _ in range(COL_COUNT)]
    for i in range(8):
        point=[0,i+1]
        board2[11][i] = point
    for i in range(8):
        point=[0,11+i]
        board2[10][i] = point
    for i in range(8):
        point=[0,21+i]
        board2[9][i] = point
    for i in range(8):
        point=[0,31+i]
        board2[8][i] = point
    for i in range(8):
        point=[0,41+i]
        board2[7][i] = point
    for i in range(8):
        point=[0,51+i]
        board2[6][i] = point
    for i in range(8):
        point=[0,i+61]
        board2[5][i] = point
    for i in range(8):
        point=[0,i+71]
        board2[4][i] = point
    for i in range(8):
        point=[0,i+81]
        board2[3][i] = point
    for i in range(8):
        point=[0,i+91]
        board2[2][i] = point
    for i in range(8):
        point=[0,i+101]
        board2[1][i] = point
    for i in range(8):
        point=[0,i+111]
        board2[0][i] = point
    return board2
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
def dropindex(cindex,rindex,card):
    if (card is Card.card1):
        nextcindex = cindex+1
        nextrindex = rindex
    elif(card is Card.card2):
        nextcindex = cindex
        nextrindex = rindex-1
    elif(card is Card.card3):
        nextcindex = cindex+1
        nextrindex = rindex
    elif(card is Card.card4):
        nextcindex = cindex
        nextrindex = rindex-1
    elif(card is Card.card5):
        nextcindex = cindex+1
        nextrindex = rindex
    elif(card is Card.card6):
        nextcindex = cindex
        nextrindex = rindex-1
    elif(card is Card.card7):
        nextcindex = cindex+1
        nextrindex = rindex
    elif(card is Card.card8):
        nextcindex = cindex
        nextrindex = rindex-1
    return nextcindex,nextrindex
def cardinformation(move,cindex,rindex,card):
    if (card is Card.card1):
        nextcindex = cindex+1
        nextrindex = rindex
        move.append(nextcindex)
        move.append(nextrindex)
    elif(card is Card.card2):
        nextcindex = cindex
        nextrindex = rindex-1
        move.append(nextcindex)
        move.append(nextrindex)
    elif(card is Card.card3):
        nextcindex = cindex+1
        nextrindex = rindex
        move.append(nextcindex)
        move.append(nextrindex)
    elif(card is Card.card4):
        nextcindex = cindex
        nextrindex = rindex-1
        move.append(nextcindex)
        move.append(nextrindex)
    elif(card is Card.card5):
        nextcindex = cindex+1
        nextrindex = rindex
        move.append(nextcindex)
        move.append(nextrindex)
    elif(card is Card.card6):
        nextcindex = cindex
        nextrindex = rindex-1
        move.append(nextcindex)
        move.append(nextrindex)
    elif(card is Card.card7):
        nextcindex = cindex+1
        nextrindex = rindex
        move.append(nextcindex)
        move.append(nextrindex)
    elif(card is Card.card8):
        nextcindex = cindex
        nextrindex = rindex-1
        move.append(nextcindex)
        move.append(nextrindex)
    return move
def is_valid(move,card,cindex):
    if 0 > int(move) or int(move) > COL_COUNT:
        return False
    else:
        if(card is Card.card1):
            if cindex ==7:
                return False
        elif(card is Card.card2):
            if 12-int(move)==0 :
                return False
        elif(card is Card.card3):
            if cindex ==7:
                return False
        elif(card is Card.card4):
            if 12-int(move)==0:
                return False
        elif(card is Card.card5):
            if cindex ==7:
                return False
        elif(card is Card.card6):
            if 12-int(move)==0:
                return False
        elif(card is Card.card7):
            if cindex ==7:
                return False
        elif(card is Card.card8):
            if 12-int(move)==0:
                return False
    return True
def drop_piece(board,row,col,piece):
    if(piece is Card.card1):
        if row==11:
            if board[row][col] == '□□' and board[row][col+1] == '□□':
                board[row][col] = piece.left[0]
                board[row][col + 1] = piece.right[0]
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
                    board[row][col] = piece.left[0]
                    board[row][col+1]=piece.right[0]
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card2):
        if row==11:
            if board[row][col] == '□□' and board[row - 1][col] == '□□':
                board[row][col] = piece.below[0]
                board[row - 1][col] = piece.top[0]
                return True
            else:
                print("already fill up")
                return False
        else:

            if board[row][col] == '□□' and board[row-1][col] == '□□':
                if board[row+1][col] == '□□':
                    print("empty below")
                    return False
                else:
                    board[row][col] = piece.below[0]
                    board[row-1][col]=piece.top[0]
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card3):
        if row==11:
            if board[row][col] == '□□' and board[row][col+1] == '□□':
                board[row][col] = piece.left[0]
                board[row][col + 1] = piece.right[0]
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
                    board[row][col] = piece.left[0]
                    board[row][col+1]=piece.right[0]
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card4):
        if row==11:
            if board[row][col] == '□□' and board[row - 1][col] == '□□':
                board[row][col] = piece.below[0]
                board[row - 1][col] = piece.top[0]
                return True
            else:
                print("already fill up")
                return False
        else:

            if board[row][col] == '□□' and board[row-1][col] == '□□':
                if board[row+1][col] == '□□':
                    print("empty below")
                    return False
                else:
                    board[row][col] = piece.below[0]
                    board[row-1][col]=piece.top[0]
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card5):
        if row==11:
            if board[row][col] == '□□' and board[row][col+1] == '□□':
                board[row][col] = piece.left[0]
                board[row][col + 1] = piece.right[0]
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
                    board[row][col] = piece.left[0]
                    board[row][col+1]=piece.right[0]
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card6):
        if row==11:
            if board[row][col] == '□□' and board[row - 1][col] == '□□':
                board[row][col] = piece.below[0]
                board[row - 1][col] = piece.top[0]
                return True
            else:
                print("already fill up")
                return False
        else:

            if board[row][col] == '□□' and board[row-1][col] == '□□':
                if board[row+1][col] == '□□':
                    print("empty below")
                    return False
                else:
                    board[row][col] = piece.below[0]
                    board[row-1][col]=piece.top[0]
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card7):
        if row==11:
            if board[row][col] == '□□' and board[row][col+1] == '□□':
                board[row][col] = piece.left[0]
                board[row][col + 1] = piece.right[0]
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
                    board[row][col] = piece.left[0]
                    board[row][col+1]=piece.right[0]
                    return True
            else:
                print("already fill up")
                return False
    elif(piece is Card.card8):
        if row==11:
            if board[row][col] == '□□' and board[row - 1][col] == '□□':
                board[row][col] = piece.below[0]
                board[row - 1][col] = piece.top[0]
                return True
            else:
                print("already fill up")
                return False
        else:

            if board[row][col] == '□□' and board[row-1][col] == '□□':
                if board[row+1][col] == '□□':
                    print("empty below")
                    return False
                else:
                    board[row][col] = piece.below[0]
                    board[row-1][col]=piece.top[0]
                    return True
            else:
                print("already fill up")
                return False

def drop_piece2(board2,row,col,piece):
    if (piece is Card.card1):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 1
        board2[xindex2][yindex2][0] = 1
    elif(piece is Card.card2):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 1
        board2[xindex2][yindex2][0] = 1
    elif(piece is Card.card3):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 1
        board2[xindex2][yindex2][0] = 1
    elif(piece is Card.card4):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 1
        board2[xindex2][yindex2][0] = 1
    elif(piece is Card.card5):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 1
        board2[xindex2][yindex2][0] = 1
    elif(piece is Card.card6):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 1
        board2[xindex2][yindex2][0] = 1
    elif(piece is Card.card7):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 1
        board2[xindex2][yindex2][0] = 1
    elif(piece is Card.card8):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 1
        board2[xindex2][yindex2][0] = 1



def drop_piece3(board,row,col,piece):
    if piece is Card.card2 or piece is Card.card4 or piece is Card.card6 or piece is Card.card8:
        board[row][col] = piece.below
        board[row - 1][col] = piece.top
    else:
        board[row][col] = piece.left
        board[row][col + 1] = piece.right





def blanklist(board, piece):
    candidate = []
    for row in range(0, COL_COUNT):
        for col in range(0, ROW_COUNT):
            if (piece is Card.card1):
                if col == 7:
                    continue
                if row == 11:
                    if board[row][col] == '□□' and board[row][col + 1] == '□□':
                        candidate.append([row, col, piece])
                    else:
                        continue
                else:
                    if board[row][col] == '□□' and board[row][col + 1] == '□□':
                        if board[row + 1][col] == '□□' or board[row + 1][col + 1] == '□□':
                            continue
                        else:
                            candidate.append([row, col, piece])
                    else:
                        continue
            elif (piece is Card.card2):
                if row == 0:
                    continue
                if row == 11:
                    if board[row][col] == '□□' and board[row - 1][col] == '□□':
                        candidate.append([row, col, piece])
                    else:
                        continue
                else:

                    if board[row][col] == '□□' and board[row - 1][col] == '□□':
                        if board[row + 1][col] == '□□':
                            continue
                        else:
                            candidate.append([row, col, piece])
                    else:
                        continue
            elif (piece is Card.card3):
                if col == 7:
                    continue
                if row == 11:
                    if board[row][col] == '□□' and board[row][col + 1] == '□□':
                        candidate.append([row, col, piece])
                    else:
                        continue
                else:
                    if board[row][col] == '□□' and board[row][col + 1] == '□□':
                        if board[row + 1][col] == '□□' or board[row + 1][col + 1] == '□□':
                            continue
                        else:

                            candidate.append([row, col, piece])
                    else:
                        continue
            elif (piece is Card.card4):
                if row == 0:
                    continue
                if row == 11:
                    if board[row][col] == '□□' and board[row - 1][col] == '□□':

                        candidate.append([row, col, piece])
                    else:
                        continue
                else:

                    if board[row][col] == '□□' and board[row - 1][col] == '□□':
                        if board[row + 1][col] == '□□':
                            continue
                        else:

                            candidate.append([row, col, piece])
                    else:
                        continue
            elif (piece is Card.card5):
                if col == 7:
                    continue
                if row == 11:
                    if board[row][col] == '□□' and board[row][col + 1] == '□□':

                        candidate.append([row, col, piece])
                    else:
                        continue
                else:
                    if board[row][col] == '□□' and board[row][col + 1] == '□□':
                        if board[row + 1][col] == '□□' or board[row + 1][col + 1] == '□□':
                            continue
                        else:

                            candidate.append([row, col, piece])
                    else:
                        continue
            elif (piece is Card.card6):
                if row == 0:
                    continue
                if row == 11:
                    if board[row][col] == '□□' and board[row - 1][col] == '□□':
                        candidate.append([row, col, piece])
                    else:
                        continue
                else:

                    if board[row][col] == '□□' and board[row - 1][col] == '□□':
                        if board[row + 1][col] == '□□':
                            continue
                        else:

                            candidate.append([row, col, piece])
                    else:
                        continue
            elif (piece is Card.card7):
                if col == 7:
                    continue
                if row == 11:
                    if board[row][col] == '□□' and board[row][col + 1] == '□□':

                        candidate.append([row, col, piece])
                    else:
                        continue
                else:
                    if board[row][col] == '□□' and board[row][col + 1] == '□□':
                        if board[row + 1][col] == '□□' or board[row + 1][col + 1] == '□□':
                            continue
                        else:

                            candidate.append([row, col, piece])
                    else:
                        continue
            elif (piece is Card.card8):
                if row == 0:
                    continue
                if row == 11:
                    if board[row][col] == '□□' and board[row - 1][col] == '□□':

                        candidate.append([row, col, piece])
                    else:
                        continue
                else:

                    if board[row][col] == '□□' and board[row - 1][col] == '□□':
                        if board[row + 1][col] == '□□':
                            continue
                        else:

                            candidate.append([row, col, piece])
                    else:
                        continue
    return candidate

def remove_piece(board,row,col,piece):
    if piece is Card.card2 or piece is Card.card4 or piece is Card.card6 or piece is Card.card8:
        board[row][col]='□□'
        board[row-1][col]='□□'
    else:
        board[row][col]='□□'
        board[row][col+1]='□□'

def remove_piece3(board3,row,col,piece):
    if piece is Card.card2 or piece is Card.card4 or piece is Card.card6 or piece is Card.card8:
        board3[row][col]='□□'
        board3[row-1][col]='□□'
    else:
        board3[row][col]='□□'
        board3[row][col+1]='□□'

def remove_piece2(board2,row,col,piece):
    if (piece is Card.card1):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 0
        board2[xindex2][yindex2][0] = 0
    elif(piece is Card.card2):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 0
        board2[xindex2][yindex2][0] = 0
    elif(piece is Card.card3):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 0
        board2[xindex2][yindex2][0] = 0
    elif(piece is Card.card4):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 0
        board2[xindex2][yindex2][0] = 0
    elif(piece is Card.card5):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 0
        board2[xindex2][yindex2][0] = 0
    elif(piece is Card.card6):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 0
        board2[xindex2][yindex2][0] = 0
    elif(piece is Card.card7):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 0
        board2[xindex2][yindex2][0] = 0
    elif(piece is Card.card8):
        yindex2, xindex2 = dropindex(col, row, piece)
        board2[row][col][0] = 0
        board2[xindex2][yindex2][0] = 0

def winning_move(board,user1,user2):
    for c in range(ROW_COUNT-3):
        for r in range(COL_COUNT):
            if user1=='dots' and user2=='colors':
                if board[r][c][1]=='O'and board[r][c+1][1]=='O' and board[r][c+2][1] == 'O' and board[r][c+3][1] =='O':
                    return 1
                elif board[r][c][1] =='X' and board[r][c+1][1]=='X' and board[r][c+2][1]=='X'and board[r][c+3][1]=='X':
                    return 1
            elif user1=='colors' and user2=='dots':
                if board[r][c][0]=='W' and board[r][c+1][0]=='W' and board[r][c+2][0]=='W' and board[r][c+3][0]=='W':
                    return 0
                elif board[r][c][0]=='R' and board[r][c+1][0]=='R' and board[r][c+2][0]=='R' and board[r][c+3][0]=='R':
                    return 0


    for c in range(ROW_COUNT):
        for r in range(COL_COUNT-3):
            if user1=='dots' and user2=='colors':
                if board[r][c][1] =='O'and board[r+1][c][1] =='O'and board[r+2][c][1] =='O' and board[r+3][c][1] == 'O':
                    return 1
                elif board[r][c][1] =='X'and board[r+1][c][1] =='X'and board[r+2][c][1]=='X' and board[r+3][c][1]== 'X':
                    return 1
            elif user1 == 'colors' and user2 == 'dots':
                if board[r][c][0]=='W' and board[r+1][c][0]=='W' and board[r+2][c][0]=='W' and board[r+3][c][0]=='W':
                    return 0
                elif board[r][c][0]=='R' and board[r+1][c][0]=='R' and board[r+2][c][0]=='R' and board[r+3][c][0]=='R':
                    return 0

    for c in range(ROW_COUNT-3):
        for r in range(3,COL_COUNT):
            if user1=='dots' and user2=='colors':
                if board[r][c][1]=='O'and board[r-1][c+1][1]=='O'and board[r-2][c+2][1]=='O'and board[r-3][c+3][1]=='O':
                    return 1
                elif board[r][c][1]=='X'and board[r-1][c+1][1]=='X'and board[r-2][c+2][1]=='X'and board[r-3][c+3][1]=='X':
                    return 1
            elif user1 == 'colors' and user2 == 'dots':
                if board[r][c][0]=='W' and board[r-1][c+1][0]=='W' and board[r-2][c+2][0]=='W' and board[r-3][c+3][0]=='W':
                    return 0
                elif board[r][c][0]=='R' and board[r-1][c+1][0]=='R' and board[r-2][c+2][0]=='R' and board[r-3][c+3][0]=='R':
                    return 0

    for c in range(ROW_COUNT-3):
        for r in range(COL_COUNT-3):
            if user1=='dots' and user2=='colors':
                if board[r][c][1] =='O'and board[r+1][c+1][1]=='O'and board[r+2][c +2][1]=='O'and board[r+3][c+3][1]=='O':
                    return 1
                elif board[r][c][1] =='X'and board[r+1][c+1][1] =='X'and board[r+2][c+2][1]=='X'and board[r+3][c+3][1]=='X':
                    return 1
            elif user1 == 'colors' and user2 == 'dots':
                if board[r][c][0]=='W' and board[r+1][c+1][0]=='W' and board[r+2][c+2][0]=='W' and board[r+3][c+3][0]=='W':
                    return 0
                if board[r][c][0]=='R' and board[r+1][c+1][0]=='R' and board[r+2][c+2][0]=='R' and board[r+3][c+3][0]=='R':
                    return 0
#   ##############################################################################3

def evaluation(board,board2,board3,player):
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    for r in range(COL_COUNT):
        for c in range(ROW_COUNT):
            if board3[r][c][1]=='R':
                if board3[r][c][2]=='X':
                    if board2[r][c][0]==1:
                        sum1 += board2[r][c][1]
                elif board3[r][c][2]=='O':
                    if board2[r][c][0]==1:
                        sum2 += board2[r][c][1]
            elif board3[r][c][1]=='W':
                if board3[r][c][2]=='O':
                    if board2[r][c][0]==1:
                        sum3 += board2[r][c][1]
                elif board3[r][c][2]=='X':
                    if board2[r][c][0]==1:
                        sum4 += board2[r][c][1]
    evalue = sum3+3*sum4-2*sum1-1.5*sum2
    return  evalue
def SwitchPlayer(player):
    if player == 'dots':
        nextplayer = 'colors'
    else:
        nextplayer = 'dots'
    return nextplayer
def SwitchPlayer2(player):
    if player =='AI':
        nextplayer = 'human'
    else:
        nextplayer = 'AI'
    return nextplayer
def minimax(board,board2,depth,dotscolor):
    values = []
    maxvalues = []
    coordinate = []
    value = -1000000000
    global search_count
    if dotscolor=='colors':
        list = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in list:
            piece = which_card(i)
            candidate = blanklist(board, piece)
            for j in range(len(candidate)):
                search_count += 1
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                value=max(value,minfunction(board, board2, depth - 1, dotscolor))
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                maxvalues.append(value)
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])

            else:
                continue

    elif dotscolor=='dots':
        list = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in list:
            piece = which_card(i)
            candidate = blanklist(board, piece)
            for j in range(len(candidate)):
                search_count += 1
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                value=max(value,minfunction(board, board2, depth - 1, dotscolor))
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                maxvalues.append(value)
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])

            else:
                continue
    return coordinate[0], coordinate[1], coordinate[2]

def maxfunction(board,board2,depth,player) :
    opponent = SwitchPlayer(player)
    value = -1000000000
    if (depth == 0):
        return evaluation(board,board2,board3,opponent)
    list = ['1', '2', '3', '4', '5', '6', '7', '8']
    for i in list:
        piece = which_card(i)
        candidate = blanklist(board, piece)
        for j in range(len(candidate)):
            global search_count
            search_count += 1
            drop_piece(board,candidate[j][0],candidate[j][1],candidate[j][2])
            drop_piece2(board2,candidate[j][0],candidate[j][1],candidate[j][2])
            drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            bestvalue = minfunction(board, board2,depth - 1,opponent)
            remove_piece(board,candidate[j][0],candidate[j][1],candidate[j][2])
            remove_piece2(board2,candidate[j][0],candidate[j][1],candidate[j][2])
            remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            if bestvalue>value:
                value = bestvalue
    return value
def minfunction(board,board2,depth,player):
    opponent = SwitchPlayer(player)
    value = 1000000000
    if (depth == 0):
        return evaluation(board, board2,board3,opponent)
    list = ['1', '2', '3', '4', '5', '6', '7', '8']
    for i in list:
        piece = which_card(i)
        candidate = blanklist(board, piece)
        for j in range(len(candidate)):
            global search_count
            search_count += 1
            drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
            drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
            drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            bestvalue = maxfunction(board, board2, depth - 1, opponent)
            remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
            remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
            remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            if bestvalue < value:
                value = bestvalue
    return value




def alphabetapruning(board,board2,depth,alpha,beta,dotscolor):
    values = []
    maxvalues = []
    coordinate = []
    value = -1000000000
    global search_count
    if dotscolor=='colors':
        list = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in list:
            piece = which_card(i)
            candidate = blanklist(board, piece)
            for j in range(len(candidate)):
                search_count += 1
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                value=max(value,alphabetapruningminfunction(board, board2, depth - 1,alpha,beta, dotscolor))
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                maxvalues.append(value)
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])

            else:
                continue

    elif dotscolor=='dots':
        list = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in list:
            piece = which_card(i)
            candidate = blanklist(board, piece)
            for j in range(len(candidate)):
                search_count += 1
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                value=max(value,alphabetapruningminfunction(board, board2, depth - 1,alpha,beta, dotscolor))
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                maxvalues.append(value)
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])

            else:
                continue
    return coordinate[0], coordinate[1], coordinate[2]


def alphabetapruningmaxfunction(board,board2,depth,alpha,beta,player) :
    opponent = SwitchPlayer(player)
    value = -1000000000
    if (depth == 0):
        return evaluation(board,board2,board3,opponent)
    list = ['1', '2', '3', '4', '5', '6', '7', '8']
    for i in list:
        piece = which_card(i)
        candidate = blanklist(board, piece)
        for j in range(len(candidate)):
            global search_count
            search_count += 1
            drop_piece(board,candidate[j][0],candidate[j][1],candidate[j][2])
            drop_piece2(board2,candidate[j][0],candidate[j][1],candidate[j][2])
            drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            value = max(value,alphabetapruningminfunction(board, board2,depth - 1,alpha,beta,opponent))
            remove_piece(board,candidate[j][0],candidate[j][1],candidate[j][2])
            remove_piece2(board2,candidate[j][0],candidate[j][1],candidate[j][2])
            remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            alpha = max(alpha, value)
            if value >= beta:
                global cut_count
                cut_count+=1
                return value
    return value
def alphabetapruningminfunction(board,board2,depth,alpha,beta,player):
    opponent = SwitchPlayer(player)
    value = 1000000000
    if (depth == 0):
        return evaluation(board, board2,board3,opponent)
    list = ['1', '2', '3', '4', '5', '6', '7', '8']
    for i in list:
        piece = which_card(i)
        candidate = blanklist(board, piece)
        for j in range(len(candidate)):
            global search_count
            search_count += 1
            drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
            drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
            drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            value = min(value,alphabetapruningmaxfunction(board, board2, depth - 1,alpha,beta,opponent))
            remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
            remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
            remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            beta = min(beta, value)
            if value <= alpha:
                global cut_count
                cut_count+=1
                return value
    return value

#¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def play(user1,user2,turn,game_over,aiorhuman,dotscolor):
    firstuser=[]
    while not game_over:
        if turn==0:
            if aiorhuman=='AI':
                move=['','','','']
                usercmd= input('Does AI activate alpha-beta? (y/n) : ')
                if usercmd.lower().startswith('y'):
                    coordinate = alphabetapruning(board,board2, DEPTH, -99999999, 99999999,dotscolor)
                else:
                    coordinate = minimax(board,board2,DEPTH,dotscolor)

                drop = drop_piece(board, coordinate[0], coordinate[1], coordinate[2])
                if drop:
                    transfermove = cardinformation(move, coordinate[1], coordinate[0], coordinate[2])
                    firstuser.append(transfermove)
                    yindex2, xindex2 = dropindex(coordinate[1], coordinate[0], coordinate[2])
                    board2[coordinate[0]][coordinate[1]][0] = 1
                    board2[xindex2][yindex2][0] = 1
                    drop_piece3(board3, coordinate[0], coordinate[1], coordinate[2])
                    # print("purning：" + str(cut_count))
                    print("searching：")
                    print(search_count)
                    print("purning：")
                    print(cut_count)
                    if user1 == 'dots':
                        win1 = winning_move(board, user1, user2)
                        win2 = winning_move(board, user2, user1)
                        if win1 == 1:
                            print(*board, sep='\n')
                            print("{0} winning".format('AI'))
                            print("*****GAME END*****")
                            break
                        elif win2 == 0:
                            print(*board, sep='\n')
                            print("{0} winning".format('human'))
                            print("*****GAME END*****")
                            break
                    elif user1 == 'colors':
                        win1 = winning_move(board, user2, user1)
                        win2 = winning_move(board, user1, user2)
                        if win1 == 1:
                            print(*board, sep='\n')
                            print("player {0} winning".format('AI'))
                            print("*****GAME END*****")
                            break
                        elif win2 == 0:
                            print(*board, sep='\n')
                            print("{0} winning".format('human'))
                            print("*****GAME END*****")
                            break

            else:
                move = input("Input a slot player {0}: ".format(aiorhuman))
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
                            print("drop failure")
                            print("try again")
                            continue
                        elif drop==True:
                            drop_piece3(board3, rindex, cindex, card)
                            transfermove = cardinformation(move,cindex,rindex,card)
                            firstuser.append(transfermove)
                            yindex2,xindex2 = dropindex(cindex,rindex,card)
                            board2[rindex][cindex][0]=1
                            board2[xindex2][yindex2][0] = 1
                        if user1=='dots':
                            win1 = winning_move(board, user1,user2)
                            win2 = winning_move(board, user2,user1)
                            if win1==1:
                                print(*board, sep='\n')
                                print("{0} winning".format('human'))
                                print("*****GAME END*****")
                                break
                            elif win2==0:
                                print(*board, sep='\n')
                                print("{0} winning".format('AI'))
                                print("*****GAME END*****")
                                break
                        elif user1=='colors':
                            win1 = winning_move(board, user2,user1)
                            win2 = winning_move(board, user1, user2)
                            if win1==1:
                                print(*board, sep='\n')
                                print("{0} winning".format('human'))
                                print("*****GAME END*****")
                                break
                            elif win2==0:
                                print(*board, sep='\n')
                                print("{0} winning".format('AI'))
                                print("*****GAME END*****")
                                break
                    else:
                        print("not valid")
                        print("try again")
                        continue
                else:
                    print("invalid input")
                    print("try again")
                    continue
        else:
            if aiorhuman=='AI':
                move = ['', '', '', '']
                usercmd= input('Does AI activate alpha-beta? (y/n) : ')
                if usercmd.lower().startswith('y'):
                    coordinate = alphabetapruning(board,board2,DEPTH, -99999999, 99999999,dotscolor)
                else:
                    coordinate = minimax(board,board2,DEPTH,dotscolor)
                drop = drop_piece(board, coordinate[0], coordinate[1], coordinate[2])
                if drop:
                    transfermove = cardinformation(move, coordinate[1], coordinate[0], coordinate[2])
                    firstuser.append(transfermove)
                    yindex2, xindex2 = dropindex(coordinate[1], coordinate[0], coordinate[2])
                    board2[coordinate[0]][coordinate[1]][0] = 1
                    board2[xindex2][yindex2][0] = 1
                    drop_piece3(board3, coordinate[0], coordinate[1], coordinate[2])
                    print("searching：", end='')
                    print(search_count)
                    print("purning：", end='')
                    print(cut_count)
                    if user2 == 'dots':
                        win1 = winning_move(board, user1, user2)
                        win2 = winning_move(board, user2, user1)
                        if win1 == 0:
                            print(*board, sep='\n')
                            print("{0} winning".format('AI'))
                            print("*****GAME END*****")
                            break
                        elif win2 == 1:
                            print(*board, sep='\n')
                            print("{0} winning".format('human'))
                            print("*****GAME END*****")
                            break
                    elif user2 == 'colors':
                        win1 = winning_move(board, user2, user1)
                        win2 = winning_move(board, user1, user2)
                        if win1 == 0:
                            print(*board, sep='\n')
                            print("player {0} winning".format('AI'))
                            print("*****GAME END*****")
                            break
                        elif win2 == 1:
                            print(*board, sep='\n')
                            print("player {0} winning".format('human'))
                            print("*****GAME END*****")
                            break
                # print("purning：" + str(cut_count))

            else:
                move = input("Input a slot player {0}: ".format(aiorhuman))
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
                            print("drop failure")
                            print("try again")
                            continue
                        elif drop==True:
                            drop_piece3(board3, rindex, cindex, card)
                            transfermove = cardinformation(move, cindex, rindex, card)
                            firstuser.append(transfermove)
                            yindex2, xindex2 = dropindex(cindex, rindex, card)
                            board2[rindex][cindex][0] = 1
                            board2[xindex2][yindex2][0] = 1
                        if user2=='dots':
                            win1 = winning_move(board, user1,user2)
                            win2 = winning_move(board, user2, user1)
                            if win1==0:
                                print(*board, sep='\n')
                                print("{0} winning".format('human'))
                                print("*****GAME END*****")
                                break
                            elif win2==1:
                                print(*board, sep='\n')
                                print("{0} winning".format('AI'))
                                print("*****GAME END*****")
                                break
                        elif user2=='colors':
                            win1 = winning_move(board, user2,user1)
                            win2 = winning_move(board, user1,user2)
                            if win1==0:
                                print(*board, sep='\n')
                                print("{0} winning".format('human'))
                                print("*****GAME END*****")
                                break
                            elif win2==1:
                                print(*board, sep='\n')
                                print("{0} winning".format('AI'))
                                print("*****GAME END*****")
                                break
                    else:
                        print("not valid")
                        print("try again")
                        continue
                else:
                    print("invalid input")
                    print("try again")
                    continue

        print(*board, sep='\n')
        turn +=1
        turn=turn % 2
        aiorhuman= SwitchPlayer2(aiorhuman)
        dotscolor =SwitchPlayer(dotscolor)
        print("Overall steps: ",end="")
        print(len(firstuser))
def PlayerGoesFirst():
    print('Does AI play first? (y/n) : ', end="")
    return input().lower().startswith('y')
def PlayerOption(aiorhuman):
    while True:
        str = input("{0} will play dots or colors?".format(aiorhuman))
        if str=="dots":
            print("{0} choose dots".format(aiorhuman))
            user1='dots'
            user2='colors'
            dotscolor ='dots'
            turn = 0
            return user1, user2,turn, dotscolor
        elif(str=="colors"):
            print("{0} choose colors".format(aiorhuman))
            user1='colors'
            user2='dots'
            dotscolor ='colors'
            turn = 1
            return user1, user2, turn,dotscolor
        else:
            print("try again")
            continue
if __name__ == '__main__':
    print("*****WELCOME TO DOUBLE-CARD GAME*****")
    print("SUPPORT: "
          "W: White "
          "R: Red "
          "X: Solid "
          "O: Hollow")
    AIORHUMAN = 'AI'
    if PlayerGoesFirst():
        user1,user2,turn,dotscolor = PlayerOption(AIORHUMAN)
    else:
        AIORHUMAN = 'human'
        user1,user2,turn,dotscolor = PlayerOption(AIORHUMAN)
    game_over = False
    board = create_board()
    board2 = create_board2()
    board3 = create_board()
    print(*board, sep='\n')
    play(user1,user2,turn,game_over,AIORHUMAN,dotscolor)

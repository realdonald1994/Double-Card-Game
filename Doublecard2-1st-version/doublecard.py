from card import Card
from point import Point
ROW_COUNT = 8
COL_COUNT = 12
DEPTH = 2
search_count=0
cut_count = 0
en_count =0
REGUALR_GAME = 4
RECYCLING_GAME=60

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

def return_card(piece):
    str=''
    if (piece is Card.card1):
        str = '1'
    elif (piece is Card.card2):
        str = '2'
    elif (piece is Card.card3):
        str = '3'
    elif (piece is Card.card4):
        str = '4'
    elif (piece is Card.card5):
        str = '5'
    elif (piece is Card.card6):
        str = '6'
    elif (piece is Card.card7):
        str = '7'
    elif (piece is Card.card8):
        str = '8'
    return str

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

def returnindex(colindex):
    str=''
    if (colindex == 0):
        str = 'A'
    elif (colindex ==1 ):
        str = 'B'
    elif (colindex == 2):
        str = 'C'
    elif (colindex == 3):
        str = 'D'
    elif (colindex ==4 ):
        str = 'E'
    elif (colindex == 5):
        str = 'F'
    elif (colindex == 6):
        str = 'G'
    elif (colindex == 7):
        str = 'H'
    return str

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

def is_valid2(move1,move2):
    if 0 > int(move1) or int(move1) > COL_COUNT or 0 > int(move2) or int(move2)> COL_COUNT:
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



def drop_piece3(board3,row,col,piece):
    if piece is Card.card2 or piece is Card.card4 or piece is Card.card6 or piece is Card.card8:
        board3[row][col] = piece.below
        board3[row - 1][col] = piece.top
    else:
        board3[row][col] = piece.left
        board3[row][col + 1] = piece.right


def drop_recycling(board,board2,board3,row,col,row2,col2,piece):
    if piece is Card.card1 or piece is Card.card3 or piece is Card.card5 or piece is Card.card7:
        board3[row][col] = piece.left
        board3[row2][col2] = piece.right
        board[row][col] = piece.left[0]
        board[row2][col2] = piece.right[0]
        board2[row][col][0] = 1
        board2[row2][col2][0] = 1
    else:
        board3[row][col] = piece.top
        board3[row2][col2] = piece.below
        board[row][col] = piece.top[0]
        board[row2][col2] = piece.below[0]
        board2[row][col][0] = 1
        board2[row2][col2][0] = 1


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

def remove(board,board2,board3,raw1,col1,raw2,col2):
    if col1==col2:
        col=col1
        raw=max(raw1,raw2)
        turn =1
    else:
        raw=raw1
        col=min(col1,col2)
        turn=2

    if turn==1:
        if raw ==1:
            board[raw1][col1] = '□□'
            board[raw2][col2] = '□□'
            board3[raw1][col1] = '□□'
            board3[raw2][col2] = '□□'
            board2[raw1][col1][0]=0
            board2[raw2][col2][0] = 0
        else:

            if board[raw-2][col]=='□□':
                board[raw1][col1] = '□□'
                board[raw2][col2] = '□□'
                board3[raw1][col1] = '□□'
                board3[raw2][col2] = '□□'
                board2[raw1][col1][0] = 0
                board2[raw2][col2][0] = 0
                return True
            else:
                return False
    elif turn==2:
        if raw==0:
            board[raw1][col1] = '□□'
            board[raw2][col2] = '□□'
            board3[raw1][col1] = '□□'
            board3[raw2][col2] = '□□'
            board2[raw1][col1][0]=0
            board2[raw2][col2][0] = 0
        else:

            if board[raw-1][col]=='□□' and board[raw-1][col+1]=='□□':
                board[raw1][col1] = '□□'
                board[raw2][col2] = '□□'
                board3[raw1][col1] = '□□'
                board3[raw2][col2] = '□□'
                board2[raw1][col1][0] = 0
                board2[raw2][col2][0] = 0
                return True
            else:
                return False

def remove_recyclingpiece(board3):
    candidate = []
    for row in range(0, COL_COUNT):
        for col in range(0, ROW_COUNT-1):
            if board3[row][col] !='□□' and board3[row][col+1]!='□□':
                if board3[row][col][3] is board3[row][col+1][3]:
                    piece = board3[row][col][3]
                    if row==0:
                        row2 = row
                        col2 =col+1
                        candidate.append([row, col,row2,col2, piece])
                    else:
                        if board3[row - 1][col] == '□□' and board3[row - 1][col + 1] == '□□':
                            row2 = row
                            col2 = col + 1
                            candidate.append([row, col, row2,col2, piece])
                        else:
                            continue
                else:
                    continue
    for row in range(0, COL_COUNT - 1):
        for col in range(0, ROW_COUNT):
            if board3[row][col] !='□□' and board3[row+1][col]!='□□':
                if board3[row][col][3] is board3[row+1][col][3]:
                    piece = board3[row][col][3]
                    if row ==0:
                        row2 = row+1
                        col2 = col
                        candidate.append([row, col,row2,col2, piece])
                    else:
                        if board3[row-1][col]=='□□':
                            row2 = row + 1
                            col2 = col
                            candidate.append([row, col,row2,col2,piece])
                        else:
                            continue
                else:
                    continue
            else:
                continue
    return candidate

def real_removerecycle(board,board2,board3,row,col,row2,col2):

    board3[row][col] = '□□'
    board3[row2][col2] = '□□'
    board[row][col] = '□□'
    board[row2][col2] = '□□'
    board2[row][col][0] = 0
    board2[row2][col2][0] = 0





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
    global en_count
    en_count+=1
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
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def lastminmax(board,board2,depth,dotscolor,list1):
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
                recycling_list = []
                recycling_list.append('0')
                recycling_list.append(return_card(candidate[j][2]))
                recycling_list.append(returnindex(candidate[j][1]))
                recycling_list.append(str(12 - candidate[j][0]).strip())
                transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                list1.append(transfermove)
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                level2value = lastminfunction(board, board2, depth - 1, dotscolor,list1)
                value=max(value,level2value)
                maxvalues.append(level2value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])
                coordinate.append(values[i][0])
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
                level2value = lastminfunction(board, board2, depth - 1, dotscolor,list1)
                value=max(value,level2value)
                maxvalues.append(level2value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])
                coordinate.append(values[i][0])
            else:
                continue
    return coordinate[0], coordinate[1], coordinate[2], coordinate[3],maxvalues
def lastminfunction(board,board2,depth,player,list1):
    opponent = SwitchPlayer(player)
    value = 1000000000
    if (depth == 0):
        return evaluation(board, board2, board3, opponent)
    candidate1 = remove_recyclingpiece(board3)
    for k in range(len(candidate1)):
        real_removerecycle(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                           candidate1[k][3])
        list = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in list:
            piece = which_card(i)
            candidate = blanklist(board, piece)
            for j in range(len(candidate)):
                global search_count
                search_count += 1
                minmaxmove = []
                cardnu = ''
                minmaxmove.append(returnindex(candidate1[k][1]))
                minmaxmove.append(str(12 - candidate1[k][0]).strip())
                minmaxmove.append(returnindex(candidate1[k][3]))
                minmaxmove.append(str(12 - candidate1[k][2]).strip())
                minmaxmove.append(return_card(candidate[j][2]))
                minmaxmove.append(returnindex(candidate[j][1]))
                minmaxmove.append(str(12 - candidate[j][0]).strip())
                cardid = samecard(minmaxmove, candidate1[k][1], candidate1[k][3], list1, cardnu)
                if cardid == return_card(candidate[j][2]):
                    continue
                elif cardid == 'notpass':
                    continue
                elif cardid == '':
                    continue
                elif cardid == "colerror":
                    continue
                recycling_list = []
                recycling_list.append('0')
                recycling_list.append(return_card(candidate[j][2]))
                recycling_list.append(returnindex(candidate[j][1]))
                recycling_list.append(str(12 - candidate[j][0]).strip())
                transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                list1.append(transfermove)
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                bestvalue = maxfunction(board, board2, depth - 1, opponent)
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                if bestvalue < value:
                    value = bestvalue
        drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2], candidate1[k][3],
                       candidate1[k][4])
    return value

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def lastaphabeta(board,board2,depth,alpha,beta,dotscolor,list1):
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
                recycling_list = []
                recycling_list.append('0')
                recycling_list.append(return_card(candidate[j][2]))
                recycling_list.append(returnindex(candidate[j][1]))
                recycling_list.append(str(12 - candidate[j][0]).strip())
                transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0],
                                               candidate[j][2])
                list1.append(transfermove)
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                level2value = lastminaphabeta(board, board2, depth - 1, alpha, beta, dotscolor,list1)
                value=max(value,level2value)
                maxvalues.append(level2value)
                alpha = max(alpha, value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])
                coordinate.append(values[i][0])

            else:
                continue

    elif dotscolor=='dots':
        list = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in list:
            piece = which_card(i)
            candidate = blanklist(board, piece)
            for j in range(len(candidate)):
                search_count += 1
                recycling_list = []
                recycling_list.append('0')
                recycling_list.append(return_card(candidate[j][2]))
                recycling_list.append(returnindex(candidate[j][1]))
                recycling_list.append(str(12 - candidate[j][0]).strip())
                transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0],
                                               candidate[j][2])
                list1.append(transfermove)
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                level2value = lastminaphabeta(board, board2, depth - 1, alpha, beta, dotscolor,list1)
                value = max(value, level2value)
                maxvalues.append(level2value)
                alpha = max(alpha, value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])
                coordinate.append(values[i][0])

            else:
                continue
    return coordinate[0], coordinate[1], coordinate[2],coordinate[3],maxvalues
def lastminaphabeta(board,board2,depth,alpha,beta,player,list1):
    opponent = SwitchPlayer(player)
    value = 1000000000
    if (depth == 0):
        return evaluation(board, board2,board3,opponent)
    candidate1 = remove_recyclingpiece(board3)
    for k in range(len(candidate1)):
        global flag2
        flag2=1
        real_removerecycle(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],candidate1[k][3])
        list = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in list:
            global flag
            flag=0
            piece = which_card(i)
            candidate = blanklist(board, piece)
            for j in range(len(candidate)):
                global search_count
                search_count += 1
                minmaxmove = []
                cardnu = ''
                minmaxmove.append(returnindex(candidate1[k][1]))
                minmaxmove.append(str(12-candidate1[k][0]).strip())
                minmaxmove.append(returnindex(candidate1[k][3]))
                minmaxmove.append(str(12-candidate1[k][2]).strip())
                minmaxmove.append(return_card(candidate[j][2]))
                minmaxmove.append(returnindex(candidate[j][1]))
                minmaxmove.append(str(12-candidate[j][0]).strip())
                cardid = samecard(minmaxmove, candidate1[k][1], candidate1[k][3], list1, cardnu)
                if cardid == return_card(candidate[j][2]):
                    continue
                elif cardid == 'notpass':
                    continue
                elif cardid == '':
                    continue
                elif cardid == "colerror":
                    continue
                else:
                    recycling_list = []
                    recycling_list.append('0')
                    recycling_list.append(return_card(candidate[j][2]))
                    recycling_list.append(returnindex(candidate[j][1]))
                    recycling_list.append(str(12-candidate[j][0]).strip())
                    transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                    list1.append(transfermove)
                    drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                    drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                    value = min(value,recyclingmaxaplhabetapurning(board, board2, depth - 1,alpha,beta,opponent,list1))
                    del list1[-1]
                    remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                    remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                    beta = min(beta, value)
                    if beta <= alpha:
                        global cut_count
                        cut_count += 1
                        drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                                       candidate1[k][3], candidate1[k][4])
                        return beta
        #                 flag=1
        #                 break
        #             else:
        #                 flag=0
        #         if flag == 1:
        #             flag2 = 0
        #             break
        #         else:
        #             continue
        # if flag2==0:
        #     continue
        else:
            drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                           candidate1[k][3], candidate1[k][4])
    return value
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
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
                level2value = minfunction(board, board2, depth - 1, dotscolor)
                value=max(value,level2value)
                maxvalues.append(level2value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])
                coordinate.append(values[i][0])

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
                level2value = minfunction(board, board2, depth - 1, dotscolor)
                value=max(value,level2value)
                maxvalues.append(level2value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])
                coordinate.append(values[i][0])

            else:
                continue
    return coordinate[0], coordinate[1], coordinate[2], coordinate[3],maxvalues

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
                level2value = alphabetapruningminfunction(board, board2, depth - 1, alpha, beta, dotscolor)
                value=max(value,level2value)
                maxvalues.append(level2value)
                alpha = max(alpha, value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])
                coordinate.append(values[i][0])

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
                level2value = alphabetapruningminfunction(board, board2, depth - 1, alpha, beta, dotscolor)
                value = max(value, level2value)
                maxvalues.append(level2value)
                alpha = max(alpha, value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])
                coordinate.append(values[i][0])

            else:
                continue
    return coordinate[0], coordinate[1], coordinate[2],coordinate[3],maxvalues

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
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
            if alpha >= beta:
                global cut_count
                cut_count+=1
                return alpha
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
            if beta <= alpha:
                global cut_count
                cut_count+=1
                return beta
    return value
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def minmaxrecycliing(board,board2,depth,dotscolor,list1):
    values = []
    maxvalues = []
    coordinate = []
    value = -1000000000
    global search_count
    if dotscolor == 'colors':
        candidate1 = remove_recyclingpiece(board3)
        for k in range(len(candidate1)):
            real_removerecycle(board,board2,board3,candidate1[k][0],candidate1[k][1],candidate1[k][2],candidate1[k][3])
            list = ['1', '2', '3', '4', '5', '6', '7', '8']
            for i in list:
                piece = which_card(i)
                candidate = blanklist(board, piece)
                for j in range(len(candidate)):
                    search_count += 1
                    move=[]
                    cardnu=''
                    move.append(returnindex(candidate1[k][1]))
                    move.append(str(12-candidate1[k][0]).strip())
                    move.append(returnindex(candidate1[k][3]))
                    move.append(str(12-candidate1[k][2]).strip())
                    move.append(return_card(candidate[j][2]))
                    move.append(returnindex(candidate[j][1]))
                    move.append(str(12-candidate[j][0]).strip())
                    cardid = samecard(move,candidate1[k][1],candidate1[k][3],list1,cardnu)
                    if cardid == return_card(candidate[j][2]):
                        continue
                    elif cardid == 'notpass':
                        continue
                    elif cardid == '':
                        continue
                    elif cardid == "colerror":
                        continue
                    else:
                        recycling_list = []
                        recycling_list.append('0')
                        recycling_list.append(return_card(candidate[j][2]))
                        recycling_list.append(returnindex(candidate[j][1]))
                        recycling_list.append(str(12-candidate[j][0]).strip())
                        transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                        list1.append(transfermove)
                        drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                        drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                        drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                        level2value =  minrecycling(board, board2, depth - 1, dotscolor,list1)
                        value = max(value,level2value)
                        maxvalues.append(level2value)
                        values.append([value, candidate1[k][0],candidate1[k][1],candidate1[k][2],candidate1[k][3],candidate[j][0], candidate[j][1], candidate[j][2]])
                        del list1[-1]
                        remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                        remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                        remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            drop_recycling(board,board2,board3,candidate1[k][0],candidate1[k][1],candidate1[k][2],candidate1[k][3],candidate1[k][4])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])
                coordinate.append(values[i][4])
                coordinate.append(values[i][5])
                coordinate.append(values[i][6])
                coordinate.append(values[i][7])
                coordinate.append(values[i][0])
            else:
                continue

    elif dotscolor == 'dots':
        candidate1 = remove_recyclingpiece(board3)
        for k in range(len(candidate1)):
            real_removerecycle(board,board2,board3,candidate1[k][0],candidate1[k][1],candidate1[k][2],candidate1[k][3])
            list = ['1', '2', '3', '4', '5', '6', '7', '8']
            for i in list:
                piece = which_card(i)
                candidate = blanklist(board, piece)
                for j in range(len(candidate)):
                    search_count += 1
                    move=[]
                    cardnu=''
                    move.append(returnindex(candidate1[k][1]))
                    move.append(str(12-candidate1[k][0]).strip())
                    move.append(returnindex(candidate1[k][3]))
                    move.append(str(12-candidate1[k][2]).strip())
                    move.append(return_card(candidate[j][2]))
                    move.append(returnindex(candidate[j][1]))
                    move.append(str(12-candidate[j][0]).strip())
                    cardid = samecard(move,candidate1[k][1],candidate1[k][3],list1,cardnu)
                    if cardid == return_card(candidate[j][2]):
                        continue
                    elif cardid == 'notpass':
                        continue
                    elif cardid == '':
                        continue
                    elif cardid == "colerror":
                        continue
                    else:
                        recycling_list = []
                        recycling_list.append('0')
                        recycling_list.append(return_card(candidate[j][2]))
                        recycling_list.append(returnindex(candidate[j][1]))
                        recycling_list.append(str(12-candidate[j][0]).strip())
                        transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                        list1.append(transfermove)
                        drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                        drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                        drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                        level2value = minrecycling(board, board2, depth - 1, dotscolor, list1)
                        value = max(value, level2value)
                        maxvalues.append(level2value)
                        values.append([value, candidate1[k][0],candidate1[k][1],candidate1[k][2],candidate1[k][3],candidate[j][0], candidate[j][1], candidate[j][2]])
                        del list1[-1]
                        remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                        remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                        remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            drop_recycling(board,board2,board3,candidate1[k][0],candidate1[k][1],candidate1[k][2],candidate1[k][3],candidate1[k][4])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])
                coordinate.append(values[i][4])
                coordinate.append(values[i][5])
                coordinate.append(values[i][6])
                coordinate.append(values[i][7])
                coordinate.append(values[i][0])
            else:
                continue
    return coordinate[0], coordinate[1], coordinate[2],coordinate[3],coordinate[4],coordinate[5],coordinate[6],coordinate[7],maxvalues
def maxrecycling(board,board2,depth,player,list1):
    opponent = SwitchPlayer(player)
    value = -1000000000
    if (depth == 0):
        return evaluation(board,board2,board3,opponent)
    candidate1 = remove_recyclingpiece(board3)
    for k in range(len(candidate1)):
        real_removerecycle(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],candidate1[k][3])
        list = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in list:
            piece = which_card(i)
            candidate = blanklist(board, piece)
            for j in range(len(candidate)):
                global search_count
                search_count += 1
                move = []
                cardnu = ''
                move.append(returnindex(candidate1[k][1]))
                move.append(str(12-candidate1[k][0]).strip())
                move.append(returnindex(candidate1[k][3]))
                move.append(str(12-candidate1[k][2]).strip())
                move.append(return_card(candidate[j][2]))
                move.append(returnindex(candidate[j][1]))
                move.append(str(12-candidate[j][0]).strip())
                cardid = samecard(move, candidate1[k][1], candidate1[k][3], list1, cardnu)
                if cardid == return_card(candidate[j][2]):
                    continue
                elif cardid == 'notpass':
                    continue
                elif cardid == '':
                    continue
                elif cardid == "colerror":
                    continue
                else:
                    recycling_list = []
                    recycling_list.append('0')
                    recycling_list.append(return_card(candidate[j][2]))
                    recycling_list.append(returnindex(candidate[j][1]))
                    recycling_list.append(str(12-candidate[j][0]).strip())
                    transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                    list1.append(transfermove)
                    drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                    drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                    bestvalue= minrecycling(board, board2, depth - 1, dotscolor,list1)
                    del list1[-1]
                    remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                    remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                    if bestvalue > value:
                        value = bestvalue
        drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2], candidate1[k][3],candidate1[k][4])
    return value

def minrecycling(board,board2,depth,player,list1):
    opponent = SwitchPlayer(player)
    value = 1000000000
    if (depth == 0):
        return evaluation(board, board2,board3,opponent)
    candidate1 = remove_recyclingpiece(board3)
    for k in range(len(candidate1)):
        real_removerecycle(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],candidate1[k][3])
        list = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in list:
            piece = which_card(i)
            candidate = blanklist(board, piece)
            for j in range(len(candidate)):
                global search_count
                search_count += 1
                minmaxmove = []
                cardnu = ''
                minmaxmove.append(returnindex(candidate1[k][1]))
                minmaxmove.append(str(12-candidate1[k][0]).strip())
                minmaxmove.append(returnindex(candidate1[k][3]))
                minmaxmove.append(str(12-candidate1[k][2]).strip())
                minmaxmove.append(return_card(candidate[j][2]))
                minmaxmove.append(returnindex(candidate[j][1]))
                minmaxmove.append(str(12-candidate[j][0]).strip())
                cardid = samecard(minmaxmove, candidate1[k][1], candidate1[k][3], list1, cardnu)
                if cardid == return_card(candidate[j][2]):
                    continue
                elif cardid == 'notpass':
                    continue
                elif cardid == '':
                    continue
                elif cardid == "colerror":
                    continue
                else:
                    recycling_list = []
                    recycling_list.append('0')
                    recycling_list.append(return_card(candidate[j][2]))
                    recycling_list.append(returnindex(candidate[j][1]))
                    recycling_list.append(str(12-candidate[j][0]).strip())
                    transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                    list1.append(transfermove)
                    drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                    drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                    bestvalue = maxrecycling(board, board2, depth - 1, opponent,list1)
                    del list1[-1]
                    remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                    remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                    if bestvalue < value:
                        value = bestvalue
        drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2], candidate1[k][3],candidate1[k][4])
    return value
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def alphabetapurningrecycling(board,board2,depth,alpha,beta,dotscolor,list1):
    values = []
    maxvalues = []
    coordinate = []
    value = -1000000000
    global search_count
    if dotscolor == 'colors':
        candidate1 = remove_recyclingpiece(board3)
        for k in range(len(candidate1)):
            real_removerecycle(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                               candidate1[k][3])
            list = ['1', '2', '3', '4', '5', '6', '7', '8']
            for i in list:
                piece = which_card(i)
                candidate = blanklist(board, piece)
                for j in range(len(candidate)):
                    search_count += 1
                    move = []
                    cardnu = ''
                    move.append(returnindex(candidate1[k][1]))
                    move.append(str(12 - candidate1[k][0]).strip())
                    move.append(returnindex(candidate1[k][3]))
                    move.append(str(12 - candidate1[k][2]).strip())
                    move.append(return_card(candidate[j][2]))
                    move.append(returnindex(candidate[j][1]))
                    move.append(str(12 - candidate[j][0]).strip())
                    cardid = samecard(move, candidate1[k][1], candidate1[k][3], list1, cardnu)
                    if cardid == return_card(candidate[j][2]):
                        continue
                    elif cardid == 'notpass':
                        continue
                    elif cardid == '':
                        continue
                    elif cardid == "colerror":
                        continue
                    else:
                        recycling_list = []
                        recycling_list.append('0')
                        recycling_list.append(return_card(candidate[j][2]))
                        recycling_list.append(returnindex(candidate[j][1]))
                        recycling_list.append(str(12 - candidate[j][0]).strip())
                        transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0],
                                                       candidate[j][2])
                        list1.append(transfermove)
                        drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                        drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                        drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                        level2value= recyclingminaplhabetapurning(board, board2, depth - 1, alpha,beta,dotscolor, list1)
                        value = max(value, level2value)
                        maxvalues.append(level2value)
                        alpha = max(alpha, value)
                        values.append([value, candidate1[k][0], candidate1[k][1], candidate1[k][2], candidate1[k][3],
                                       candidate[j][0], candidate[j][1], candidate[j][2]])
                        del list1[-1]
                        remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                        remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                        remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                           candidate1[k][3], candidate1[k][4])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])
                coordinate.append(values[i][4])
                coordinate.append(values[i][5])
                coordinate.append(values[i][6])
                coordinate.append(values[i][7])
                coordinate.append(values[i][0])
            else:
                continue

    elif dotscolor == 'dots':
        candidate1 = remove_recyclingpiece(board3)
        for k in range(len(candidate1)):
            real_removerecycle(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                               candidate1[k][3])
            list = ['1', '2', '3', '4', '5', '6', '7', '8']
            for i in list:
                piece = which_card(i)
                candidate = blanklist(board, piece)
                for j in range(len(candidate)):
                    search_count += 1
                    move = []
                    cardnu = ''
                    move.append(returnindex(candidate1[k][1]))
                    move.append(str(12 - candidate1[k][0]).strip())
                    move.append(returnindex(candidate1[k][3]))
                    move.append(str(12 - candidate1[k][2]).strip())
                    move.append(return_card(candidate[j][2]))
                    move.append(returnindex(candidate[j][1]))
                    move.append(str(12 - candidate[j][0]).strip())
                    cardid = samecard(move, candidate1[k][1], candidate1[k][3], list1, cardnu)
                    if cardid == return_card(candidate[j][2]):
                        continue
                    elif cardid == 'notpass':
                        continue
                    elif cardid == '':
                        continue
                    elif cardid == "colerror":
                        continue
                    else:
                        recycling_list = []
                        recycling_list.append('0')
                        recycling_list.append(return_card(candidate[j][2]))
                        recycling_list.append(returnindex(candidate[j][1]))
                        recycling_list.append(str(12 - candidate[j][0]).strip())
                        transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0],
                                                       candidate[j][2])
                        list1.append(transfermove)
                        drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                        drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                        drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                        level2value = recyclingminaplhabetapurning(board, board2, depth - 1, alpha, beta, dotscolor,
                                                                   list1)
                        value = max(value, level2value)
                        maxvalues.append(level2value)
                        alpha = max(alpha, value)
                        values.append([value, candidate1[k][0], candidate1[k][1], candidate1[k][2], candidate1[k][3],
                                       candidate[j][0], candidate[j][1], candidate[j][2]])
                        del list1[-1]
                        remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                        remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                        remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                           candidate1[k][3], candidate1[k][4])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                coordinate.append(values[i][1])
                coordinate.append(values[i][2])
                coordinate.append(values[i][3])
                coordinate.append(values[i][4])
                coordinate.append(values[i][5])
                coordinate.append(values[i][6])
                coordinate.append(values[i][7])
                coordinate.append(values[i][0])
            else:
                continue
    return coordinate[0], coordinate[1], coordinate[2], coordinate[3], coordinate[4], coordinate[5], coordinate[6],coordinate[7],maxvalues
def recyclingminaplhabetapurning(board,board2,depth,alpha,beta,player,list1):
    opponent = SwitchPlayer(player)
    value = 1000000000
    if (depth == 0):
        return evaluation(board, board2,board3,opponent)
    candidate1 = remove_recyclingpiece(board3)
    for k in range(len(candidate1)):
        global flag2
        flag2=1
        real_removerecycle(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],candidate1[k][3])
        list = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in list:
            global flag
            flag=0
            piece = which_card(i)
            candidate = blanklist(board, piece)
            for j in range(len(candidate)):
                global search_count
                search_count += 1
                minmaxmove = []
                cardnu = ''
                minmaxmove.append(returnindex(candidate1[k][1]))
                minmaxmove.append(str(12-candidate1[k][0]).strip())
                minmaxmove.append(returnindex(candidate1[k][3]))
                minmaxmove.append(str(12-candidate1[k][2]).strip())
                minmaxmove.append(return_card(candidate[j][2]))
                minmaxmove.append(returnindex(candidate[j][1]))
                minmaxmove.append(str(12-candidate[j][0]).strip())
                cardid = samecard(minmaxmove, candidate1[k][1], candidate1[k][3], list1, cardnu)
                if cardid == return_card(candidate[j][2]):
                    continue
                elif cardid == 'notpass':
                    continue
                elif cardid == '':
                    continue
                elif cardid == "colerror":
                    continue
                else:
                    recycling_list = []
                    recycling_list.append('0')
                    recycling_list.append(return_card(candidate[j][2]))
                    recycling_list.append(returnindex(candidate[j][1]))
                    recycling_list.append(str(12-candidate[j][0]).strip())
                    transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                    list1.append(transfermove)
                    drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                    drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                    value = min(value,recyclingmaxaplhabetapurning(board, board2, depth - 1,alpha,beta,opponent,list1))
                    del list1[-1]
                    remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                    remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                    beta = min(beta, value)
                    if beta <= alpha:
                        global cut_count
                        cut_count += 1
                        drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                                       candidate1[k][3], candidate1[k][4])
                        return beta
        #                 flag=1
        #                 break
        #             else:
        #                 flag=0
        #         if flag == 1:
        #             flag2 = 0
        #             break
        #         else:
        #             continue
        # if flag2==0:
        #     continue
        else:
            drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                           candidate1[k][3], candidate1[k][4])
    return value
def recyclingmaxaplhabetapurning(board,board2,depth,alpha,beta,player,list1):

    opponent = SwitchPlayer(player)
    value = -1000000000
    if (depth == 0):
        return evaluation(board,board2,board3,opponent)
    candidate1 = remove_recyclingpiece(board3)
    for k in range(len(candidate1)):
        global flag2
        flag2=1
        real_removerecycle(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],candidate1[k][3])
        list = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in list:
            global flag
            flag=0
            piece = which_card(i)
            candidate = blanklist(board, piece)
            for j in range(len(candidate)):
                global search_count
                search_count += 1
                move = []
                cardnu = ''
                move.append(returnindex(candidate1[k][1]))
                move.append(str(12-candidate1[k][0]).strip())
                move.append(returnindex(candidate1[k][3]))
                move.append(str(12-candidate1[k][2]).strip())
                move.append(return_card(candidate[j][2]))
                move.append(returnindex(candidate[j][1]))
                move.append(str(12-candidate[j][0]).strip())
                cardid = samecard(move, candidate1[k][1], candidate1[k][3], list1, cardnu)
                if cardid == return_card(candidate[j][2]):
                    continue
                elif cardid == 'notpass':
                    continue
                elif cardid == '':
                    continue
                elif cardid == "colerror":
                    continue
                else:
                    recycling_list = []
                    recycling_list.append('0')
                    recycling_list.append(return_card(candidate[j][2]))
                    recycling_list.append(returnindex(candidate[j][1]))
                    recycling_list.append(str(12-candidate[j][0]).strip())
                    transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                    list1.append(transfermove)
                    drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                    drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                    value = max(value,recyclingminaplhabetapurning(board, board2,depth - 1,alpha,beta,opponent,list1))
                    del list1[-1]
                    remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                    remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        global cut_count
                        cut_count += 1
                        drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                                       candidate1[k][3], candidate1[k][4])
                        return alpha
        #                 flag = 1
        #                 break
        #             else:
        #                 flag = 0
        #         if flag == 1:
        #             flag2 = 0
        #             break
        #         else:
        #             continue
        # if flag2==0:
        #     continue
        else:
            drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                           candidate1[k][3], candidate1[k][4])

    return value

#¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def samecard(move,cindex1,cindex2,recyclelist,card_id):
    if move[0] == move[2]:
        num = 1
        minmove = move[0]
    elif cindex1 == cindex2 - 1 or cindex1 == cindex2 + 1:
        num = 2
        minmove = min(move[0], move[2])
    else:
        print("invalid col input")
        card_id ="colerror"
        return card_id
    if num == 1:
        for j in recyclelist:
            for i in j:
                if minmove == i:
                    if recyclelist[recyclelist.index(j)][3] == move[1]:
                        if 12 - recyclelist[recyclelist.index(j)][5] == int(move[3]):
                            if recyclelist.index(j) < len(recyclelist) - 1:
                                if move[5] == move[0] == move[2] == recyclelist[recyclelist.index(j)][2] and move[6] == move[1] == \
                                        recyclelist[recyclelist.index(j)][3]:
                                    card_id = recyclelist[recyclelist.index(j)][1]
                                    return card_id
                                else:
                                    card_id = 'pass'
                                    continue
                            else:
                                if move[0] == recyclelist[recyclelist.index(j)][2] and move[1] == recyclelist[recyclelist.index(j)][3]:
                                    card_id = 'notpass'
                                    return card_id
                        else:
                            continue
                    elif int(recyclelist[recyclelist.index(j)][3]) == int(move[1]) - 1:
                        if 12 - recyclelist[recyclelist.index(j)][5] == int(move[3]) + 1:
                            if recyclelist.index(j) < len(recyclelist) - 1:
                                if move[5] == move[0] == move[2] == recyclelist[recyclelist.index(j)][2] and move[6] == move[3] == \
                                        recyclelist[recyclelist.index(j)][3]:
                                    card_id = recyclelist[recyclelist.index(j)][1]
                                    return card_id
                                else:
                                    card_id = 'pass'
                                    continue

                            else:
                                if move[2] == recyclelist[recyclelist.index(j)][2] and move[3] == recyclelist[recyclelist.index(j)][3]:
                                    card_id = 'notpass'
                                    return card_id
                        else:
                            continue
                    else:
                        continue
    elif num == 2:

        for j in recyclelist:
            for i in j:
                if minmove == i:
                    if recyclelist[recyclelist.index(j)][2] == move[0]:
                        judgemove = which_cindex(move[2])
                        if judgemove == recyclelist[recyclelist.index(j)][4]:
                            if recyclelist.index(j) < len(recyclelist) - 1:
                                if move[1] == move[3] == move[6] == recyclelist[recyclelist.index(j)][3] and move[5] == move[0] == \
                                        recyclelist[recyclelist.index(j)][2]:
                                    card_id = recyclelist[recyclelist.index(j)][1]
                                    return card_id
                                else:
                                    card_id = 'pass'
                                    continue

                            else:
                                if move[1] == recyclelist[recyclelist.index(j)][3]:
                                    card_id = 'notpass'
                                    return card_id
                        else:
                            continue
                    elif recyclelist[recyclelist.index(j)][2] == move[2]:
                        judgemove = which_cindex(move[0])
                        if judgemove == recyclelist[recyclelist.index(j)][4]:
                            if recyclelist.index(j) < len(recyclelist) - 1:
                                if move[1] == move[3] == move[6] == recyclelist[recyclelist.index(j)][3] and move[5] == move[2] == \
                                        recyclelist[recyclelist.index(j)][2]:
                                    card_id = recyclelist[recyclelist.index(j)][1]
                                    return card_id
                                else:
                                    card_id = 'pass'
                                    continue

                            else:
                                if move[3] == recyclelist[recyclelist.index(j)][3]:
                                    card_id = 'notpass'
                                    return card_id

                        else:
                            continue
                    else:
                        continue
    return card_id
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def play(user1,user2,turn,game_over,aiorhuman,dotscolor):
    firstuser=[]
    while not game_over:
        global en_count
        global orpurning
        if turn==0:
            if aiorhuman=='AI':
                orpurning=0
                print("It’s the turn of AI")
                en_count=0
                usercmd= input('Does AI activate alpha-beta? (y/n) : ')
                if usercmd.lower().startswith('y'):
                    if len(firstuser)==REGUALR_GAME-1:
                        coordinate = lastaphabeta(board,board2, DEPTH, -99999999, 99999999,dotscolor,firstuser)
                        orpurning =1
                    else:
                        coordinate = alphabetapruning(board,board2, DEPTH, -99999999, 99999999,dotscolor)
                        orpurning =1
                else:
                    if len(firstuser)==REGUALR_GAME-1:
                        coordinate = lastminmax(board,board2,DEPTH,dotscolor,firstuser)
                        orpurning=2
                    else:
                        coordinate = minimax(board,board2,DEPTH,dotscolor)
                        orpurning=2
                if orpurning==1:
                    outputcmd = input('Does AI generate trace of alpha-beta? (y/n) : ')
                    if outputcmd.lower().startswith('y'):
                        print(str(en_count).strip()+'\n'+str(coordinate[3]).strip()+'\n',file=open("output_alphabeta.txt", 'a'))
                        for i in range(0,len(coordinate[4])):
                            print(str(coordinate[4][i]).strip(),file=open("output_alphabeta.txt", 'a'))
                        print('\n'.strip(), file=open("output_alphabeta.txt", 'a'))
                else:
                    outputcmd = input('Does AI generate trace of mini-max? (y/n) : ')
                    if outputcmd.lower().startswith('y'):
                        print(str(en_count).strip()+'\n'+str(coordinate[3]).strip()+'\n',file=open("output_minmax.txt", 'a'))
                        for i in range(0,len(coordinate[4])):
                            print(str(coordinate[4][i]).strip(),file=open("output_minmax.txt", 'a'))
                        print('\n'.strip(),file=open("output_minmax.txt", 'a'))
                drop = drop_piece(board, coordinate[0], coordinate[1], coordinate[2])
                if drop:
                    colindex = returnindex(coordinate[1])
                    move = []
                    move.append('0')
                    move.append(return_card(coordinate[2]))
                    move.append(colindex)
                    move.append(str(12-coordinate[0]).strip())
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
                orpurning=0
                print("It’s the turn of AI")
                en_count=0
                usercmd= input('Does AI activate alpha-beta? (y/n) : ')
                if usercmd.lower().startswith('y'):
                    if len(firstuser)==REGUALR_GAME-1:
                        coordinate = lastaphabeta(board,board2,DEPTH, -99999999, 99999999,dotscolor,firstuser)
                        orpurning = 1
                    else:
                        coordinate = alphabetapruning(board,board2,DEPTH, -99999999, 99999999,dotscolor)
                        orpurning = 1
                else:
                    if len(firstuser)==REGUALR_GAME-1:
                        coordinate = lastminmax(board,board2,DEPTH,dotscolor,firstuser)
                        orpurning=2
                    else:
                        coordinate = minimax(board,board2,DEPTH,dotscolor)
                        orpurning=2
                if orpurning==1:
                    outputcmd = input('Does AI generate trace of alpha-beta? (y/n) : ')
                    if outputcmd.lower().startswith('y'):
                        print(str(en_count).strip()+'\n'+str(coordinate[3]).strip()+'\n',file=open("output_alphabeta.txt", 'a'))
                        for i in range(0,len(coordinate[4])):
                            print(str(coordinate[4][i]).strip(),file=open("output_alphabeta.txt", 'a'))
                        print('\n'.strip(), file=open("output_alphabeta.txt", 'a'))
                else:
                    outputcmd = input('Does AI generate trace of mini-max? (y/n) : ')
                    if outputcmd.lower().startswith('y'):
                        print(str(en_count).strip()+'\n'+str(coordinate[3]).strip()+'\n',file=open("output_minmax.txt", 'a'))
                        for i in range(0,len(coordinate[4])):
                            print(str(coordinate[4][i]).strip(),file=open("output_minmax.txt", 'a'))
                        print('\n'.strip(),file=open("output_minmax.txt", 'a'))
                drop = drop_piece(board, coordinate[0], coordinate[1], coordinate[2])
                if drop:
                    colindex = returnindex(coordinate[1])
                    move = []
                    move.append('0')
                    move.append(return_card(coordinate[2]))
                    move.append(colindex)
                    move.append(str(12-coordinate[0]).strip())
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
        if(len(firstuser)==REGUALR_GAME):
            print("In regular game, game ends in a draw. They need go head to next section")
            sum = len(firstuser)
            recycling(firstuser,game_over,user1,user2,turn,sum,aiorhuman,dotscolor)
            break

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def recycling(recyclelist,game_over,user1,user2,turn,sum,aiorhuman,dotscolor):
    global remo
    global card_id
    global cardnum
    global recyclinglist
    while not game_over:
        cardnum = ''
        global orpurning
        global en_count
        if turn == 0:
            if aiorhuman == 'AI':
                orpurning=0
                print("It’s the turn of AI")
                en_count=0
                usercmd= input('Does AI activate alpha-beta? (y/n) : ')
                if usercmd.lower().startswith('y'):
                    if sum==59:
                        DEPTH=1
                        coordinate = alphabetapurningrecycling(board,board2, DEPTH, -99999999, 99999999,dotscolor,recyclelist)
                        orpurning=1
                    else:
                        coordinate = alphabetapurningrecycling(board,board2, DEPTH, -99999999, 99999999,dotscolor,recyclelist)
                        orpurning=1
                else:
                    if sum==59:
                        DEPTH=1
                        coordinate = minmaxrecycliing(board, board2, DEPTH, dotscolor, recyclelist)
                        orpurning = 2
                    else:
                        coordinate = minmaxrecycliing(board,board2,DEPTH,dotscolor,recyclelist)
                        orpurning=2
                if orpurning==1:
                    outputcmd = input('Does AI generate trace of alpha-beta? (y/n) : ')
                    if outputcmd.lower().startswith('y'):
                        if sum==59:
                            print(str(en_count).strip() + '\n' + str(coordinate[7]).strip() + '\n',
                                  file=open("output_alphabeta.txt", 'a'))
                            print(str(coordinate[7]).strip() + '\n',file=open("output_alphabeta.txt", 'a'))
                        else:
                            print(str(en_count).strip()+'\n'+str(coordinate[7]).strip()+'\n',file=open("output_alphabeta.txt", 'a'))
                            for i in range(0,len(coordinate[8])):
                                print(str(coordinate[8][i]).strip(),file=open("output_alphabeta.txt", 'a'))
                            print('\n'.strip(), file=open("output_alphabeta.txt", 'a'))
                else:
                    outputcmd = input('Does AI generate trace of mini-max? (y/n) : ')
                    if outputcmd.lower().startswith('y'):
                        if sum==59:
                            print(str(en_count).strip() + '\n' + str(coordinate[7]).strip() + '\n',
                                  file=open("output_minmax.txt", 'a'))
                            print(str(coordinate[7]).strip() + '\n',file=open("output_minmax.txt", 'a'))
                        else:
                            print(str(en_count).strip()+'\n'+str(coordinate[7]).strip()+'\n',file=open("output_minmax.txt", 'a'))
                            for i in range(0,len(coordinate[8])):
                                print(str(coordinate[8][i]).strip(),file=open("output_minmax.txt", 'a'))
                            print('\n'.strip(),file=open("output_minmax.txt", 'a'))
                real_removerecycle(board,board2,board3,coordinate[0],coordinate[1],coordinate[2],coordinate[3])
                drop = drop_piece(board, coordinate[4], coordinate[5], coordinate[6])
                if drop:
                    sum+=1
                    colindex = returnindex(coordinate[5])
                    recyclinglist = []
                    recyclinglist.append('0')
                    recyclinglist.append(return_card(coordinate[6]))
                    recyclinglist.append(colindex)
                    recyclinglist.append(str(12-coordinate[4]).strip())
                    transfermove = cardinformation(recyclinglist, coordinate[5], coordinate[4], coordinate[6])
                    recyclelist.append(transfermove)
                    yindex2, xindex2 = dropindex(coordinate[5], coordinate[4], coordinate[6])
                    board2[coordinate[4]][coordinate[5]][0] = 1
                    board2[xindex2][yindex2][0] = 1
                    drop_piece3(board3, coordinate[4], coordinate[5], coordinate[6])
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
                if move[0]!='0':
                    cindex1 = which_cindex(move[0])
                    cindex2 = which_cindex(move[2])
                    if cindex1==UnboundLocalError or cindex2==UnboundLocalError :
                        continue
                    card_id=samecard(move,cindex1,cindex2,recyclelist,cardnum)
                    if card_id == move[4]:
                        print("cannot be same card")
                        print("try again")
                        continue
                    elif card_id=='notpass':
                        print("cannot place card in other player just placed")
                        print("try again")
                        continue

                    elif card_id=='':
                        print("error input")
                        continue
                    elif card_id=="colerror":
                        continue
                    if is_valid2(move[1],move[3]):
                        rindex1 = 12 - int(move[1])
                        rindex2 = 12 - int(move[3])
                        remo = remove(board,board2,board3,rindex1,cindex1,rindex2,cindex2)
                        if remo==False:
                            print("remove failure")
                            print("try again")
                            continue
                    else:
                        print("not valid")
                        print("try again")
                        continue

                    card = which_card(move[4])
                    cindex3 = which_cindex(move[5])
                    if card==UnboundLocalError:
                        continue
                    elif cindex3==UnboundLocalError:
                        continue
                    if is_valid(move[6],card,cindex3):
                        rindex = 12-int(move[6])
                        drop = drop_piece(board, rindex, cindex3, card)
                        if drop==False:
                            print("drop failure")
                            print("try again")
                            continue
                        elif drop==True:
                            sum += 1
                            recyclinglist=[]
                            recyclinglist.append('0')
                            recyclinglist.append(move[4])
                            recyclinglist.append(move[5])
                            recyclinglist.append(move[6])
                            transfermove = cardinformation(recyclinglist, cindex3, rindex, card)
                            recyclelist.append(transfermove)
                            drop_piece3(board3, rindex, cindex3, card)
                            yindex2, xindex2 = dropindex(cindex3, rindex, card)
                            board2[rindex][cindex3][0] = 1
                            board2[xindex2][yindex2][0] = 1

                        if user1=='dots':
                            win1 = winning_move(board, user1, user2)
                            win2 = winning_move(board, user2, user1)
                            if win1 == 1:
                                print(*board, sep='\n')
                                print("player {0} winning".format(aiorhuman))
                                print("*****GAME END*****")
                                break
                            elif win2 == 0:
                                print(*board, sep='\n')
                                print("player {0} winning".format(SwitchPlayer2(aiorhuman)))
                                print("*****GAME END*****")
                                break
                        elif user1=='colors':
                            win1 = winning_move(board, user2, user1)
                            win2 = winning_move(board, user1, user2)
                            if win1 == 1:
                                print(*board, sep='\n')
                                print("player {0} winning".format(aiorhuman))
                                print("*****GAME END*****")
                                break
                            elif win2 == 0:
                                print(*board, sep='\n')
                                print("player {0} winning".format(SwitchPlayer2(aiorhuman)))
                                print("*****GAME END*****")
                                break
                    else:
                        print("not valid")
                        print("try again")
                        continue
                else:
                    print("try again")
                    continue

        else:
            if aiorhuman=='AI':
                orpurning=0
                print("It’s the turn of AI")
                en_count=0
                usercmd= input('Does AI activate alpha-beta? (y/n) : ')
                if usercmd.lower().startswith('y'):
                    if sum == 59:
                        DEPTH = 1
                        coordinate = alphabetapurningrecycling(board, board2, DEPTH, -99999999, 99999999, dotscolor,
                                                               recyclelist)
                        orpurning = 1
                    else:
                        coordinate = alphabetapurningrecycling(board, board2, DEPTH, -99999999, 99999999, dotscolor,
                                                               recyclelist)
                        orpurning = 1
                else:
                    if sum == 59:
                        DEPTH = 1
                        coordinate = minmaxrecycliing(board, board2, DEPTH, dotscolor, recyclelist)
                        orpurning = 2
                    else:
                        coordinate = minmaxrecycliing(board, board2, DEPTH, dotscolor, recyclelist)
                        orpurning = 2
                if orpurning == 1:
                    outputcmd = input('Does AI generate trace of alpha-beta? (y/n) : ')
                    if outputcmd.lower().startswith('y'):
                        if sum == 59:
                            print(str(en_count).strip() + '\n' + str(coordinate[7]).strip() + '\n',
                                  file=open("output_alphabeta.txt", 'a'))
                            print(str(coordinate[7]).strip() + '\n', file=open("output_alphabeta.txt", 'a'))
                        else:
                            print(str(en_count).strip() + '\n' + str(coordinate[7]).strip() + '\n',
                                  file=open("output_alphabeta.txt", 'a'))
                            for i in range(0, len(coordinate[8])):
                                print(str(coordinate[8][i]).strip(), file=open("output_alphabeta.txt", 'a'))
                            print('\n'.strip(), file=open("output_alphabeta.txt", 'a'))
                else:
                    outputcmd = input('Does AI generate trace of mini-max? (y/n) : ')
                    if outputcmd.lower().startswith('y'):
                        if sum == 59:
                            print(str(en_count).strip() + '\n' + str(coordinate[7]).strip() + '\n',
                                  file=open("output_minmax.txt", 'a'))
                            print(str(coordinate[7]).strip() + '\n', file=open("output_minmax.txt", 'a'))
                        else:
                            print(str(en_count).strip() + '\n' + str(coordinate[7]).strip() + '\n',
                                  file=open("output_minmax.txt", 'a'))
                            for i in range(0, len(coordinate[8])):
                                print(str(coordinate[8][i]).strip(), file=open("output_minmax.txt", 'a'))
                            print('\n'.strip(), file=open("output_minmax.txt", 'a'))
                real_removerecycle(board, board2, board3, coordinate[0], coordinate[1], coordinate[2], coordinate[3])
                drop = drop_piece(board, coordinate[4], coordinate[5], coordinate[6])
                if drop:
                    sum+=1
                    colindex = returnindex(coordinate[5])
                    recyclinglist = []
                    recyclinglist.append('0')
                    recyclinglist.append(return_card(coordinate[6]))
                    recyclinglist.append(colindex)
                    recyclinglist.append(str(12-coordinate[4]).strip())
                    transfermove = cardinformation(recyclinglist, coordinate[5], coordinate[4], coordinate[6])
                    recyclelist.append(transfermove)
                    yindex2, xindex2 = dropindex(coordinate[5], coordinate[4], coordinate[6])
                    board2[coordinate[4]][coordinate[5]][0] = 1
                    board2[xindex2][yindex2][0] = 1
                    drop_piece3(board3, coordinate[4], coordinate[5], coordinate[6])
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

            else:
                move = input("Input a slot player {0}: ".format(aiorhuman))
                move = move.split(' ')
                if move[0]!='0':
                    cindex1 = which_cindex(move[0])
                    cindex2 = which_cindex(move[2])

                    if cindex1==UnboundLocalError or cindex2==UnboundLocalError :
                        continue
                    card_id = samecard(move, cindex1, cindex2, recyclelist, cardnum)
                    if card_id == move[4]:
                        print("cannot be same card")
                        print("try again")
                        continue
                    elif card_id=='notpass':
                        print("cannot place card in other player just placed")
                        print("try again")
                        continue
                    elif card_id=='':
                        print("error input")
                        continue
                    elif card_id=="colerror":
                        continue
                    if is_valid2(move[1], move[3]):
                        rindex1 = 12 - int(move[1])
                        rindex2 = 12 - int(move[3])
                        remo = remove(board,board2,board3,rindex1, cindex1, rindex2, cindex2)
                        if remo == False:
                            print("remove failure")
                            print("try again")
                            continue
                    else:
                        print("not valid")
                        print("try again")
                        continue

                    card = which_card(move[4])
                    cindex3 = which_cindex(move[5])
                    if card == UnboundLocalError:
                        continue
                    elif cindex3 == UnboundLocalError:
                        continue

                    if is_valid(move[6],card,cindex3):
                        rindex = 12-int(move[6])
                        drop= drop_piece(board, rindex, cindex3, card)
                        if drop==False:
                            print("drop failure")
                            print("try again")
                            continue
                        elif drop == True:
                            sum += 1
                            recyclinglist=[]
                            recyclinglist.append('0')
                            recyclinglist.append(move[4])
                            recyclinglist.append(move[5])
                            recyclinglist.append(move[6])
                            transfermove = cardinformation(recyclinglist, cindex3, rindex, card)
                            recyclelist.append(transfermove)
                            drop_piece3(board3, rindex, cindex3, card)
                            yindex2, xindex2 = dropindex(cindex3, rindex, card)
                            board2[rindex][cindex3][0] = 1
                            board2[xindex2][yindex2][0] = 1
                        if user2=='dots':
                            win1 = winning_move(board, user1,user2)
                            win2 = winning_move(board, user2, user1)
                            if win1==0:
                                print(*board, sep='\n')
                                print("player {0} winning".format(aiorhuman))
                                print("*****GAME END*****")
                                break
                            elif win2==1:
                                print(*board, sep='\n')
                                print("player {0} winning".format(SwitchPlayer2(aiorhuman)))
                                print("*****GAME END*****")
                                break
                        elif user2=='colors':
                            win1 = winning_move(board, user2,user1)
                            win2 = winning_move(board, user1,user2)
                            if win1==0:
                                print(*board, sep='\n')
                                print("player {0} winning".format(aiorhuman))
                                print("*****GAME END*****")
                                break
                            elif win2==1:
                                print(*board, sep='\n')
                                print("player {0} winning".format(SwitchPlayer2(aiorhuman)))
                                print("*****GAME END*****")
                                break
                    else:
                        print("not valid")
                        print("try again")
                        continue
                else:
                    print("try again")
                    continue
        print(*board, sep='\n')
        turn +=1
        turn=turn % 2
        aiorhuman= SwitchPlayer2(aiorhuman)
        dotscolor =SwitchPlayer(dotscolor)
        print("Overall steps: ",end="")
        print(sum)
        if sum==RECYCLING_GAME:
            print("After regualr and recycling game, game ends in a draw")
            break
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

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

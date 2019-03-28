from card import Card
from point import Point
import timeit
import random
ROW_COUNT = 8
COL_COUNT = 12
global DEPTH
DEPTH = 2
search_count=0
cut_count = 0
en_count =0
REGUALR_GAME = 24
RECYCLING_GAME=60

def create_board():
    board = [['□□' for _ in range(ROW_COUNT)] for _ in range(COL_COUNT)]
    return board
#$$$$$$$$$$$$$$$$$$$$$
def evaluation_2(board, player):
    TOTAL_ROW = 12
    TOTAL_COL = 8

    global en_count
    en_count += 1
    SCOREAI = 0     # (good for AI + danger for human) - (good for human + danger for AI)
    SCOREHUMAN = 0  # (good for human + danger for AI) - (good for AI + danger for human)

    # iterate over all lines possible for the current board
    list_x = []
    list_y = []
    list_posdiagonal = []
    list_negadiagonal = []
    linecount = 0
    # push all x-coordinate in list_x
    for r in range(TOTAL_ROW):
        list=[]
        for c in range(TOTAL_COL):
            list.append(board[r][c])
        list_x.append(list)

    # push all y-coordinate in list_y
    for c in range(TOTAL_COL):
        list=[]
        for r in range (TOTAL_ROW):
            list.append(board[r][c])
        list_y.append(list)

    # push all positive diagonal coordinate in list_posdiagonal
    # (first 9 positive diagonals)
    for r in range(0, TOTAL_ROW):
        list = []
        rr = r
        for c in range(0, TOTAL_COL):
            list.append(board[rr][c])
            rr-=1
            if rr == -1:
                break
        if len(list) >= 4:
            list_posdiagonal.append(list)
    # (the rest 4 positive diagonals)
    h = 0
    for r in range(TOTAL_ROW - 1, 5 + h, -1):
        list = []
        rr = r
        for c in range(1 + h, TOTAL_COL):
            list.append(board[rr][c])
            rr-=1
        h+=1
        if len(list) >= 4:
            list_posdiagonal.append(list)

    # push all negative diagnonal coordiate in list_negadiagonal
    # (first 9 negative diagonals)
    for r in range(0, TOTAL_ROW):
        list = []
        rr = r
        for c in range(0, TOTAL_COL):
            list.append(board[rr][c])
            rr+=1
            if rr == TOTAL_ROW:
                break
        if len(list) >= 4:
            list_negadiagonal.append(list)
    # (the rest 4 negative diagonals)
    h = 0
    for r in range(0, 6 - h):
        list = []
        rr = r
        for c in range(1 + h, TOTAL_COL):
            list.append(board[rr][c])
            rr+=1
        h+=1
        if len(list) >= 4:
            list_negadiagonal.append(list)
    # so far, list_x, list_y, list_posdiagonal, list_negadiagonal have been assigned

    # print('len(list_x) = ', len(list_x))
    # print('len(list_y) = ', len(list_y))
    # print('len(list_posdiagonal) = ', len(list_posdiagonal))
    # print('len(list_negadiagonal) = ', len(list_negadiagonal))

    # danger and good scale between 0 and 100
    danger_color = 0.0
    good_color = 0.0
    danger_dot = 0.0
    good_dot = 0.0
    DANGER_FACTOR = 100.0
    GOOD_FACTOR = 50.0

    # look at all rows
    for i in range(len(list_x)):
        red = 0
        white = 0
        hollow = 0
        solid = 0
        for j in range(0, len(list_x[i]) - 4):
            if list_x[i][j][0] == '□':
                continue
            for k in range(0, 4):
                linecount += 1
                if list_x[i][j+k][1] == 'O':
                    hollow+=1
                if list_x[i][j+k][1] == 'X':
                    solid+=1
                if list_x[i][j+k][0] == 'R':
                    red+=1
                if list_x[i][j+k][0] == 'W':
                    white+=1

        # calculate danger_dot and danger_color
        maxAllowPerc = (4 - 1) / 4.0
        percWon_color = red / 4.0
        if percWon_color > 0.3:
            dangerous = percWon_color * (DANGER_FACTOR / maxAllowPerc)
            danger_dot += dangerous
        percWon_color = white / 4.0
        if percWon_color > 0.3:
            dangerous = percWon_color * (DANGER_FACTOR / maxAllowPerc)
            danger_dot += dangerous

        percWon_dot = hollow / 4.0
        if percWon_dot > 0.3:
            dangerous = percWon_dot * (DANGER_FACTOR / maxAllowPerc)
            danger_color += dangerous
        percWon_dot = solid / 4.0
        if percWon_dot > 0.3:
            dangerous = percWon_dot * (DANGER_FACTOR / maxAllowPerc)
            danger_color += dangerous

        # calculate good_color and good_dot
        goodFac = GOOD_FACTOR / ((4 - 1) * (4 - 1))
        goodness = red * red * goodFac
        good_color += goodness
        goodness = white * white * goodFac
        good_color += goodness

        goodness = hollow * hollow * goodFac
        good_dot += goodness
        goodness = solid * solid * goodFac
        good_dot += goodness


    # look at all columns
    for i in range(len(list_y)):
        red = 0
        white = 0
        hollow = 0
        solid = 0
        for j in range(0, len(list_y[i]) - 4):
            if list_y[i][j][0] == '□':
                continue
            for k in range(0, 4):
                linecount += 1
                if list_y[i][j+k][1] == 'O':
                    hollow+=1
                if list_y[i][j+k][1] == 'X':
                    solid+=1
                if list_y[i][j+k][0] == 'R':
                    red+=1
                if list_y[i][j+k][0] == 'W':
                    white+=1

        # calculate danger_dot and danger_color
        maxAllowPerc = (4 - 1) / 4.0
        percWon_color = red / 4.0
        if percWon_color > 0.3:
            dangerous = percWon_color * (DANGER_FACTOR / maxAllowPerc)
            danger_dot += dangerous
        percWon_color = white / 4.0
        if percWon_color > 0.3:
            dangerous = percWon_color * (DANGER_FACTOR / maxAllowPerc)
            danger_dot += dangerous

        percWon_dot = hollow / 4.0
        if percWon_dot > 0.3:
            dangerous = percWon_dot * (DANGER_FACTOR / maxAllowPerc)
            danger_color += dangerous
        percWon_dot = solid / 4.0
        if percWon_dot > 0.3:
            dangerous = percWon_dot * (DANGER_FACTOR / maxAllowPerc)
            danger_color += dangerous

        # calculate good_color and good_dot
        goodFac = GOOD_FACTOR / ((4 - 1) * (4 - 1))
        goodness = red * red * goodFac
        good_color += goodness
        goodness = white * white * goodFac
        good_color += goodness

        goodness = hollow * hollow * goodFac
        good_dot += goodness
        goodness = solid * solid * goodFac
        good_dot += goodness

    # look at all positive diagonals
    for i in range(len(list_posdiagonal)):
        red = 0
        white = 0
        hollow = 0
        solid = 0
        for j in range(0, len(list_posdiagonal[i]) - 4):
            if list_posdiagonal[i][j][0] == '□':
                continue
            for k in range(0, 4):
                linecount += 1
                if list_posdiagonal[i][j + k][1] == 'O':
                    hollow+=1
                if list_posdiagonal[i][j + k][1] == 'X':
                    solid+=1
                if list_posdiagonal[i][j + k][0] == 'R':
                    red+=1
                if list_posdiagonal[i][j + k][0] == 'W':
                    white+=1

        # calculate danger_dot and danger_color
        maxAllowPerc = (4 - 1) / 4.0
        percWon_color = red / 4.0
        if percWon_color > 0.3:
            dangerous = percWon_color * (DANGER_FACTOR / maxAllowPerc)
            danger_dot += dangerous
        percWon_color = white / 4.0
        if percWon_color > 0.3:
            dangerous = percWon_color * (DANGER_FACTOR / maxAllowPerc)
            danger_dot += dangerous

        percWon_dot = hollow / 4.0
        if percWon_dot > 0.3:
            dangerous = percWon_dot * (DANGER_FACTOR / maxAllowPerc)
            danger_color += dangerous
        percWon_dot = solid / 4.0
        if percWon_dot > 0.3:
            dangerous = percWon_dot * (DANGER_FACTOR / maxAllowPerc)
            danger_color += dangerous

        # calculate good_color and good_dot
        goodFac = GOOD_FACTOR / ((4 - 1) * (4 - 1))
        goodness = red * red * goodFac
        good_color += goodness
        goodness = white * white * goodFac
        good_color += goodness

        goodness = hollow * hollow * goodFac
        good_dot += goodness
        goodness = solid * solid * goodFac
        good_dot += goodness


    # look at all negative diagonals
    for i in range(len(list_negadiagonal)):
        red = 0
        white = 0
        hollow = 0
        solid = 0
        for j in range(0, len(list_negadiagonal[i]) - 4):
            if list_negadiagonal[i][j][0] == '□':
                continue
            for k in range(0, 4):
                linecount += 1
                if list_negadiagonal[i][j + k][1] == 'O':
                    hollow+=1
                if list_negadiagonal[i][j + k][1] == 'X':
                    solid+=1
                if list_negadiagonal[i][j + k][0] == 'R':
                    red+=1
                if list_negadiagonal[i][j + k][0] == 'W':
                    white+=1
        # calculate danger_dot and danger_color
        maxAllowPerc = (4 - 1) / 4.0
        percWon_color = red / 4.0
        if percWon_color > 0.3:
            dangerous = percWon_color * (DANGER_FACTOR / maxAllowPerc)
            danger_dot += dangerous
        percWon_color = white / 4.0
        if percWon_color > 0.3:
            dangerous = percWon_color * (DANGER_FACTOR / maxAllowPerc)
            danger_dot += dangerous

        percWon_dot = hollow / 4.0
        if percWon_dot > 0.3:
            dangerous = percWon_dot * (DANGER_FACTOR / maxAllowPerc)
            danger_color += dangerous
            percWon_dot = solid / 4.0
        if percWon_dot > 0.3:
            dangerous = percWon_dot * (DANGER_FACTOR / maxAllowPerc)
            danger_color += dangerous

        # calculate good_color and good_dot
        goodFac = GOOD_FACTOR / ((4 - 1) * (4 - 1))
        goodness = red * red * goodFac
        good_color += goodness
        goodness = white * white * goodFac
        good_color += goodness

        goodness = hollow * hollow * goodFac
        good_dot += goodness
        goodness = solid * solid * goodFac
        good_dot += goodness

    # print('good = ', good / linecount)
    # print('danger = ', danger / linecount)

    if player == 'colors':   # AI plays color
        SCOREAI = (good_color * 5 + danger_dot * 4) - (good_dot * 2 + danger_color * 1)
        SCOREHUMAN = (good_dot * 5 + danger_color * 4) - (good_color * 2 + danger_dot * 1)
    else:   # AI plays dot
        SCOREAI = (good_dot * 5 + danger_color * 4) - (good_color * 2 + danger_dot * 1)
        SCOREHUMAN = (good_color * 5 + danger_dot * 4)   - (good_dot * 2 + danger_color * 1)
    #
    # print('SCORE AI = ', SCOREAI / linecount)
    # print('SCORE HUMAN = ', SCOREHUMAN / linecount)

    return SCOREAI - SCOREHUMAN
#$$$$$$$$$$$$$$$$$$$$$
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

def history_list(board,row,col,piece,historylist):
    drop_piece(board, row, col, piece)
    list=[]
    for r in range(COL_COUNT):
        for c in range(ROW_COUNT):
            if board[r][c]!='□□':
                list.append(r)
                list.append(c)
                list.append(board[r][c])
            else:
                continue
    list.append(0)
    allofsame=True
    historyvalue=0
    for x in range(len(historylist)):
        if len(historylist[x])==len(list):
            for y in range(len(historylist[x])-1):
                if y==len(historylist[x])-2:
                    if historylist[x][y]==list[y]:
                        historyvalue=historylist[x][y+1]
                        remove_piece(board, row, col, piece)
                        return allofsame,historyvalue
                    else:
                        break
                elif historylist[x][y]==list[y]:
                    continue
                else:
                    break
    allofsame = False
    remove_piece(board, row, col, piece)
    return allofsame,historyvalue
def isalone(board3,row,col,piece):
    drop_piece3(board3, row, col, piece)
    if row==11:
            if (piece is Card.card2 or piece is Card.card4 or piece is Card.card6 or piece is Card.card8):
                if col==0:
                    if board3[row][col+1]=='□□':
                        return True
                elif col==7:
                    if board3[row][col-1]=='□□':
                        return True
                else:
                    if board3[row][col-1]=='□□' and board3[row][col+1]=='□□':
                        return True
            else:
                if col==0:
                    if board3[row][col+2]=='□□':
                        return True
                elif col==6:
                    if board3[row][col-1]=='□□':
                        return True
                else:
                    if board3[row][col-1]=='□□' and board3[row][col+2]=='□□':
                        return True
    remove_piece3(board3, row, col, piece)
    return False


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
        # board2[row][col][0] = 1
        # board2[row2][col2][0] = 1
    else:
        board3[row][col] = piece.top
        board3[row2][col2] = piece.below
        board[row][col] = piece.top[0]
        board[row2][col2] = piece.below[0]
        # board2[row][col][0] = 1
        # board2[row2][col2][0] = 1


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
            # board2[raw1][col1][0]=0
            # board2[raw2][col2][0] = 0
        else:

            if board[raw-2][col]=='□□':
                board[raw1][col1] = '□□'
                board[raw2][col2] = '□□'
                board3[raw1][col1] = '□□'
                board3[raw2][col2] = '□□'
                # board2[raw1][col1][0] = 0
                # board2[raw2][col2][0] = 0
                return True
            else:
                return False
    elif turn==2:
        if raw==0:
            board[raw1][col1] = '□□'
            board[raw2][col2] = '□□'
            board3[raw1][col1] = '□□'
            board3[raw2][col2] = '□□'
            # board2[raw1][col1][0]=0
            # board2[raw2][col2][0] = 0
        else:

            if board[raw-1][col]=='□□' and board[raw-1][col+1]=='□□':
                board[raw1][col1] = '□□'
                board[raw2][col2] = '□□'
                board3[raw1][col1] = '□□'
                board3[raw2][col2] = '□□'
                # board2[raw1][col1][0] = 0
                # board2[raw2][col2][0] = 0
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
    # board2[row][col][0] = 0
    # board2[row2][col2][0] = 0





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
                elif board[r][c][0]=='R' and board[r+1][c+1][0]=='R' and board[r+2][c+2][0]=='R' and board[r+3][c+3][0]=='R':
                    return 0
#   ##############################################################################3

def evaluation(board,board2,board3,player):
    global en_count
    en_count+=1
    SCOREAI =0
    SCOREHUMAN =0

    # X coordinate
    listx =[]
    listy=[]
    list_posdiag=[]
    list_negadiag=[]
    for r in range(COL_COUNT):
        list=[]
        for c in range(ROW_COUNT):
            list.append(board[r][c])
        listx.append(list)
    # y coordinate
    for c in range(ROW_COUNT):
        list=[]
        for r in range (COL_COUNT):
            list.append(board[r][c])
        listy.append(list)

    # above_half postitive diagonal coordinate
    for r in range(3,12):
        list = []
        if r<=7:
            c=0
            for i in range(r,-1,-1):
                list.append(board[i][c])
                c+=1
            list_posdiag.append(list)
    # below_half postitive diagonal coordinate
        else:
            i=r
            for c in range(0,8,1):
                list.append(board[i][c])
                i-=1
            list_posdiag.append(list)
    for c in range(1,ROW_COUNT-3):
        r = 11
        list=[]
        for j in range(c,8,1):
            list.append(board[r][j])
            r-=1
        list_posdiag.append(list)
    # below_half diagonal coordinate
    for r in range(COL_COUNT-3):
        list=[]
        if r<=4:
            i=r
            for c in range(0,8,1):
                list.append(board[i][c])

                i+=1
            list_negadiag.append(list)
        else:
            c=0
            for i in range(r,12,1):
                list.append(board[i][c])

                c+=1
            list_negadiag.append(list)
    # above_half postitive diagonal coordinate
    for c in range(1,ROW_COUNT-3):
        list=[]
        r=0
        for j in range(c,8,1):
            list.append(board[r][j])
            r+=1
        list_negadiag.append(list)
    alllist=listx+listy+list_posdiag+list_negadiag
    scoreai ,scorehuman = hurestic_overallfunction(alllist,player)
    SCOREAI+=scoreai
    SCOREHUMAN+=scorehuman
    return SCOREAI - SCOREHUMAN
def hurestic_function(list_elem1,list_elem2,list_elem3,list_elem4,player):
    SCOREHUMAN =0
    SCOREAI=0
    list=[]
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    list.append(list_elem1)
    list.append(list_elem2)
    list.append(list_elem3)
    list.append(list_elem4)

    for i in list:
        if i=='□□':
            sum1+=1
        elif i[0]=='W':
            sum2+=1
        elif i[0]=='R':
            sum3+=1
        elif i[1]=='O':
            sum4+=1
        elif i[1]=='X':
            sum5+=1
    if sum1==4 or sum2+sum3>0 and sum4+ sum5>0:
        SCOREHUMAN+=0
        SCOREAI+=0
    if player == 'colors':
        if sum2==1 and sum1==3:
            SCOREAI+=1
        elif sum3==1 and sum1==3:
            SCOREAI+=1
        elif sum4==1 and sum1==3:
            SCOREHUMAN+=1
        elif sum5==1 and sum1==3:
            SCOREHUMAN+=1
        elif sum2==2 and sum1==2:
            SCOREAI+=10
        elif sum3==2 and sum1==2:
            SCOREAI+=10
        elif sum4==2 and sum1==2:
            SCOREHUMAN+=10
        elif sum5==2 and sum1==2:
            SCOREHUMAN+=10
        elif sum2==3 and sum1==1:
            SCOREAI+=50
        elif sum3==3 and sum1==1:
            SCOREAI+=50
        elif sum4==3 and sum1==1:
            SCOREHUMAN+=50
        elif sum5==3 and sum1==1:
            SCOREHUMAN+=50
        elif sum2==4 and sum1==0:
            SCOREAI+=512
        elif sum3==4 and sum1==0:
            SCOREAI+=512
        elif sum4==4 and sum1==0:
            SCOREHUMAN+=512
        elif sum5==4 and sum1==0:
            SCOREHUMAN+=512
    else:
        if sum4==1 and sum1==3:
            SCOREAI+=1
        elif sum5==1 and sum1==3:
            SCOREAI+=1
        elif sum2==1 and sum1==3:
            SCOREHUMAN+=1
        elif sum3==1 and sum1==3:
            SCOREHUMAN+=1
        elif sum4==2 and sum1==2:
            SCOREAI+=10
        elif sum5==2 and sum1==2:
            SCOREAI+=10
        elif sum2==2 and sum1==2:
            SCOREHUMAN+=10
        elif sum3==2 and sum1==2:
            SCOREHUMAN+=10
        elif sum4==3 and sum1==1:
            SCOREAI+=50
        elif sum5==3 and sum1==1:
            SCOREAI+=50
        elif sum2==3 and sum1==1:
            SCOREHUMAN+=50
        elif sum3==3 and sum1==1:
            SCOREHUMAN+=50
        elif sum4==4 and sum1==0:
            SCOREAI+=512
        elif sum5==4 and sum1==0:
            SCOREAI+=512
        elif sum2==4 and sum1==0:
            SCOREHUMAN+=512
        elif sum3==4 and sum1==0:
            SCOREHUMAN+=512
    return SCOREAI,SCOREHUMAN
def hurestic_overallfunction(list,player):
    SCOREHUMAN =0
    SCOREAI=0
    for i in range(len(list)):
        for j in range(0,len(list[i])-3):
            if player =='colors':
                scoreai,scorehuman = hurestic_function(list[i][j],list[i][j+1],list[i][j+2],list[i][j+3],player)
                SCOREAI += scoreai
                SCOREHUMAN += scorehuman
            else:
                scoreai,scorehuman = hurestic_function(list[i][j],list[i][j+1],list[i][j+2],list[i][j+3],player)
                SCOREAI += scoreai
                SCOREHUMAN += scorehuman
    return SCOREAI,SCOREHUMAN

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
                # drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                level2value = lastminfunction(board, board2, depth - 1, dotscolor,list1)
                value=max(value,level2value)
                maxvalues.append(level2value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                # remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
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
                transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                list1.append(transfermove)
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                # drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                level2value = lastminfunction(board, board2, depth - 1, dotscolor,list1)
                value=max(value,level2value)
                maxvalues.append(level2value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                # remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
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
    for k in range(0,len(candidate1)):
        # if candidate1[k][2] == list1[len(list1) - 1][4] and candidate1[k][3] == list1[len(list1) - 1][5]:
        #     if candidate1[k][0] == which_cindex(list1[len(list1) - 1][2]) and candidate1[k][1] == 12 - int(
        #             list1[len(list1) - 1][3]):
        #         continue
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
                minmaxmove.append(returnindex(candidate1[k][1]))
                minmaxmove.append(str(12 - candidate1[k][0]).strip())
                minmaxmove.append(returnindex(candidate1[k][3]))
                minmaxmove.append(str(12 - candidate1[k][2]).strip())
                minmaxmove.append(return_card(candidate[j][2]))
                minmaxmove.append(returnindex(candidate[j][1]))
                minmaxmove.append(str(12 - candidate[j][0]).strip())
                cardid = samecard(minmaxmove, candidate1[k][1], candidate1[k][3], list1, '')
                if cardid == minmaxmove[4]:
                    continue
                elif cardid == 'notpass':
                    continue
                elif cardid == '':
                    continue
                elif cardid == "colerror":
                    continue
                if candidate1[k][2]==list1[-1][4] and candidate1[k][3]==list1[-1][5]:
                    continue
                recycling_list = []
                recycling_list.append('0')
                recycling_list.append(return_card(candidate[j][2]))
                recycling_list.append(returnindex(candidate[j][1]))
                recycling_list.append(str(12 - candidate[j][0]).strip())
                transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                list1.append(transfermove)
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])

                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                bestvalue = maxfunction(board, board2, depth - 1, opponent)
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])

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

                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                level2value = lastminaphabeta(board, board2, depth - 1, alpha, beta, dotscolor,list1)
                value=max(value,level2value)
                maxvalues.append(level2value)
                alpha = max(alpha, value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])

                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            fakelist = []
            if largestvalue == values[i][0]:
                fakelist.append(values[i][1])
                fakelist.append(values[i][2])
                fakelist.append(values[i][3])
                fakelist.append(values[i][0])
                coordinate.append(fakelist)

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

                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                level2value = lastminaphabeta(board, board2, depth - 1, alpha, beta, dotscolor,list1)
                value = max(value, level2value)
                maxvalues.append(level2value)
                alpha = max(alpha, value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])

                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            fakelist = []
            if largestvalue == values[i][0]:
                fakelist.append(values[i][1])
                fakelist.append(values[i][2])
                fakelist.append(values[i][3])
                fakelist.append(values[i][0])

            else:
                continue
            coordinate.append(fakelist)
        # g = random.randint(0, len(coordinate) - 1)
        return coordinate[0][0], coordinate[0][1], coordinate[0][2], coordinate[0][3], maxvalues
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
                minmaxmove.append(returnindex(candidate1[k][1]))
                minmaxmove.append(str(12-candidate1[k][0]).strip())
                minmaxmove.append(returnindex(candidate1[k][3]))
                minmaxmove.append(str(12-candidate1[k][2]).strip())
                minmaxmove.append(return_card(candidate[j][2]))
                minmaxmove.append(returnindex(candidate[j][1]))
                minmaxmove.append(str(12-candidate[j][0]).strip())
                cardid = samecard(minmaxmove, candidate1[k][1], candidate1[k][3], list1, '')
                if cardid == minmaxmove[4]:
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
                recycling_list.append(str(12-candidate[j][0]).strip())
                transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                list1.append(transfermove)
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])

                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                value = min(value,recyclingmaxaplhabetapurning(board, board2, depth - 1,alpha,beta,opponent,list1))
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])

                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                beta = min(beta, value)
                if beta <= alpha:
                    global cut_count
                    cut_count += 1
                    drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                                   candidate1[k][3], candidate1[k][4])
                    return beta


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

                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                level2value = minfunction(board, board2, depth - 1, dotscolor)
                value=max(value,level2value)
                maxvalues.append(level2value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])

                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            if largestvalue == values[i][0]:
                fakelist = []
                if largestvalue == values[i][0]:
                    fakelist.append(values[i][1])
                    fakelist.append(values[i][2])
                    fakelist.append(values[i][3])
                    fakelist.append(values[i][0])
                    coordinate.append(fakelist)

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
                # drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                level2value = minfunction(board, board2, depth - 1, dotscolor)
                value=max(value,level2value)
                maxvalues.append(level2value)
                values.append([value, candidate[j][0], candidate[j][1], candidate[j][2]])
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                # remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            fakelist = []
            if largestvalue == values[i][0]:
                fakelist.append(values[i][1])
                fakelist.append(values[i][2])
                fakelist.append(values[i][3])
                fakelist.append(values[i][0])

            else:
                continue
            coordinate.append(fakelist)
        g = random.randint(0, len(coordinate) - 1)
        return coordinate[g][0], coordinate[g][1], coordinate[g][2], coordinate[g][3], maxvalues

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

            drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            bestvalue = minfunction(board, board2,depth - 1,opponent)
            remove_piece(board,candidate[j][0],candidate[j][1],candidate[j][2])

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
            # drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
            drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            bestvalue = maxfunction(board, board2, depth - 1, opponent)
            remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
            # remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
            remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            if bestvalue < value:
                value = bestvalue
    return value




def alphabetapruning(board,board2,depth,alpha,beta,dotscolor):
    values = []
    maxvalues = []
    coordinate = []
    candidate=[]
    historylist=[]
    value = -1000000000
    global search_count
    if dotscolor=='colors':

        list = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in list:
            piece = which_card(i)
            candidate_eachpiece = blanklist(board, piece)
            candidate.append(candidate_eachpiece)
        for k in range(len(candidate)):
            for j in range(len(candidate[k])):
                neighbor = isalone(board3,candidate[k][j][0],candidate[k][j][1],candidate[k][j][2])
                if neighbor==True:
                    continue
                else:
                    search_count += 1
                    drop_piece(board, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2])

                    drop_piece3(board3, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2])
                    level2value = alphabetapruningminfunction(board, board2, depth - 1, alpha, beta, dotscolor,historylist)
                    value = max(value, level2value)
                    maxvalues.append(level2value)
                    alpha = max(alpha, value)
                    values.append([level2value, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2]])
                    remove_piece(board, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2])

                    remove_piece3(board3, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            fakelist=[]
            if largestvalue == values[i][0]:
                fakelist.append(values[i][1])
                fakelist.append(values[i][2])
                fakelist.append(values[i][3])
                fakelist.append(values[i][0])

            else:
                continue
            coordinate.append(fakelist)

    elif dotscolor=='dots':

        list = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in list:
            piece = which_card(i)
            candidate_eachpiece = blanklist(board, piece)
            candidate.append(candidate_eachpiece)
        for k in range(len(candidate)):
            for j in range(len(candidate[k])):
                neighbor = isalone(board3,candidate[k][j][0],candidate[k][j][1],candidate[k][j][2])
                if neighbor==True:
                    continue
                else:
                    search_count += 1
                    drop_piece(board, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2])
                    drop_piece3(board3, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2])
                    level2value = alphabetapruningminfunction(board, board2, depth - 1, alpha, beta, dotscolor,historylist)
                    value = max(value, level2value)
                    maxvalues.append(level2value)
                    alpha = max(alpha, value)
                    values.append([level2value, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2]])
                    remove_piece(board, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2])
                    remove_piece3(board3, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2])
        largestvalue = max(maxvalues)
        for i in range(len(values)):
            fakelist=[]
            if largestvalue == values[i][0]:
                fakelist.append(values[i][1])
                fakelist.append(values[i][2])
                fakelist.append(values[i][3])
                fakelist.append(values[i][0])
            else:
                continue
            coordinate.append(fakelist)
    g = random.randint(0,len(coordinate)-1)
    for i in range(len(values)):
        values[i][3]= return_card(values[i][3])
    return coordinate[0][0], coordinate[0][1], coordinate[0][2],coordinate[0][3],values

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def alphabetapruningmaxfunction(board,board2,depth,alpha,beta,player) :
    opponent = SwitchPlayer(player)
    value = -1000000000
    if (depth == 0):
        #return evaluation(board,board2,board3,opponent)
        return evaluation_2(board,opponent)
    list = ['1', '2', '3', '4', '5', '6', '7', '8']
    for i in list:
        piece = which_card(i)
        candidate = blanklist(board, piece)
        for j in range(len(candidate)):
            global search_count
            search_count += 1
            drop_piece(board,candidate[j][0],candidate[j][1],candidate[j][2])

            drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            value = max(value,alphabetapruningminfunction(board, board2,depth - 1,alpha,beta,opponent))
            remove_piece(board,candidate[j][0],candidate[j][1],candidate[j][2])

            remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
            alpha = max(alpha, value)
            if alpha >= beta:
                global cut_count
                cut_count+=1
                return alpha
    return value
def alphabetapruningminfunction(board,board2,depth,alpha,beta,player,historylist):
    opponent = SwitchPlayer(player)
    value = 1000000000
    candidate = []
    if (depth == 0):
        return evaluation(board, board2,board3,opponent)
    list = ['1', '2', '3', '4', '5', '6', '7', '8']
    for i in list:
        piece = which_card(i)
        candidate_eachpiece = blanklist(board, piece)
        candidate.append(candidate_eachpiece)
    for k in range(len(candidate)):
        for j in range(len(candidate[k])):
            neighbor = isalone(board3, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2])
            if neighbor==True:
                continue
            else:
                allsame,historyvalue = history_list(board,candidate[k][j][0], candidate[k][j][1], candidate[k][j][2],historylist)
                if allsame==True:
                    value = min(value,historyvalue)
                    beta = min(beta, value)
                    if beta <= alpha:
                        global cut_count
                        cut_count += 1
                        return beta

                else:
                    global search_count
                    search_count += 1
                    drop_piece(board, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2])
                    drop_piece3(board3, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2])
                    newvalue = alphabetapruningmaxfunction(board, board2, depth - 1, alpha, beta, opponent)
                    value = min(value, newvalue)
                    fakelist2=[]
                    for r in range(COL_COUNT):
                        for c in range(ROW_COUNT):
                            if board[r][c] != '□□':
                                fakelist2.append(r)
                                fakelist2.append(c)
                                fakelist2.append(board[r][c])
                            else:
                                continue
                    fakelist2.append(newvalue)
                    historylist.append(fakelist2)
                    remove_piece(board, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2])
                    remove_piece3(board3, candidate[k][j][0], candidate[k][j][1], candidate[k][j][2])
                    beta = min(beta, value)
                    if beta <= alpha:
                        # global  cut_count
                        cut_count += 1
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

                    recycling_list = []
                    recycling_list.append('0')
                    recycling_list.append(return_card(candidate[j][2]))
                    recycling_list.append(returnindex(candidate[j][1]))
                    recycling_list.append(str(12-candidate[j][0]).strip())
                    transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                    list1.append(transfermove)
                    drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    # drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                    drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                    level2value =  minrecycling(board, board2, depth - 1, dotscolor,list1)
                    value = max(value,level2value)
                    maxvalues.append(level2value)
                    values.append([value, candidate1[k][0],candidate1[k][1],candidate1[k][2],candidate1[k][3],candidate[j][0], candidate[j][1], candidate[j][2]])
                    del list1[-1]
                    remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    # remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
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
            # if candidate1[k][2] == list1[len(list1) - 1][4] and candidate1[k][3] == list1[len(list1) - 1][5]:
            #     if candidate1[k][0] == which_cindex(list1[len(list1) - 1][2]) and candidate1[k][1] == 12 - int(
            #             list1[len(list1) - 1][3]):
            #         continue
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
                    recycling_list = []
                    recycling_list.append('0')
                    recycling_list.append(return_card(candidate[j][2]))
                    recycling_list.append(returnindex(candidate[j][1]))
                    recycling_list.append(str(12-candidate[j][0]).strip())
                    transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                    list1.append(transfermove)
                    drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    # drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                    drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                    level2value = minrecycling(board, board2, depth - 1, dotscolor, list1)
                    value = max(value, level2value)
                    maxvalues.append(level2value)
                    values.append([value, candidate1[k][0],candidate1[k][1],candidate1[k][2],candidate1[k][3],candidate[j][0], candidate[j][1], candidate[j][2]])
                    del list1[-1]
                    remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    # remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
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

                recycling_list = []
                recycling_list.append('0')
                recycling_list.append(return_card(candidate[j][2]))
                recycling_list.append(returnindex(candidate[j][1]))
                recycling_list.append(str(12-candidate[j][0]).strip())
                transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                list1.append(transfermove)
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                # drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                bestvalue= minrecycling(board, board2, depth - 1, dotscolor,list1)
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                # remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
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
                recycling_list = []
                recycling_list.append('0')
                recycling_list.append(return_card(candidate[j][2]))
                recycling_list.append(returnindex(candidate[j][1]))
                recycling_list.append(str(12-candidate[j][0]).strip())
                transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                list1.append(transfermove)
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                # drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                bestvalue = maxrecycling(board, board2, depth - 1, opponent,list1)
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                # remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
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
                    recycling_list = []
                    recycling_list.append('0')
                    recycling_list.append(return_card(candidate[j][2]))
                    recycling_list.append(returnindex(candidate[j][1]))
                    recycling_list.append(str(12 - candidate[j][0]).strip())
                    transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0],
                                                   candidate[j][2])
                    list1.append(transfermove)
                    drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    # drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                    drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                    level2value= recyclingminaplhabetapurning(board, board2, depth - 1, alpha,beta,dotscolor, list1)
                    value = max(value, level2value)
                    maxvalues.append(level2value)
                    alpha = max(alpha, value)
                    values.append([value, candidate1[k][0], candidate1[k][1], candidate1[k][2], candidate1[k][3],
                                   candidate[j][0], candidate[j][1], candidate[j][2]])
                    del list1[-1]
                    remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    # remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
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
            # if candidate1[k][2] == list1[len(list1) - 1][4] and candidate1[k][3] == list1[len(list1) - 1][5]:
            #     if candidate1[k][0] == which_cindex(list1[len(list1) - 1][2]) and candidate1[k][1] == 12 - int(
            #             list1[len(list1) - 1][3]):
            #         continue
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

                    recycling_list = []
                    recycling_list.append('0')
                    recycling_list.append(return_card(candidate[j][2]))
                    recycling_list.append(returnindex(candidate[j][1]))
                    recycling_list.append(str(12 - candidate[j][0]).strip())
                    transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0],
                                                   candidate[j][2])
                    list1.append(transfermove)
                    drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                    # drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
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
                    # remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
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
        # if candidate1[k][2] == list1[len(list1) - 1][4] and candidate1[k][3] == list1[len(list1) - 1][5]:
        #     if candidate1[k][0] == which_cindex(list1[len(list1) - 1][2]) and candidate1[k][1] == 12 - int(
        #             list1[len(list1) - 1][3]):
        #         continue
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
                recycling_list = []
                recycling_list.append('0')
                recycling_list.append(return_card(candidate[j][2]))
                recycling_list.append(returnindex(candidate[j][1]))
                recycling_list.append(str(12-candidate[j][0]).strip())
                transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                list1.append(transfermove)
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                # drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                value = min(value,recyclingmaxaplhabetapurning(board, board2, depth - 1,alpha,beta,opponent,list1))
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                # remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                beta = min(beta, value)
                if beta <= alpha:
                    global cut_count
                    cut_count += 1
                    drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                                   candidate1[k][3], candidate1[k][4])
                    return beta


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
                recycling_list = []
                recycling_list.append('0')
                recycling_list.append(return_card(candidate[j][2]))
                recycling_list.append(returnindex(candidate[j][1]))
                recycling_list.append(str(12-candidate[j][0]).strip())
                transfermove = cardinformation(recycling_list, candidate[j][1], candidate[j][0], candidate[j][2])
                list1.append(transfermove)
                drop_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                # drop_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                drop_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                value = max(value,recyclingminaplhabetapurning(board, board2,depth - 1,alpha,beta,opponent,list1))
                del list1[-1]
                remove_piece(board, candidate[j][0], candidate[j][1], candidate[j][2])
                # remove_piece2(board2, candidate[j][0], candidate[j][1], candidate[j][2])
                remove_piece3(board3, candidate[j][0], candidate[j][1], candidate[j][2])
                alpha = max(alpha, value)
                if alpha >= beta:
                    global cut_count
                    cut_count += 1
                    drop_recycling(board, board2, board3, candidate1[k][0], candidate1[k][1], candidate1[k][2],
                                   candidate1[k][3], candidate1[k][4])
                    return alpha


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
                    elif recyclelist[recyclelist.index(j)][3] == move[3]:
                        if 12 - recyclelist[recyclelist.index(j)][5] == int(move[1]):
                            if recyclelist.index(j) < len(recyclelist) - 1:
                                if move[5] == move[0] == move[2] == recyclelist[recyclelist.index(j)][2] and move[6] == move[3] == \
                                        recyclelist[recyclelist.index(j)][3]:
                                    card_id = recyclelist[recyclelist.index(j)][1]
                                    return card_id
                                else:
                                    card_id = 'pass'
                                    continue

                            else:
                                if move[0] == recyclelist[recyclelist.index(j)][2] and move[3] == recyclelist[recyclelist.index(j)][3]:
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
                                if move[1] == recyclelist[recyclelist.index(j)][3] and move[0]==recyclelist[recyclelist.index(j)][2]:
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
                                if move[1] == recyclelist[recyclelist.index(j)][3] and move[2]==recyclelist[recyclelist.index(j)][2]:
                                    card_id = 'notpass'
                                    return card_id

                        else:
                            continue
                    else:
                        continue
    return card_id
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def play(user1,user2,turn,game_over,aiorhuman,dotscolor,aifirst):
    firstuser=[]
    while not game_over:
        global en_count
        global orpurning
        if turn==0:
            if aiorhuman=='AI':
                orpurning=0
                print("It’s the turn of AI")
                en_count=0
                if aifirst==True:
                    drop = drop_piece(board, 11, 0, which_card('2'))
                    aifirst=False
                    if drop:
                        move = []
                        move.append('0')
                        move.append('2')
                        move.append('A')
                        move.append(str(1).strip())
                        for i in move:
                            print(i.strip() + '')
                        transfermove = cardinformation(move, 0, 11, which_card('2'))
                        firstuser.append(transfermove)


                        drop_piece3(board3, 11, 0, which_card('2'))
                else:

                    usercmd= input('Does AI activate alpha-beta? (y/n) : ')
                    start = timeit.default_timer()
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
                    stop = timeit.default_timer()
                    print('Time: ', stop - start,'S')
                    if drop:
                        colindex = returnindex(coordinate[1])
                        move = []
                        move.append('0')
                        move.append(return_card(coordinate[2]))
                        move.append(colindex)
                        move.append(str(12-coordinate[0]).strip())
                        for i in move:
                            print(i.strip()+'')
                        transfermove = cardinformation(move, coordinate[1], coordinate[0], coordinate[2])
                        firstuser.append(transfermove)


                        drop_piece3(board3, coordinate[0], coordinate[1], coordinate[2])

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
                            for i in move:
                                print(i.strip()+'')
                            drop_piece3(board3, rindex, cindex, card)
                            transfermove = cardinformation(move,cindex,rindex,card)
                            firstuser.append(transfermove)


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
                if aifirst==True:
                    drop = drop_piece(board,11,0, which_card('2'))
                    aifirst = False
                    if drop:
                        move = []
                        move.append('0')
                        move.append('2')
                        move.append('A')
                        move.append(str(1).strip())
                        for i in move:
                            print(i.strip() + '')
                        transfermove = cardinformation(move, 0, 11, which_card('2'))
                        firstuser.append(transfermove)

                        drop_piece3(board3, 11, 0, which_card('2'))
                else:

                    usercmd= input('Does AI activate alpha-beta? (y/n) : ')
                    start = timeit.default_timer()
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
                    stop = timeit.default_timer()
                    print('Time: ', stop - start,'S')
                    if drop:
                        colindex = returnindex(coordinate[1])
                        move = []
                        move.append('0')
                        move.append(return_card(coordinate[2]))
                        move.append(colindex)
                        move.append(str(12-coordinate[0]).strip())
                        for i in move:
                            print(i.strip()+'')
                        transfermove = cardinformation(move, coordinate[1], coordinate[0], coordinate[2])
                        firstuser.append(transfermove)


                        drop_piece3(board3, coordinate[0], coordinate[1], coordinate[2])

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
                            for i in move:
                                print(i.strip()+'')
                            transfermove = cardinformation(move, cindex, rindex, card)
                            firstuser.append(transfermove)

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
                start = timeit.default_timer()
                if usercmd.lower().startswith('y'):
                    if sum==59:

                        DEPTH=1
                        coordinate = alphabetapurningrecycling(board,board2, DEPTH, -99999999, 99999999,dotscolor,recyclelist)
                        orpurning=1
                    else:
                        DEPTH=2
                        coordinate = alphabetapurningrecycling(board,board2, DEPTH, -99999999, 99999999,dotscolor,recyclelist)
                        orpurning=1
                else:
                    if sum==59:

                        DEPTH=1
                        coordinate = minmaxrecycliing(board, board2, DEPTH, dotscolor, recyclelist)
                        orpurning = 2
                    else:
                        DEPTH=2
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
                stop = timeit.default_timer()
                print('Time: ', stop - start)
                if drop:
                    sum+=1
                    move=[]
                    move.append(returnindex(coordinate[1]))
                    move.append(str(12 - coordinate[0]).strip())
                    move.append(returnindex(coordinate[3]))
                    move.append(str(12 - coordinate[2]).strip())
                    move.append(return_card(coordinate[6]))
                    move.append(returnindex(coordinate[5]))
                    move.append(str(12 - coordinate[4]).strip())
                    for i in move:
                        print(i.strip()+'')
                    colindex = returnindex(coordinate[5])
                    recyclinglist = []
                    recyclinglist.append('0')
                    recyclinglist.append(return_card(coordinate[6]))
                    recyclinglist.append(colindex)
                    recyclinglist.append(str(12-coordinate[4]).strip())
                    transfermove = cardinformation(recyclinglist, coordinate[5], coordinate[4], coordinate[6])
                    recyclelist.append(transfermove)

                    drop_piece3(board3, coordinate[4], coordinate[5], coordinate[6])

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
                            for i in move:
                                print(i.strip()+'')
                            recyclinglist=[]
                            recyclinglist.append('0')
                            recyclinglist.append(move[4])
                            recyclinglist.append(move[5])
                            recyclinglist.append(move[6])
                            transfermove = cardinformation(recyclinglist, cindex3, rindex, card)
                            recyclelist.append(transfermove)
                            drop_piece3(board3, rindex, cindex3, card)


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
                start = timeit.default_timer()
                if usercmd.lower().startswith('y'):
                    if sum == 59:

                        DEPTH = 1
                        coordinate = alphabetapurningrecycling(board, board2, DEPTH, -99999999, 99999999, dotscolor,
                                                               recyclelist)
                        orpurning = 1
                    else:
                        DEPTH=2
                        coordinate = alphabetapurningrecycling(board, board2, DEPTH, -99999999, 99999999, dotscolor,
                                                               recyclelist)
                        orpurning = 1
                else:
                    if sum == 59:

                        DEPTH = 1
                        coordinate = minmaxrecycliing(board, board2, DEPTH, dotscolor, recyclelist)
                        orpurning = 2
                    else:
                        DEPTH =2
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
                stop = timeit.default_timer()
                print('Time: ', stop - start)
                if drop:
                    sum+=1
                    move=[]
                    move.append(returnindex(coordinate[1]))
                    move.append(str(12 - coordinate[0]).strip())
                    move.append(returnindex(coordinate[3]))
                    move.append(str(12 - coordinate[2]).strip())
                    move.append(return_card(coordinate[6]))
                    move.append(returnindex(coordinate[5]))
                    move.append(str(12 - coordinate[4]).strip())
                    for i in move:
                        print(i.strip()+'')
                    colindex = returnindex(coordinate[5])
                    recyclinglist = []
                    recyclinglist.append('0')
                    recyclinglist.append(return_card(coordinate[6]))
                    recyclinglist.append(colindex)
                    recyclinglist.append(str(12-coordinate[4]).strip())
                    transfermove = cardinformation(recyclinglist, coordinate[5], coordinate[4], coordinate[6])
                    recyclelist.append(transfermove)

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
                            for i in move:
                                print(i.strip()+'')
                            recyclinglist=[]
                            recyclinglist.append('0')
                            recyclinglist.append(move[4])
                            recyclinglist.append(move[5])
                            recyclinglist.append(move[6])
                            transfermove = cardinformation(recyclinglist, cindex3, rindex, card)
                            recyclelist.append(transfermove)
                            drop_piece3(board3, rindex, cindex3, card)

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
        AIFIRST=True
    else:
        AIORHUMAN = 'human'
        user1,user2,turn,dotscolor = PlayerOption(AIORHUMAN)
        AIFIRST=False
    game_over = False
    board = create_board()
    board2 = create_board2()
    board3 = create_board()
    print(*board, sep='\n')
    play(user1,user2,turn,game_over,AIORHUMAN,dotscolor,AIFIRST)

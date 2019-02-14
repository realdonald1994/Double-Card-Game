from card import Card
ROW_COUNT = 8
COL_COUNT = 12


def create_board():
    board = [['□□' for _ in range(ROW_COUNT)] for _ in range(COL_COUNT)]
    return board
def remove(board,raw1,col1,raw2,col2):

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
        else:

            if board[raw-2][col]=='□□':
                board[raw1][col1] = '□□'
                board[raw2][col2] = '□□'
                return True
            else:
                return False
    elif turn==2:
        if raw==0:
            board[raw1][col1] = '□□'
            board[raw2][col2] = '□□'
        else:

            if board[raw-1][col]=='□□' and board[raw-1][col+1]=='□□':
                board[raw1][col1] = '□□'
                board[raw2][col2] = '□□'
                return True
            else:
                return False

def is_valid2(move1,move2):
    if 0 > int(move1) or int(move1) > COL_COUNT or 0 > int(move2) or int(move2)> COL_COUNT:
        return False
    return True
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
        if row==11:
            if board[row][col] == '□□' and board[row - 1][col] == '□□':
                board[row][col] = piece.below
                board[row - 1][col] = piece.top
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
                    board[row][col] = piece.below
                    board[row-1][col]=piece.top
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
        if row==11:
            if board[row][col] == '□□' and board[row - 1][col] == '□□':
                board[row][col] = piece.below
                board[row - 1][col] = piece.top
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
                    board[row][col] = piece.below
                    board[row-1][col]=piece.top
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
        if row==11:
            if board[row][col] == '□□' and board[row - 1][col] == '□□':
                board[row][col] = piece.below
                board[row - 1][col] = piece.top
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
                    board[row][col] = piece.below
                    board[row-1][col]=piece.top
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
        if row==11:
            if board[row][col] == '□□' and board[row - 1][col] == '□□':
                board[row][col] = piece.below
                board[row - 1][col] = piece.top
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
                    board[row][col] = piece.below
                    board[row-1][col]=piece.top
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

def winning_move(board,user1,user2):
    for c in range(ROW_COUNT-3):
        for r in range(COL_COUNT):
            if user1==1 and user2==2:
                if board[r][c][1]=='O'and board[r][c+1][1]=='O' and board[r][c+2][1] == 'O' and board[r][c+3][1] =='O':
                    return 1
                elif board[r][c][1] =='X' and board[r][c+1][1]=='X' and board[r][c+2][1]=='X'and board[r][c+3][1]=='X':
                    return 1
            elif user1==2 and user2==1:
                if board[r][c][0]=='W' and board[r][c+1][0]=='W' and board[r][c+2][0]=='W' and board[r][c+3][0]=='W':
                    return 0
                elif board[r][c][0]=='R' and board[r][c+1][0]=='R' and board[r][c+2][0]=='R' and board[r][c+3][0]=='R':
                    return 0


    for c in range(ROW_COUNT):
        for r in range(COL_COUNT-3):
            if user1==1 and user2==2:
                if board[r][c][1] =='O'and board[r+1][c][1] =='O'and board[r+2][c][1] =='O' and board[r+3][c][1] == 'O':
                    return 1
                elif board[r][c][1] =='X'and board[r+1][c][1] =='X'and board[r+2][c][1]=='X' and board[r+3][c][1]== 'X':
                    return 1
            elif user1 == 2 and user2 == 1:
                if board[r][c][0]=='W' and board[r+1][c][0]=='W' and board[r+2][c][0]=='W' and board[r+3][c][0]=='W':
                    return 0
                elif board[r][c][0]=='R' and board[r+1][c][0]=='R' and board[r+2][c][0]=='R' and board[r+3][c][0]=='R':
                    return 0

    for c in range(ROW_COUNT-3):
        for r in range(3,COL_COUNT):
            if user1==1 and user2==2:
                if board[r][c][1]=='O'and board[r-1][c+1][1]=='O'and board[r-2][c+2][1]=='O'and board[r-3][c+3][1]=='O':
                    return 1
                elif board[r][c][1]=='X'and board[r-1][c+1][1]=='X'and board[r-2][c+2][1]=='X'and board[r-3][c+3][1]=='X':
                    return 1
            elif user1 == 2 and user2 == 1:
                if board[r][c][0]=='W' and board[r-1][c+1][0]=='W' and board[r-2][c+2][0]=='W' and board[r-3][c+3][0]=='W':
                    return 0
                elif board[r][c][0]=='R' and board[r-1][c+1][0]=='R' and board[r-2][c+2][0]=='R' and board[r-3][c+3][0]=='R':
                    return 0

    for c in range(ROW_COUNT-3):
        for r in range(COL_COUNT-3):
            if user1==1 and user2==2:
                if board[r][c][1] =='O'and board[r+1][c+1][1]=='O'and board[r+2][c +2][1]=='O'and board[r+3][c+3][1]=='O':
                    return 1
                elif board[r][c][1] =='X'and board[r+1][c+1][1] =='X'and board[r+2][c+2][1]=='X'and board[r+3][c+3][1]=='X':
                    return 1
            elif user1 == 2 and user2 == 1:
                if board[r][c][0]=='W' and board[r+1][c+1][0]=='W' and board[r+2][c+2][0]=='W' and board[r+3][c+3][0]=='W':
                    return 0
                if board[r][c][0]=='R' and board[r+1][c+1][0]=='R' and board[r+2][c+2][0]=='R' and board[r+3][c+3][0]=='R':
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


def play(user1,user2,turn,game_over):
    firstuser=[]
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
                        print("drop failure")
                        print("try again")
                        continue
                    elif drop==True:
                        firstuser.append(move)
                    if user1==1:
                        win1 = winning_move(board, user1,user2)
                        win2 = winning_move(board, user2,user1)
                        if win1==1:
                            print(*board, sep='\n')
                            print(*board, sep='\n', file=open("output.txt", 'a'))
                            print("player {0} winning".format(user1))
                            print("player {0} winning".format(user1), file=open("output.txt", 'a'))
                            print("*****GAME END*****")
                            print("*****GAME END*****", file=open("output.txt", 'a'))
                            break
                        elif win2==0:
                            print(*board, sep='\n')
                            print(*board, sep='\n', file=open("output.txt", 'a'))
                            print("player {0} winning".format(user2))
                            print("player {0} winning".format(user2), file=open("output.txt", 'a'))
                            print("*****GAME END*****")
                            print("*****GAME END*****", file=open("output.txt", 'a'))
                            break
                    elif user1==2:
                        win1 = winning_move(board, user2,user1)
                        win2 = winning_move(board, user1, user2)
                        if win1==1:
                            print(*board, sep='\n')
                            print(*board, sep='\n', file=open("output.txt", 'a'))
                            print("player {0} winning".format(user1))
                            print("player {0} winning".format(user1), file=open("output.txt", 'a'))
                            print("*****GAME END*****")
                            print("*****GAME END*****", file=open("output.txt", 'a'))
                            break
                        elif win2==0:
                            print(*board, sep='\n')
                            print(*board, sep='\n', file=open("output.txt", 'a'))
                            print("player {0} winning".format(user2))
                            print("player {0} winning".format(user2), file=open("output.txt", 'a'))
                            print("*****GAME END*****")
                            print("*****GAME END*****", file=open("output.txt", 'a'))
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
                        print("drop failure")
                        print("try again")
                        continue
                    elif drop==True:
                        firstuser.append(move)
                    if user2==1:
                        win1 = winning_move(board, user1,user2)
                        win2 = winning_move(board, user2, user1)
                        if win1==0:
                            print(*board, sep='\n')
                            print(*board, sep='\n', file=open("output.txt", 'a'))
                            print("player {0} winning".format(user2))
                            print("player {0} winning".format(user2), file=open("output.txt", 'a'))
                            print("*****GAME END*****")
                            print("*****GAME END*****", file=open("output.txt", 'a'))
                            break
                        elif win2==1:
                            print(*board, sep='\n')
                            print(*board, sep='\n', file=open("output.txt", 'a'))
                            print("player {0} winning".format(user1))
                            print("player {0} winning".format(user1), file=open("output.txt", 'a'))
                            print("*****GAME END*****")
                            print("*****GAME END*****", file=open("output.txt", 'a'))
                            break
                    elif user2==2:
                        win1 = winning_move(board, user2,user1)
                        win2 = winning_move(board, user1,user2)
                        if win1==0:
                            print(*board, sep='\n')
                            print(*board, sep='\n', file=open("output.txt", 'a'))
                            print("player {0} winning".format(user2))
                            print("player {0} winning".format(user2), file=open("output.txt", 'a'))
                            print("*****GAME END*****")
                            print("*****GAME END*****", file=open("output.txt", 'a'))
                            break
                        elif win2==1:
                            print(*board, sep='\n')
                            print(*board, sep='\n', file=open("output.txt", 'a'))
                            print("player {0} winning".format(user1))
                            print("player {0} winning".format(user1), file=open("output.txt", 'a'))
                            print("*****GAME END*****")
                            print("*****GAME END*****", file=open("output.txt", 'a'))
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
        print(*board, sep='\n', file=open("output.txt", 'a'))
        turn +=1
        turn=turn % 2
        print("Overall steps: ",end="")
        print("Overall steps: ", end="", file=open("output.txt", 'a'))
        print(len(firstuser))
        print(len(firstuser), file=open("output.txt", 'a'))
        if(len(firstuser)==24):
            print("In regualr game, game ends in a draw. They need go head to next section")
            print("In regualr game, game ends in a draw. They need go head to next section", file=open("output.txt", 'a'))
            lastcol = firstuser[23][2]
            lastraw = firstuser[23][3]
            sum = len(firstuser)
            recycling(firstuser,game_over,user1,user2,turn,lastcol,lastraw,sum)
            break
def recycling(list1,game_over,user1,user2,turn,lastcol,lastraw,sum):
    global remo
    global remove
    global card_id
    global newcol
    global newraw
    global newcindex
    global lastcindex
    while not game_over:
        if turn == 0:
            move = input("Input a slot player {0}: ".format(user1))
            sum+=1
            move = move.split(' ')
            cindex1 = which_cindex(move[0])
            cindex2 = which_cindex(move[2])
            newcol=min(move[0],move[2])
            newcindex = which_cindex(newcol)
            lastcindex = which_cindex(lastcol)
            newraw= min(move[1],move[3])
            if cindex1==UnboundLocalError or cindex2==UnboundLocalError :
                continue
            if move[0]==move[2]:
                num=1
                minmove=move[0]
            else:
                num=2
                minmove=min(move[0],move[2])
            if num==1:
                for j in list1:
                    for i in j:
                        if minmove==i:
                            if list1[list1.index(j)][3]==move[1] or int(list1[list1.index(j)][3])==int(move[1])-1:
                                card_id = list1[list1.index(j)][1]
                            else:
                                continue
            elif num==2:
                for j in list1:
                    for i in j:
                        if minmove==i:

                            if list1[list1.index(j)][3]==move[1] or list1[list1.index(j)][3]==move[3]:
                                card_id = list1[list1.index(j)][1]
                            else:
                                continue

            if newcindex==lastcindex and int(lastraw)==int(newraw):
                print("cannot place card in other player just placed")
                print("try again")
                continue




            if is_valid2(move[1],move[3]):
                rindex1 = 12 - int(move[1])
                rindex2 = 12 - int(move[3])
                remo = remove(board,rindex1,cindex1,rindex2,cindex2)
                if remo==False:
                    print("remove failure")
                    print("try again")
                    continue
            else:
                print("not valid")
                print("try again")
                continue
            if move[4]==card_id:
                print("cannot be same direction")
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
                    lastcol=move[5]
                    lastraw=move[6]
                if user1==1:
                    win1 = winning_move(board, user1, user2)
                    win2 = winning_move(board, user2, user1)
                    if win1 == 1:
                        print(*board, sep='\n')
                        print(*board, sep='\n',file=open("output.txt", 'a'))
                        print("player {0} winning".format(user1))
                        print("player {0} winning".format(user1),file=open("output.txt", 'a'))
                        print("*****GAME END*****")
                        print("*****GAME END*****",file=open("output.txt", 'a'))
                        break
                    elif win2 == 0:
                        print(*board, sep='\n')
                        print(*board, sep='\n',file=open("output.txt", 'a'))
                        print("player {0} winning".format(user2))
                        print("player {0} winning".format(user2),file=open("output.txt", 'a'))
                        print("*****GAME END*****")
                        print("*****GAME END*****",file=open("output.txt", 'a'))
                        break
                elif user1==2:
                    win1 = winning_move(board, user2, user1)
                    win2 = winning_move(board, user1, user2)
                    if win1 == 1:
                        print(*board, sep='\n')
                        print(*board, sep='\n',file=open("output.txt", 'a'))
                        print("player {0} winning".format(user1))
                        print("player {0} winning".format(user1),file=open("output.txt", 'a'))
                        print("*****GAME END*****")
                        print("*****GAME END*****",file=open("output.txt", 'a'))
                        break
                    elif win2 == 0:
                        print(*board, sep='\n')
                        print(*board, sep='\n',file=open("output.txt", 'a'))
                        print("player {0} winning".format(user2))
                        print("player {0} winning".format(user2),file=open("output.txt", 'a'))
                        print("*****GAME END*****")
                        print("*****GAME END*****",file=open("output.txt", 'a'))
                        break
            else:
                print("not valid")
                print("try again")
                continue

        else:
            move = input("Input a slot player {0}: ".format(user2))
            sum+=1
            move = move.split(' ')
            cindex1 = which_cindex(move[0])
            cindex2 = which_cindex(move[2])
            newcol=min(move[0],move[2])
            newcindex = which_cindex(newcol)
            lastcindex = which_cindex(lastcol)
            newraw= min(move[1],move[3])
            if cindex1==UnboundLocalError or cindex2==UnboundLocalError :
                continue
            if move[0]==move[2]:
                num=1
                minmove=move[0]
            else:
                num=2
                minmove=min(move[0],move[2])
            if num==1:
                for i in list1:
                    for j in i:
                        if minmove==j:
                            if list1[list1.index(i)][3]==move[1] or int(list1[list1.index(i)][3])==int(move[1])-1:
                                card_id = list1[list1.index(i)][1]
                            else:
                                continue
            elif num==2:
                for j in list1:
                    for i in j:
                        if minmove==i:
                            if list1[list1.index(j)][3]==move[1] or list1[list1.index(j)][3]==move[3]:
                                card_id = list1[list1.index(j)][1]
                            else:
                                continue

            if newcindex == lastcindex and int(lastraw) == int(newraw):
                print("cannot place card in other player just placed")
                print("try again")
                continue

            if is_valid2(move[1], move[3]):
                rindex1 = 12 - int(move[1])
                rindex2 = 12 - int(move[3])
                remo = remove(board, rindex1, cindex1, rindex2, cindex2)
                if remo == False:
                    print("remove failure")
                    print("try again")
                    continue
            else:
                print("not valid")
                print("try again")
                continue
            if move[4] == card_id:
                print("cannot be same direction")
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
                    lastcol = move[5]
                    lastraw = move[6]
                if user2==1:
                    win1 = winning_move(board, user1,user2)
                    win2 = winning_move(board, user2, user1)
                    if win1==0:
                        print(*board, sep='\n')
                        print(*board, sep='\n',file=open("output.txt", 'a'))
                        print("player {0} winning".format(user2))
                        print("player {0} winning".format(user2),file=open("output.txt", 'a'))
                        print("*****GAME END*****")
                        print("*****GAME END*****",file=open("output.txt", 'a'))
                        break
                    elif win2==1:
                        print(*board, sep='\n')
                        print(*board, sep='\n',file=open("output.txt", 'a'))
                        print("player {0} winning".format(user1))
                        print("player {0} winning".format(user1),file=open("output.txt", 'a'))
                        print("*****GAME END*****")
                        print("*****GAME END*****",file=open("output.txt", 'a'))
                        break
                elif user2==2:
                    win1 = winning_move(board, user2,user1)
                    win2 = winning_move(board, user1,user2)
                    if win1==0:
                        print(*board, sep='\n')
                        print(*board, sep='\n',file=open("output.txt", 'a'))
                        print("player {0} winning".format(user2))
                        print("player {0} winning".format(user2),file=open("output.txt", 'a'))
                        print("*****GAME END*****")
                        print("*****GAME END*****",file=open("output.txt", 'a'))
                        break
                    elif win2==1:
                        print(*board, sep='\n')
                        print(*board, sep='\n',file=open("output.txt", 'a'))
                        print("player {0} winning".format(user1))
                        print("player {0} winning".format(user1),file=open("output.txt", 'a'))
                        print("*****GAME END*****")
                        print("*****GAME END*****",file=open("output.txt", 'a'))
                        break
            else:
                print("not valid")
                print("try again")
                continue
        print(*board, sep='\n')
        print(*board, sep='\n',file=open("output.txt", 'a'))
        turn +=1
        turn=turn % 2
        print("Overall steps: ",end="")
        print("Overall steps: ", end="",file=open("output.txt", 'a'))
        print(sum)
        print(sum,file=open("output.txt", 'a'))
        if sum==36:
            print("After regualr and recycling game, game ends in a draw")
            print("After regualr and recycling game, game ends in a draw",file=open("output.txt", 'a'))
            break


if __name__ == '__main__':
    print("*****WELCOME TO DOUBLE-CARD GAME*****")
    print("*****WELCOME TO DOUBLE-CARD GAME*****",file=open("output.txt", 'a'))
    print("SUPPORT: "
          "W: White "
          "R: Red "
          "X: Solid "
          "O: Hollow")
    print("SUPPORT: "
          "W: White "
          "R: Red "
          "X: Solid "
          "O: Hollow",file=open("output.txt", 'a'))
    str = input("Player 1 will play dots or colors?")
    if str=="dots":
        print("Player1 choose dots")
        print("Player1 choose dots",file=open("output.txt", 'a'))
        print("Player2 choose colors")
        print("Player2 choose colors",file=open("output.txt", 'a'))
        user1=1
        user2=2
        turn =0
    elif(str=="colors"):
        print("Player1 choose colors")
        print("Player1 choose colors", file=open("output.txt", 'a'))
        print("Player2 choose dots")
        print("Player2 choose dots", file=open("output.txt", 'a'))
        user1=2
        user2=1
        turn =1
    else:
        print("try again")
        str = input("Player 1 will play dots or colors?")
        if str == "dots":
            print("Player1 choose dots")
            print("Player1 choose dots", file=open("output.txt", 'a'))
            print("Player2 choose colors")
            print("Player2 choose colors", file=open("output.txt", 'a'))
            user1 = 1
            user2 = 2
            turn = 0
        elif (str == "colors"):
            print("Player1 choose colors")
            print("Player1 choose colors", file=open("output.txt", 'a'))
            print("Player2 choose dots")
            print("Player2 choose dots", file=open("output.txt", 'a'))
            user1 = 2
            user2 = 1
            turn = 1
    game_over = False
    board = create_board()
    print(*board, sep='\n')
    print(*board, sep='\n', file=open("output.txt", 'a'))
    print("*****************************************************", file=open("output.txt", 'a'))
    play(user1,user2,turn,game_over)


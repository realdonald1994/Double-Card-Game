# -*- coding: utf-8 -*-

import copy

class ConnectFour:
    def __init__(self):
        self.moves = 0  #The count of moves, 42 moves is equal than board is full
        self.turn = 0  #Use this variable to recognize which one player turn is it

    def PrintGameBoard(self, board):
        print('  0   1   2   3   4   5   6') # This function just raws a board
        for i in range(5, -1, -1):
            print('|---|---|---|---|---|---|---|')
            print("| ",end="")
            for j in range(7):
                print(board[i][j],end="")
                if j != 6:
                    print(" | ",end="")
                else:
                    print(" |")
        print('`---------------------------´')

    def LegalRow(self, col, board):
        stacks = [[x[i] for x in board] for i in range(len(board[0]))] # This function checks stack of given column and return the row where you can draw mark. If the stack is full return -1
        countofitems = stacks[col].count("x") + stacks[col].count("o") # count of items in stack
        if (countofitems) < 6:
            return (countofitems)
        else:
            return -1

    def LegalMoves(self, board):
        legalmoves = []
        stacks = [[x[i] for x in board] for i in range(len(board[0]))]
        order = [3,2,4,1,5,0,6]
        for i in order:
            if self.LegalRow(i, board)!=-1:
                legalmoves.append(i)
        return legalmoves

    def MakeMove(self, board, col, player, row):
        board[row][col] = player # This function make a move and increases count of moves
        self.moves += 1
        return board

    def UnmakeMove(self, board, col, row):
        board[row][col] = " " # This function make a move and increases count of moves
        self.moves -= 1
        return board

    def IsWinning(self, currentplayer, board):
        for i in range(6): # This function returns True or False depending on if current player have four "tila" in a row (win)
            for j in range(4):
                if board[i][j] == currentplayer and board[i][j+1] == currentplayer and board[i][j+2] == currentplayer and board[i][j+3] == currentplayer:
                    return True
        for i in range(3):
            for j in range(7):
                if board[i][j] == currentplayer and board[i+1][j] == currentplayer and board[i+2][j] == currentplayer and board[i+3][j] == currentplayer:
                    return True
        for i in range(3):
            for j in range(4):
                if board[i][j] == currentplayer and board[i+1][j+1] == currentplayer and board[i+2][j+2] == currentplayer and board[i+3][j+3] == currentplayer:
                    return True
        for i in range(3,6):
            for j in range(4):
                if board[i][j] == currentplayer and board[i-1][j+1] == currentplayer and board[i-2][j+2] == currentplayer and board[i-3][j+3] == currentplayer:
                    return True
        return False

    def PlayerMove(self, board, player):
        allowedmove = False     # This function ask players move when its his turn and returns board after making move.
        while not allowedmove:
            try:
                print("Choose a column where you want to make your move (0-6): ",end="")
                col =input()
                col=int(col)
                row = self.LegalRow(col, board)
            except (NameError, ValueError, IndexError, TypeError, SyntaxError) as e:
                print("Give a number as an integer between 0-6!")
            else:
                if row != -1 and (col<=6 and col>=0):
                    board[row][int(col)] = player
                    self.moves += 1
                    allowedmove = True
                elif col>6 or col<0:
                    print("The range was 0-6!!!")
                else:
                    print("This column is full")
        return board

    def SwitchPlayer(self, player): # This function gives opponent player's mark
        if player=="x":
            nextplayer="o"
        else:
            nextplayer="x"
        return nextplayer

    def evaluation(self, board): # This function evaluate gameboard (heuristic). The rules of evaluation are in site: http://isites.harvard.edu/fs/docs/icb.topic788088.files/Assignment%203/asst3c.pdf
        list = []
        player = "x"
        opponent = "o"
        if self.IsWinning(player, board):
            score = -512
        elif self.IsWinning(opponent, board):
            score = +512
        elif self.moves==42:
            score=0
        else:
            score = 0
            for i in range(6):  #append to list horizontal segments
                for j in range(4):
                    list.append([str(board[i][j]),str(board[i][j+1]),str(board[i][j+2]),str(board[i][j+3])])
            for i in range(3): #append to list vertical segments
                for j in range(7):
                    list.append([str(board[i][j]),str(board[i+1][j]),str(board[i+2][j]),str(board[i+3][j])])
            for i in range(3): #append to list diagonal segments
                for j in range(4):
                    list.append([str(board[i][j]),str(board[i+1][j+2]),str(board[i+2][j+2]),str(board[i+3][j+3])])
            for i in range(3, 6): #append to list diagonal segments
                for j in range(4):
                    list.append([str(board[i][j]),str(board[i-1][j+2]),str(board[i-2][j+2]),str(board[i-3][j+3])])
            for k in range(len(list)): #add to score with rules of site above
                if ((list[k].count(str("x"))>0) and (list[k].count(str("o"))>0)) or list[k].count(" ")==4:
                    score += 0
                if list[k].count(player)==1 and list[k].count(opponent)==0:
                    score -= 1
                if list[k].count(player)==2 and list[k].count(opponent)==0:
                    score -= 10
                if list[k].count(player)==3 and list[k].count(opponent)==0:
                    score -= 50
                if list[k].count(opponent)==1 and list[k].count(player)==0:
                    score += 1
                if list[k].count(opponent)==2 and list[k].count(player)==0:
                    score += 10
                if list[k].count(opponent)==3 and list[k].count(player)==0:
                    score += 50
            if self.turn==player:
                score -= 16
            else:
                score += 16
        return score

    def maxfunction(self, board, depth, player, alpha, beta):
        opponent = self.SwitchPlayer(player)
        self.turn = opponent
        legalmoves = self.LegalMoves(board)
        if (depth==0) or self.moves==42:
            return self.evaluation(board)
        value=-1000000000
        for col in legalmoves:
            row = self.LegalRow(col, board)

            value = max(value, minfunction(board, depth-1, opponent,alpha, beta))
            newboard = self.UnmakeMove(board, col, row)
            if value >= beta:
                global cut_count
                cut_count += 1
                return value
            alpha = max(alpha, value)
        return value

    def minfunction(self, board, depth, opponent, alpha, beta):
        player = self.SwitchPlayer(opponent)
        self.turn = player
        legalmoves = self.LegalMoves(board)
        if (depth==0):
            return evaluation(board)
        value=1000000000
        for col in legalmoves:
            row = self.LegalRow(col, board)
            newboard = self.MakeMove(board, col, player, row)
            value = min(value, self.maxfunction(board, depth-1, player ,alpha, beta))
            newboard = self.UnmakeMove(board, col, row)
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value

    def alphabetapruning(self, board, depth, opponent, alpha, beta): #This is the alphabeta-function modified from: https://github.com/msaveski/connect-four
        values = []
        cols = []
        value = -1000000000
        for col in self.LegalMoves(board):
            row = self.LegalRow(col, board)
            board = self.MakeMove(board, col, opponent, row)
            value = max(value, self.minfunction(board, depth-1, opponent, alpha, beta))
            values.append(value)
            cols.append(col)
            board = self.UnmakeMove(board, col, row)
        largestvalue= max(values)
        print(cols)
        print(values)
        for i in range(len(values)):
            if largestvalue==values[i]:
                position = cols[i]
                return largestvalue, position

    def searchingfunction(self, board, depth, opponent):
        #This function update turn to opponent and calls alphabeta (main algorithm) and after that update new board (add alphabeta position to old board) and returns new board.
        newboard = copy.deepcopy(board)
        value, position=self.alphabetapruning(newboard, depth, opponent, -10000000000, 10000000000)
        board = self.MakeMove(board, position, opponent, self.LegalRow(position, board))
        return board

def PlayerGoesFirst():
    print("Player is X and AI is O") #This function just ask who goes first
    player = 'x'
    opponent = 'o'
    print('Do you want to play first? (y/n) : ',end="")
    return input().lower().startswith('y')

def PlayAgain():
    print('Do you want to play again? (y/n) :',end="") #This function ask if player want to play new game
    return input().lower().startswith('y')

def main():
    print("Connect4") #The main function. This ask player mark, initialize gameboard (table), print board after each turn, ask players move, make AI's move and checks after each move is game is tie/win or lose.
    print("-"*34)
    while True:
        connectfour = ConnectFour()
        gameisgoing = True
        table  = [[],[],[],[],[],[]]
        for i in range(7):
            for j in range(6):
                table[j].append(" ")
        player = "x"
        opponent = "o"
        if PlayerGoesFirst():
            turn = "x"
        else:
            turn = "o"
        while gameisgoing:
            connectfour.PrintGameBoard(table)
            if turn=="x":
                table = connectfour.PlayerMove(table, player)
                if connectfour.IsWinning(player, table):
                    connectfour.PrintGameBoard(table)
                    print('You won the game!')
                    gameisgoing = False
                else:
                    if connectfour.moves==42:
                        connectfour.PrintGameBoard(table)
                        print('Game is tie')
                        gameisgoing=False
                    else:
                        turn = "o"
            else:
                table = connectfour.searchingfunction(table, 6, opponent) #Here is AI's move. Takes as input current table (board), depth and opponents mark. Output should be new gameboard with AI's move.
                if connectfour.IsWinning(opponent, table):
                    connectfour.PrintGameBoard(table)
                    print('Computer won the game')
                    gameisgoing = False
                else:
                    if connectfour.moves==42:
                        connectfour.PrintGameBoard(table)
                        print('Game is tie')
                        gameisgoing=False
                    else:
                        turn = "x"
        if not PlayAgain():
            print("Game ended")
            print("-"*34)
            break

if __name__ == '__main__':
    main()
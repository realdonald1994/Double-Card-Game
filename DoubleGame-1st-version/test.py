import numpy as np
from card import Card
board = [['□' for _ in range(6)] for _ in range(7)]

print(Card().card5.left)
print('ddd')
#print(*board,sep='\n')
board[7-5][0]='A'
print(*board,sep='\n')


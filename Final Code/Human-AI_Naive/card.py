from type import Type
from infor import Infor
class Card:
    card1 = Type()
    card2 = Type()
    card3 = Type()
    card4 = Type()
    card5 = Type()
    card6 = Type()
    card7 = Type()
    card8 = Type()
    # card1.left = Infor()
    # card1.right = Infor()
    # card2.top = Infor()
    # card2.below = Infor()
    # card3.left = Infor()
    # card3.right = Infor()
    # card4.top = Infor()
    # card4.below = Infor()
    # card5.left = Infor()
    # card5.right = Infor()
    # card6.top = Infor()
    # card6.below = Infor()
    # card7.left = Infor()
    # card7.right = Infor()
    # card8.top = Infor()
    # card8.below = Infor()


    def __init__(self):
        # self.card1.left ='RX'
        # self.card1.right = 'WO'
        self.card1.left= ('RX','R','X',Card.card1)
        self.card1.right=('WO','W','O',Card.card1)
        # self.card2.top = 'RX'
        # self.card2.below = 'WO'
        self.card2.top = ('RX', 'R', 'X',Card.card2)
        self.card2.below = ('WO', 'W', 'O',Card.card2)
        # self.card3.left = 'WO'
        self.card3.left = ('WO', 'W', 'O',Card.card3)
        # self.card3.right = 'RX'
        self.card3.right = ('RX', 'R', 'X',Card.card3)
        # self.card4.top = 'WO'
        # self.card4.below = 'RX'
        self.card4.top = ('WO', 'W', 'O',Card.card4)
        self.card4.below = ('RX', 'R', 'X',Card.card4)
        # self.card5.left = "RO"
        # self.card5.right = 'WX'
        self.card5.left = ("RO",'R','O',Card.card5)
        self.card5.right = ('WX','W','X',Card.card5)
        # self.card6.top = 'RO'
        # self.card6.below = 'WX'
        self.card6.top = ("RO", 'R', 'O',Card.card6)
        self.card6.below = ('WX', 'W', 'X',Card.card6)
        # self.card7.left = 'WX'
        # self.card7.right  ='RO'
        self.card7.left = ('WX', 'W', 'X',Card.card7)
        self.card7.right = ("RO", 'R', 'O',Card.card7)
        # self.card8.top = 'WX'
        # self.card8.below = 'RO'
        self.card8.top = ('WX', 'W', 'X',Card.card8)
        self.card8.below = ("RO", 'R', 'O',Card.card8)
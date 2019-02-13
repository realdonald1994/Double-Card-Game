from type import Type
class Card:
    card1=Type()
    card2=Type()
    card3=Type()
    card4 = Type()
    card5 = Type()
    card6 = Type()
    card7 = Type()
    card8 = Type()

    def __init__(self):
        self.card5.left = "RO"
        self.card5.right = 'WX'
        self.card1.left ='RX'
        self.card1.right = 'WO'
        self.card2.top = 'RX'
        self.card2.below = 'WO'
        self.card3.left = 'WO'
        self.card3.right = 'RX'
        self.card4.top = 'WO'
        self.card4.below = 'RX'
        self.card6.top = 'RO'
        self.card6.below = 'WX'
        self.card7.left = 'WX'
        self.card7.right  ='RO'
        self.card8.top = 'WX'
        self.card8.below = 'RO'

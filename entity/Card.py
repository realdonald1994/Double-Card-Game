from .Segment import Segment
from .Player import Player

# Card class
class Card:
    # left segment
    left_seg = Segment()
    # right segment
    right_seg = Segment()
    # the player who placed the card
    player = Player()

    # constructor
    def __init__(self, left, right, player):
        self.left_seg = left
        self.right_seg = right
        self.player = player


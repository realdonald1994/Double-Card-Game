from entity.Segment import Segment
from entity.Player import Player

# Card class
class Card:
    # left/bottom segment
    left_seg = Segment()
    # right/up segment
    right_seg = Segment()
    # the player who placed the card
    player = Player()

    # constructor
    def __init__(self, left = Segment, right = Segment, player = 'human1'):
        self.left_seg = left
        self.right_seg = right
        self.player = player

    # create_card
    @staticmethod
    def get_card(rotation):
        if rotation == 1:
            return Card(Segment.get_red_with_solid_dot_segment(),
                Segment.get_white_with_hollow_dot_segment())
        elif rotation == 2:
            return Card(Segment.get_white_with_hollow_dot_segment(),
                Segment.get_red_with_solid_dot_segment())
        elif rotation == 3:
            return Card(Segment.get_white_with_hollow_dot_segment(),
                Segment.get_red_with_solid_dot_segment())
        elif rotation == 4:
            return Card(Segment.get_red_with_solid_dot_segment(),
                Segment.get_white_with_hollow_dot_segment())
        elif rotation == 5:
            return Card(Segment.get_red_with_hollow_dot_segment(),
                Segment.get_white_with_solid_dot_segment())
        elif rotation == 6:
            return Card(Segment.get_white_with_solid_dot_segment(),
                Segment.get_red_with_hollow_dot_segment())
        elif rotation == 7:
            return Card(Segment.get_white_with_solid_dot_segment(),
                Segment.get_red_with_hollow_dot_segment())
        elif rotation == 8:
            return Card(Segment.get_red_with_hollow_dot_segment(),
                Segment.get_white_with_solid_dot_segment())

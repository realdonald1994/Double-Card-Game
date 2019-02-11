# Segment class
# each card has 2 segments (a left and a right segment)
class Segment:
    # dots (solid / hollow)
    dots = ''
    # color (red / white)
    color = ''

    # constructor
    def __init__(self, dots = '', color = ''):
        self.dots = dots
        self.color = color

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

    # get_red_with_solid_dot_segment
    @staticmethod
    def get_red_with_solid_dot_segment():
        return Segment('solid', 'red')

    # get_white_with_solid_dot_segment
    @staticmethod
    def get_white_with_solid_dot_segment():
        return Segment('solid', 'white')

    # get_red_with_hollow_dot_segment
    @staticmethod
    def get_red_with_hollow_dot_segment():
        return Segment('hollow', 'red')

    # get_white_with_hollow_dot_segment
    @staticmethod
    def get_white_with_hollow_dot_segment():
        return Segment('hollow', 'white')

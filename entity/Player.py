# Player class
class Player:
    # player's name (human1 / human2 / ai1 / ai2)
    name = ''
    # player's type (human / ai)
    type = ''

    # constructor
    def __init__(self, name = 'human1', type = 'human'):
        self.name = name
        self.type = type


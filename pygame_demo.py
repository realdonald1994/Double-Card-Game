# link: https://realpython.com/pygame-a-primer/

import pygame
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(820, random.randint(0, 600)))

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# define player object and call super to give it all the properties and
# methods of pygame.sprite.Sprite
# the surface we fraw on the screen is now a property of 'Player'
# (5) sprites
# a sprite is a 2d representation of somethign on the screen
# essentially, a sprite is a picture
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # define the behavior of the sprite based off the keys that are pressed
    # K_UP, K_DOWN, K_LEFT, K_RIGHT correspond to the arrow keys
    # on the keyboard
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

# (1) create a screen to display on
pygame.init()
# pass a tuple with the width and height of the window we want
# size is 800x600
screen = pygame.display.set_mode((800, 600))

# initialize pygame
player = Player()


# (2) game loop
# variable to keep our main loop running
running = True

# our main loop
while running:
    # for loop through the event queue
    #
    # all user input go into the PyGame event queue, which can be accessed
    # by calling pygame.event.get()
    for event in pygame.event.get():
        # check for KEYDOWN event; KEYDOWN is a constant defined
        # in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # if the Esc key has been pressed set running to false to
            # exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False

    # (6) user input
    # make the player controllable
    # pygame.event.get_pressed() returns a dictionary with all the keydown
    # events in the queue
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # draw the player to the screen
    # (4) blit and flip
    # blit is just a technical way to say draw
    # here's how we draw our surf to the screen
    # this line says "Draw surf onto screen at coordinates x:400, y:300"
    # blit's two arguments:
    #      1st: the surface to draw
    #      2nd: the location to draw it at on the source surface
    # screen.blit(player.surf, player.rect)
    screen.blit(player.surf, (400, 300))
    # update the display
    # flip will update the entire screen with everything
    # that has been drawn since the last flip, without a call
    # to flip(), nothing will show
    pygame.display.flip()

    # (3) surfaces and rects
    # create the surface and pass in a tuple with its length and width
    # #surf = pygame.Surface((50, 50))
    # give the surface a color to differentiate it from the background
    # #surf.fill((255, 255, 255))
    # #rect = surf.get_rect()








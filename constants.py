# Adding pygame here just to have my groups as contants as well
import pygame

# File to hold game constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TUPLE = tuple([SCREEN_WIDTH, SCREEN_HEIGHT])

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8 # constant in seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

SOLID_BLACK_COLOR = (0, 0, 0)
SOLID_WHITE_COLOR = (255, 255, 255)

PLAYER_RADIUS = 20
PLAYER_LINE_WIDTH = 2
PLAYER_START_X = SCREEN_WIDTH / 2
PLAYER_START_Y = SCREEN_HEIGHT / 2
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200

# Creating the groups
UPDATABLE_GROUP = pygame.sprite.Group() # objects that can be updated
DRAWABLE_GROUP = pygame.sprite.Group() # objects that can be draw to the screen

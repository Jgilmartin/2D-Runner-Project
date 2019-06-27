# A 2D runner game with randomized platform height and spacing (within limitation)
# Intended to be played with a single button, but it might be played with a second button, one for jumping and one for fast falling


# To DO: 
#Create Color classes and scheme for game

import pygame

# Temporary Colors
WHITE_C = (255, 255, 255)
BLACK_C = (0, 0, 0)

# Setup Screen Size
SCREEN_TITLE = 'Bicc Peepee'
SCREEN_W = 800 
SCREEN_H = 600

# Creating game clock
clock = pygame.time.Clock()

class Game:
    TICK_RATE = 60
    gameOver = False
    SCORE = 0

    # Initializer for the game class, will include game window size and title

class GameObject:
    def __init__(self, image_path, x, y, width, height):
        # Declare image path
        object_image = pygame.image.load(image_path)
        # Scale image
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


class Platform(GameObject):
    def __init__(self, platHeight, platWidth, platSpeed):
        
        self.platHeight = platHeight
        self.platWidth = platWidth
        self.platSpeed = platSpeed
        
        # Creating game window
        self.game_screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

        # Set the game window/background

        self.game_screen.fill(WHITE_C) 

        # Main game clock
        while gameOver == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True


# Class to represent the player character

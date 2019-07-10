# A 2D runner game with randomized platform height and spacing (within limitation)
# Intended to be played with a single button, but it might be played with a second button, one for jumping and one for fast falling


# To DO: 
#Create Color classes and scheme for game

import pygame
pygame.init()
# Temporary Colors
WHITE_C = (255, 255, 255)
BLACK_C = (0, 0, 0)

# Setup Screen Size
SCREEN_TITLE = 'Runner'
SCREEN_W = 1200
SCREEN_H = 800

# Creating game clock
clock = pygame.time.Clock()

class Game():
    TICK_RATE = 60
    gameOver = False
    SCORE = 0

    # Initializer for the game class, will include game window size and title
    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Creating the game screen
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_C)

        pygame.display.set_caption(title)

        background = pygame.image.load(image_path)
        self.finalBackground = pygame.transform.scale(background, (width, height))
    
    def runGameLoop(self):
        # input_y handles character movement
        gameOver = False
        input_y = 0

        platform1 = Platform(400, 200, 1, 550, 200)

        while gameOver != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction_y = 1
                    elif event.key == pygame.K_DOWN:
                        direction_y = -1
                print(event)
            platform1.draw(self.game_screen)

            # Graphics Rendering (inside for event loop)
        self.game_screen.fill(WHITE_C)
        self.game_screen.blit(self.finalBackground, (0,0))
        pygame.display.update()
        clock.tick(self.TICK_RATE)

        
        
        
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

    def draw(self, image):
        self.background.blit(self.image, (self.x_pos, self.y_pos))

# pygame.draw.rect(screen, Color, (x, y, x_size, y_size))
class Platform(GameObject):
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
class Player(GameObject):
    def __init__(self, otherObject):
        super().__init__(otherObject)

new_game = Game('forest_background.png', SCREEN_TITLE, SCREEN_W, SCREEN_H)
new_game.runGameLoop()

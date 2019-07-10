# A 2D runner game with randomized platform height and spacing (within limitation)
# Intended to be played with a single button, but it might be played with a second button, one for jumping and one for fast falling


# To DO: 
#Create Color classes and scheme for game

import pygame

pygame.init()
# Temporary Colors

# Creating game clock

WHITE_C = (255, 255, 255)
BLACK_C = (0, 0, 0)
SCREEN_TITLE = 'Runner'
SCREEN_W = 800
SCREEN_H = 800
TICK_RATE = 60

# pygame.draw.rect(screen, Color, (x, y, x_size, y_size))

class Game():
    # Setup Screen Size


    def __init__(self, backgroundImage, height, width, title):
        self.backgroundImage = backgroundImage
        self.height = height
        self.width = width
        self.title = title
        
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_C)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        x_pos = 200
        y_pos = 200
        gameOver = False
        direction_y = 0
        
        clock = pygame.time.Clock()
        while gameOver != True:
            platform1 = Platform(x_pos, y_pos, 200, 200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction_y = 1
                    elif event.key == pygame.K_DOWN:
                        direction_y = -1
                elif event.type == pygame.KEYUP:
                    direction_y = 0
            if direction_y == -1:
                x_pos += 20
            if direction_y == 1:
                x_pos -= 20

                print(event)
            # pygame.draw.rect(self.game_screen, BLACK_C, (y_pos, x_pos, x_size, y_size))
            
            self.game_screen.fill(WHITE_C)
            platform1.draw(self.game_screen)
            
            pygame.display.update()
            clock.tick(TICK_RATE)

class GameObject: 
    def __init__(self, image_path, x, y, width, height):
        self.x_pos = x
        self.y_pos = y

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))

class Platform():
    def __init__(self, y_pos, x_pos, width, height):
        self.image = pygame.image.load('cobblestone.jpg')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.width = width
        self.height = height
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

    def move(self):
        yee = 0

class Player():
    SPEED = 10
    def __init__(self, y_pos, x_pos, width, height):
        self.image = pygame.image.load()
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.width = width
        self.height = height
        

new_game = Game('forest_background.png', SCREEN_H, SCREEN_W, SCREEN_TITLE)
new_game.run_game_loop()

# player_image = pygame.image.load('path')
# player_image = pygame.transform.scale(player_image, (50, 50))
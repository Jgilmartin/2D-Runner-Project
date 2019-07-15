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

    # Creating a game that takes in a few parameters for the game window
    # 
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
        y_pos = 600
        playerPos_x = 225
        playerPos_y = 400
        playerVelocity = 0
        gameOver = False
        
        clock = pygame.time.Clock()
        # Current problem is that sprite flies off the screen very quickly
        # Need to implement collision in order to prevent the sprite from flying off the screen and possibly find a more efficient posititon physics function
        while gameOver != True:
            platform1 = Platform(y_pos, x_pos, 200, 200)
            platform2 = Platform(700, 500, 200, 100)
            player1 = Player(playerPos_y, playerPos_x, 50, 50)

            if playerVelocity <= 20:
                playerVelocity += (playerVelocity + 0.02)
            playerPos_y += playerVelocity
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                elif event.type == pygame.K_DOWN:
                    if event.type == pygame.K_UP:
                        playerVelocity = -40
                print(event)
            # pygame.draw.rect(self.game_screen, BLACK_C, (y_pos, x_pos, x_size, y_size))
            
            self.game_screen.fill(WHITE_C)
            player1.draw(self.game_screen)
            platform1.draw(self.game_screen)
            platform2.draw(self.game_screen)
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

        self.image = pygame.image.load('Runner_stickman.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

    def collisionDetection(self, platform):
        if self.y_pos + self.height >= platform.y_pos:
            return True



    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

new_game = Game('forest_background.png', SCREEN_H, SCREEN_W, SCREEN_TITLE)
new_game.run_game_loop()

# player_image = pygame.image.load('path')
# player_image = pygame.transform.scale(player_image, (50, 50))
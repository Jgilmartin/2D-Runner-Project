# A 2D runner game with randomized platform height and spacing (within limitation)
# Intended to be played with a single button, but it might be played with a second button, one for jumping and one for fast falling
# To DO: 

from pygame.locals import *
import pygame, random
pygame.init()
# Temporary Colors
# Creating game clock
WHITE_C = (255, 255, 255)
BLACK_C = (0, 0, 0)
SCREEN_TITLE = 'Runner'
SCREEN_W = 800
SCREEN_H = 800
TICK_RATE = 120
TICK_RATE = 60
info_font = pygame.font.SysFont("Verdana", 20)

pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
# pygame.draw.rect(screen, Color, (x, y, x_size, y_size))
class Game():
    # Setup Screen Size
    # Creating a game that takes in a few parameters for the game window
    
    fps = 0
    fps_overlay = info_font.render(str(fps), True, BLACK_C)
    def __init__(self, backgroundImage, height, width, title):
        self.backgroundImage = pygame.image.load('forest_background.png')
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (SCREEN_W, SCREEN_H))
        self.height = height
        self.height = height    
        self.width = width
        self.title = title

        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_C)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        playerPos_x = 225
        playerPos_y = 200
        playerVelocity = 0
        gameOver = False
        clock = pygame.time.Clock()
        activePlatform = Platform(500, 500, 250, 300)

        player1 = Player(playerPos_y, playerPos_x, 50, 50)

        # Game loop
        while gameOver != True:
            # Check if the platform is off screen and if so, spawn a new platform
            if activePlatform.x_pos+activePlatform.width < -20:
                #activePlatform = Platform(300, 805, activePlatform.width, 200)

                # Platform with randomly generated height and width 
                activePlatform = Platform(random.randrange(400, 600), 805, random.randrange(200, 400), 400)
            # Move platform x_pos by -20 every frame
            activePlatform.x_pos += -20
            
            # Player respawn when off screen and when colliding with side of platform
            if player1.y_pos > 800:
                player1.y_pos =0
            if playerVelocity < 20 and player1.collisionDetection(activePlatform, playerVelocity) == False:
                playerVelocity += 1
            if playerVelocity > 20:
                playerVelocity = 20

            # Function sets the player height to the platform height and removes velocity upon collision
            elif player1.collisionDetection(activePlatform, playerVelocity) == True:
                playerVelocity = 0
                player1.y_pos = activePlatform.y_pos
                player1.y_pos = activePlatform.y_pos-player1.height

            playerPos_y += playerVelocity

            player1.y_pos += playerVelocity # move the players position every frame


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and player1.collisionDetection(activePlatform, playerVelocity) == True:
                        playerVelocity = -30
                    if event.key == pygame.K_DOWN and playerVelocity >=0 :
                        playerVelocity = 
                


            print(event)
            self.game_screen.fill(WHITE_C)
            # self.game_screen.blit(self.backgroundImage, (0,0))
            player1.draw(self.game_screen)
            activePlatform.draw(self.game_screen)
            pygame.display.update()
            clock.tick(TICK_RATE)

class GameObject: 
    def __init__(self, image_path, x, y, width, height):
        self.x_pos = x
        self.y_pos = y
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        
class Platform():
    def __init__(self, y_pos, x_pos, width, height):
        self.image = pygame.image.load('cobblestone.jpg').convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.width = width
        self.height = height
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))
    def move(self):
        yee = 0
        
def spawnPlatform(activePlatform):
    activePlatform = Platform(500, activePlatform.x_pos, activePlatform.width, activePlatform.height)

class Player():
    SPEED = 10
    def __init__(self, y_pos, x_pos, width, height):
        self.image = pygame.image.load('Runner_stickman.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
    # Mostly final collision detection, player no longer gets locked into the platform, quicksand platforms fixed player can jump out of platform.
    # Can recreate quicksand platforms by chaning the if statemnt to > 0 instead of >= 0
    def collisionDetection(self, platform, playerVelocity): 
        self.platform = platform
        if self.y_pos + self.height >= platform.y_pos and playerVelocity >= 0 and self.x_pos+self.width >= platform.x_pos and self.x_pos <= platform.x_pos+platform.width:
            return True
        else:
            return False
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))
new_game = Game('forest_background.png', SCREEN_H, SCREEN_W, SCREEN_TITLE)
new_game.run_game_loop()
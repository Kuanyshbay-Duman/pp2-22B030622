import time
import random
from random import randrange
import sys
import pygame
from pygame.locals import *


# Initialzing
pygame.init()

# Setting up fps
fps = 60
FramePerSec = pygame.time.Clock()

# Creating colors
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Other Variables for use in the program
width = 400
height = 600
speed = 5
score = 0
collect = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

# background image
background = pygame.image.load("Week10/TSIS8/TOOLS/AnimatedStreet.png")

# Create a white screen
screen = pygame.display.set_mode((400, 600))
screen.fill(white)
pygame.display.set_caption("Game")

# object of enemy


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # enemy image
        self.image = pygame.image.load("Week10/TSIS8/TOOLS/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)
# enemy mowing

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        # if the enemy go away from the area score is increasing and new enemy appears
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)

# object of coin


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("Week10/TSIS8/TOOLS/coin.png"), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40),
                            random.randint(0, height))

# object of player


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Week10/TSIS8/TOOLS/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
# moving of player

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coins()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coinss = pygame.sprite.Group()
coinss.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Game Loop
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))

    # showing text of score
    scores = font_small.render(str(score), True, black)
    screen.blit(scores, (10, 10))

    # showing text of collected coin
    col = font_small.render('Money '+str(collect), True, black)
    screen.blit(col, (width - col.get_width()-10, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        weight = randrange(1, 6)
        if entity != C1:
            entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('Week10/TSIS8/TOOLS/crash.wav').play()
        time.sleep(0.5)
        # showing game over text
        screen.fill(red)
        screen.blit(game_over, (30, 250))

        pygame.display.update()
        # removes all objects
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        # exit from application
        pygame.quit()
        sys.exit()
        # To be run if collision occurs between Player and coin
    if pygame.sprite.spritecollideany(P1, coinss):
        collect += weight
        if collect > 10:
            speed = speed + 10

        for i in coinss:
            i.rect.center = (random.randint(40, width - 40),
                             random.randint(40, height))

    pygame.display.update()
    FramePerSec.tick(fps)

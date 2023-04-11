import pygame
import time
import random
from random import randrange

pygame.init()
# colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
yellow = pygame.Color(238, 242, 0)
blue = pygame.Color(0, 242, 255)

# size of window
width, height = 800, 800
size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Amazing')

# position of head, food, and body
snake_pos = [randrange(0, 40)*20, randrange(0, 40)*20]
food_pos = [randrange(0, 40)*20, randrange(0, 40)*20]
snake_body = [[snake_pos[0], snake_pos[1]]]

direction = ''
change_to = direction

clr_for_food = random.choice([yellow, blue])

background = pygame.image.load('Week13\TSIS9\TOOLS\BAS.jpg')
score = 0
level = 0
collision = False
fps = 5

start_time = pygame.time.get_ticks()
time_limit = 5500  # in milliseconds


def show_score(choice, color, font, size):
    # showing score text
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    screen.blit(score_surface, (5, 10))

# showing score level


def show_level(choice, color, font, size):

    level_font = pygame.font.SysFont(font, size)
    level_surface = level_font.render('Level : ' + str(level), True, color)
    screen.blit(level_surface, (width - level_surface.get_width()-5, 10))


def show_time(choice, color, font, size):

    time_font = pygame.font.SysFont(font, size)
    time_surface = time_font.render(
        'Time left : ' + str(int(time_left/1000)), True, color)
    screen.blit(time_surface, (width - time_surface.get_width()-5, 30))


def game_over():
    over_font = pygame.font.SysFont('abadi', 80)
    over_surface = over_font.render(
        'GAME OVER. SCORE: ' + str(score), True, blue)
    over_rect = over_surface.get_rect()
    over_rect.midtop = (width/2, height/2)
    screen.blit(over_surface, over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    exit()


while True:
    # screen.blit(background, (0, 0))
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            # finds direction
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'up'
            if event.key == pygame.K_DOWN:
                change_to = 'down'
            if event.key == pygame.K_LEFT:
                change_to = 'left'
            if event.key == pygame.K_RIGHT:
                change_to = 'right'
        # checking if snake is going in opposite direction
    if change_to == 'up' and direction != 'down':
        direction = 'up'
    elif change_to == 'down' and direction != 'up':
        direction = 'down'
    elif change_to == 'left' and direction != 'right':
        direction = 'left'
    elif change_to == 'right' and direction != 'left':
        direction = 'right'
 # moving of snake
    if direction == 'up':
        snake_pos[1] += -size
    elif direction == 'down':
        snake_pos[1] += size
    elif direction == 'left':
        snake_pos[0] += -size
    elif direction == 'right':
        snake_pos[0] += size
        # growing of snake
    snake_body.insert(0, list(snake_pos))
    # eating the food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        if clr_for_food == yellow:
            score += 5
        else:
            score += 10
        clr_for_food = random.choice([yellow, blue])
        if score % 30 == 0:
            # grow of level, score, speed
            level = int(score / 30)
            fps += 4
        collision = True
        start_time = pygame.time.get_ticks()
    else:
        snake_body.pop()
# if it eats new food appears
    if collision:
        food_pos = [randrange(0, 40)*20, randrange(0, 40)*20]
        collision = False
# drawing parts of snake by coordinates
    for x in snake_body:
        pygame.draw.rect(screen, red, pygame.Rect(x[0], x[1], size, size))
    # drawing food by coordinates
    pygame.draw.rect(screen, clr_for_food, pygame.Rect(
        food_pos[0], food_pos[1], size, size))
# game over if it touches the border
    if snake_pos[0] < 0 or snake_pos[0] > width:
        game_over()
    elif snake_pos[1] < 0 or snake_pos[1] > height:
        game_over()

# game over if it eats hisself
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
   # setting timer for the food
    current_time = pygame.time.get_ticks()
    time_left = time_limit - (current_time - start_time)
    if time_left <= 0:
        clr_for_food = random.choice([yellow, blue])
        food_pos = [randrange(0, 40)*20, randrange(0, 40)*20]
        collision = False
        start_time = pygame.time.get_ticks()

    show_score(1, white, 'monaco', 30)
    show_level(1, white, 'monaco', 30)
    show_time(1, white, 'monaco', 30)

    pygame.display.update()
    pygame.time.Clock().tick(fps)

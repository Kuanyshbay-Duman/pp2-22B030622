import pygame

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Food Timer')

# Set up the clock
clock = pygame.time.Clock()

# Define the food image and its initial position
food_image = pygame.image.load('Week13/TSIS9/TOOLS/Enemy.png')
food_x = (display_width - food_image.get_width()) / 2
food_y = (display_height - food_image.get_height()) / 2

# Define the timer variables
start_time = pygame.time.get_ticks()
time_limit = 5000 # in milliseconds

# Main game loop
game_exit = False
while not game_exit:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

    # Calculate the time left
    current_time = pygame.time.get_ticks()
    time_left = time_limit - (current_time - start_time)

    # Update the screen
    game_display.fill((255, 255, 255)) # fill with white color
    game_display.blit(food_image, (food_x, food_y)) # draw the food image
    if time_left > 0:
        # Display the time left
        font = pygame.font.Font(None, 36)
        text = font.render('Time left: ' + str(time_left // 1000) + ' seconds', True, (0, 0, 0))
        text_rect = text.get_rect(center=(display_width // 2, display_height // 2 - 50))
        game_display.blit(text, text_rect)
    else:
        # Display the message when time is up
        font = pygame.font.Font(None, 48)
        text = font.render('Time is up!', True, (255, 0, 0))
        text_rect = text.get_rect(center=(display_width // 2, display_height // 2 - 50))
        game_display.blit(text, text_rect)

    pygame.display.update()

    # Limit the frame rate to 60 fps
    clock.tick(60)

# Quit Pygame
pygame.quit()
quit()
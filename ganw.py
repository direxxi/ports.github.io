import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set up the colors
background_color = (255, 255, 255)
snake_color = (0, 255, 0)
food_color = (255, 0, 0)

# Set up the snake
snake_block_size = 10
snake_speed = 15
snake_list = []
snake_length = 1
x1 = screen_width / 2
y1 = screen_height / 2

# Set up the food
food_block_size = 10
food_x = round(random.randrange(0, screen_width - food_block_size) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - food_block_size) / 10.0) * 10.0

# Set up the font
font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    msg = font_style.render(msg, True, color)
    screen.blit(msg, [screen_width / 6, screen_height / 3])

# Game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the snake
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x1 -= snake_block_size
    elif keys[pygame.K_RIGHT]:
        x1 += snake_block_size
    elif keys[pygame.K_UP]:
        y1 -= snake_block_size
    elif keys[pygame.K_DOWN]:
        y1 += snake_block_size

    # Draw the snake and the food
    screen.fill(background_color)
    pygame.draw.rect(screen, food_color, [food_x, food_y, food_block_size, food_block_size])

    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    for segment in snake_list:
        pygame.draw.rect(screen, snake_color, [segment[0], segment[1], snake_block_size, snake_block_size])

    pygame.display.update()

    # Check if the snake has collided with the food
    if x1 == food_x and y1 == food_y:
        food_x = round(random.randrange(0, screen_width - food_block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - food_block_size) / 10.0) * 10.0
        snake_length += 1

    # Set the clock speed
    clock.tick(snake_speed)

# Quit Pygame
pygame.quit()
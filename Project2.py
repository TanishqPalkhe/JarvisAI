import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
grey = (0, 255, 0)
# Creating window
screen_width = 500
screen_height = 600
score_width = 100
score_height = 50
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()

# Game specific variables

font = pygame.font.SysFont(None, 40)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    fps = 30
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    velocity_x = 0
    velocity_y = 0
    score = 0


snk_list = []
snake_length = 1

clock = pygame.time.Clock()
# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 15
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -15
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = -15
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y = 15
                velocity_x = 0
        snake_x += velocity_x
        snake_y += velocity_y
        if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
            score += 1

            food_x = random.randint(0, screen_width // 2)
            food_y = random.randint(0, screen_height // 2)
            snake_length += 4

    gameWindow.fill(white)
    text_screen("Score:" + str(score * 10), red, 5, 5)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)
    if len(snk_list) > snake_length:
        del snk_list[0]

    # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    plot_snake(gameWindow, black, snk_list, snake_size)
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()

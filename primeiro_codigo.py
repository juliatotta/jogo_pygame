import sys, pygame
from time import sleep
import random

pygame.init()

size = width, height = 600, 600
speed = [1, 1]
white = 255, 255, 255
BLUE = (0, 200, 255)
BLACK = (0, 0, 0)

SNAKE_X = width / 2
SNAKE_Y = height / 2

screen = pygame.display.set_mode(size)

def make_food(screen):
    x = random.randint(10, 570)
    y = random.randint(10, 570)
    return pygame.draw.rect(screen, BLACK, [x, y, 10, 10])

make_food(screen)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(white)
    snake = pygame.draw.rect(screen, BLUE, [SNAKE_X, SNAKE_Y, 10, 10])

    SNAKE_X += 2
    sleep(0.1)

    print(snake)

    pygame.display.flip()

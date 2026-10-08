import pygame
from sys import exit
import random

ROWS = 25
COLUMNS = ROWS
TILE_SIZE = 25
GAME_WIDTH = TILE_SIZE * COLUMNS
GAME_HEIGHT = TILE_SIZE * ROWS
ACHTERGROND = "darkolivegreen2"
snake_velocity = (0, 0) #velocity x and y

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

def get_random(limit):
    return random.randint(0, limit-1) * TILE_SIZE

food = pygame.Rect(get_random(COLUMNS), get_random(ROWS), TILE_SIZE, TILE_SIZE)

snake = []
snake.append(pygame.Rect(get_random(COLUMNS), get_random(ROWS), TILE_SIZE, TILE_SIZE)) #head

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                snake_velocity = (0, -TILE_SIZE)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                snake_velocity = (0, TILE_SIZE)
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                snake_velocity = (-TILE_SIZE, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                snake_velocity = (TILE_SIZE, 0)

    #move
    snake[0].move_ip(snake_velocity)



    window.fill(ACHTERGROND)

    pygame.draw.rect(window, "red", food)
    for snake_part in snake:
        pygame.draw.rect(window, "darkolivegreen4", snake_part)
    pygame.display.update()
    clock.tick(10)
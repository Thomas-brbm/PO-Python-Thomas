import pygame
from sys import exit
import random

ROWS = 25
COLUMNS = ROWS
TILE_SIZE = 25
GAME_WIDTH = TILE_SIZE * COLUMNS
GAME_HEIGHT = TILE_SIZE * ROWS
ACHTERGROND = "darkolivegreen2"

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

def get_random(limit):
    return random.randint(0, limit-1) * TILE_SIZE

food = pygame.Rect(get_random(COLUMNS), get_random(ROWS), TILE_SIZE, TILE_SIZE)



#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill(ACHTERGROND)

    pygame.draw.rect(window, "red", food)
    pygame.display.update()
    clock.tick(10)
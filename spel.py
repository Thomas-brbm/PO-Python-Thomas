import pygame
from sys import exit

TILE_SIZE = 25
GAME_WIDTH = 500
GAME_HEIGHT = 500

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

food = pygame.Rect(100, 150, TILE_SIZE, TILE_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(window, "cyan", food)
    pygame.display.update()
    clock.tick(10)
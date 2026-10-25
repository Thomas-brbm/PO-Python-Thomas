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
pygame.mixer.init()
pygame.font.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font("fonts/pixelfont.ttf", 48)

def get_random(limit):
    return random.randint(0, limit-1) * TILE_SIZE

def spawn_food(snake_list):
    while True:
        food = pygame.Rect(get_random(COLUMNS), get_random(ROWS), TILE_SIZE, TILE_SIZE)

        overlap = False
        for part in snake_list:
            if part.center == food.center:
                overlap = True
                break

        if not overlap:
            return food

pygame.mixer.music.load("sounds/snake_music.ogg")
eating_sound = pygame.mixer.Sound("sounds/eating_sound.wav")

pygame.mixer.music.play(-1)

pygame.mixer.music.set_volume(0.3)

snake = []
snake.append(pygame.Rect(get_random(COLUMNS), get_random(ROWS), TILE_SIZE, TILE_SIZE)) #head

food = spawn_food(snake)
#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                if snake_velocity != (0, TILE_SIZE):
                    snake_velocity = (0, -TILE_SIZE)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                if snake_velocity != (0, -TILE_SIZE):
                    snake_velocity = (0, TILE_SIZE)
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                if snake_velocity != (TILE_SIZE, 0):
                    snake_velocity = (-TILE_SIZE, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                if snake_velocity != (-TILE_SIZE, 0):
                    snake_velocity = (TILE_SIZE, 0)

    for i in range (len(snake)-1, 0, -1):
        snake[i] = snake[i-1].copy()
    snake[0].move_ip(snake_velocity)

    if not window.get_rect().contains(snake[0]):
        snake.clear()
        snake.append(pygame.Rect(get_random(COLUMNS), get_random(ROWS), TILE_SIZE, TILE_SIZE))
        food = spawn_food(snake)
        snake_velocity = (0, 0)
        pygame.mixer.music.play(-1)
        score = 0

    if snake[0].center == food.center:
        pygame.mixer.Sound.play(eating_sound)
        snake.append(food)
        food = spawn_food(snake)
        score += 1

    if any([snake[0].center == snake[i].center for i in range(1, len(snake) - 1)]):
        snake.clear()
        snake.append(pygame.Rect(get_random(COLUMNS), get_random(ROWS), TILE_SIZE, TILE_SIZE))
        food = spawn_food(snake)
        snake_velocity = (0, 0)
        pygame.mixer.music.play(-1)
        score = 0


    window.fill(ACHTERGROND)

    pygame.draw.rect(window, "red", food)
    for snake_part in snake:
        pygame.draw.rect(window, "darkolivegreen4", snake_part)

        if snake_velocity == (0, 0):
            pygame.draw.rect(window, "white", (snake[0].x + 0, snake[0].y + 4, 10, 6))
            pygame.draw.rect(window, "white", (snake[0].x + 15, snake[0].y + 4, 10, 6))
                        
            pygame.draw.rect(window, "black", (snake[0].x + 5, snake[0].y + 4, 5, 6))
            pygame.draw.rect(window, "black", (snake[0].x + 20, snake[0].y + 4, 5, 6))
                        
            pygame.draw.rect(window, "black", (snake[0].x + 7, snake[0].y + 19, 3, 3))
            pygame.draw.rect(window, "black", (snake[0].x + 16, snake[0].y + 19, 3, 3))           

        elif snake_velocity == (0, TILE_SIZE):
            pygame.draw.rect(window, "white", (snake[0].x + 0, snake[0].y + 4, 10, 6))
            pygame.draw.rect(window, "white", (snake[0].x + 15, snake[0].y + 4, 10, 6))
            
            pygame.draw.rect(window, "black", (snake[0].x + 5, snake[0].y + 4, 5, 6))
            pygame.draw.rect(window, "black", (snake[0].x + 20, snake[0].y + 4, 5, 6))
            
            pygame.draw.rect(window, "black", (snake[0].x + 7, snake[0].y + 19, 3, 3))
            pygame.draw.rect(window, "black", (snake[0].x + 16, snake[0].y + 19, 3, 3))

        elif snake_velocity == (0, -TILE_SIZE):
            pygame.draw.rect(window, "white", (snake[0].x + 0, snake[0].y + 17, 10, 6))
            pygame.draw.rect(window, "white", (snake[0].x + 15, snake[0].y + 17, 10, 6))
            
            pygame.draw.rect(window, "black", (snake[0].x + 0, snake[0].y + 17, 5, 6))
            pygame.draw.rect(window, "black", (snake[0].x + 15, snake[0].y + 17, 5, 6))
            
            pygame.draw.rect(window, "black", (snake[0].x + 7, snake[0].y + 3, 3, 3))
            pygame.draw.rect(window, "black", (snake[0].x + 16, snake[0].y + 3, 3, 3))

        elif snake_velocity == (TILE_SIZE, 0):
            pygame.draw.rect(window, "white", (snake[0].x + 4, snake[0].y + 0, 6, 10))
            pygame.draw.rect(window, "white", (snake[0].x + 4, snake[0].y + 15, 6, 10))
                        
            pygame.draw.rect(window, "black", (snake[0].x + 4, snake[0].y + 0, 6, 5))
            pygame.draw.rect(window, "black", (snake[0].x + 4, snake[0].y + 15, 6, 5))
                        
            pygame.draw.rect(window, "black", (snake[0].x + 19, snake[0].y + 7, 3, 3))
            pygame.draw.rect(window, "black", (snake[0].x + 19, snake[0].y + 16, 3, 3))

        elif snake_velocity == (-TILE_SIZE, 0):
            pygame.draw.rect(window, "white", (snake[0].x + 17, snake[0].y + 0, 6, 10))
            pygame.draw.rect(window, "white", (snake[0].x + 17, snake[0].y + 15, 6, 10))
                                    
            pygame.draw.rect(window, "black", (snake[0].x + 17, snake[0].y + 5, 6, 5))
            pygame.draw.rect(window, "black", (snake[0].x + 17, snake[0].y + 20, 6, 5))
                                    
            pygame.draw.rect(window, "black", (snake[0].x + 3, snake[0].y + 7, 3, 3))
            pygame.draw.rect(window, "black", (snake[0].x + 3, snake[0].y + 16, 3, 3))  

    score_text = font.render(f"Score: {score}", False, "black")
    window.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(10)
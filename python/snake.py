import pygame, random
from pygame.locals import *

display_width = 600
display_height = 600

pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

is_paused = False

def transport_to_opposite_direction(pos):
    if pos[0] < 0:
        return (display_height, pos[1]);
    if pos[0] > display_height:
        return (0, pos[1]);
    if pos[1] < 0:
        return (pos[0], display_width);
    if pos[1] > display_width:
       return (pos[0], 0);

    return pos

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])

def paused():
    global is_paused
    while is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                is_paused = False
                
        pygame.display.update()
        clock.tick(15)  

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255,0,0))

my_direction = LEFT

clock = pygame.time.Clock();

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_SPACE:
                is_paused = True
                paused()
    
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0],snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0],snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10 ,snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10,snake[0][1])

    snake[0] = transport_to_opposite_direction(snake[0])

    for i in range(1, len(snake)):
        if collision(snake[0], snake[i]):
            pygame.quit()

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()

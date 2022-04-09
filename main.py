import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 600, 400
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

is_play = True

while is_play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_play = False

    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    rgb_collor = (red, green, blue)
    coordinate_x = randint(0, WIDTH)
    coordinate_y = randint(0, HEIGHT)
    coordinates = (coordinate_x, coordinate_y)
    rect_sizes = (10, 10)

    pygame.draw.rect(window, rgb_collor, (*coordinates, *rect_sizes))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

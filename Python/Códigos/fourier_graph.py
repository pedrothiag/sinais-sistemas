"""
subscribe to my youtube channel
https://www.youtube.com/channel/UCjPk9YDheKst1FlAf_KSpyA
"""
import pygame
from pygame import gfxdraw
import random
import time
import os
import math
os.environ["SDL_VIDEO_CENTERED"]='1'

#pygame configurations
width,height = 1280, 720
fps= 60
pygame.display.set_caption("Fourier series")
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#colors
white = (230, 230, 230)
black = (28, 28, 28)
gray = (100, 100, 100)
green = (54, 255, 141)
gray2 = (80, 80,100)
red = (240, 30,40)


N = 1
time= 0
radius = 0
pos_x = 300
pos_y = 320
wave_list = []
offset = 300

ITERATIONS = 10

run=True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    x = pos_x
    y = pos_y
    for i in range(ITERATIONS):
        old_x = x
        old_y = y

        N = i * 2 + 1
        radius = 100 * (4/ (N * math.pi))
        x += int( radius * math.cos(2 * N * time))
        y +=  int( radius * math.sin(2 * N * time))

        pygame.gfxdraw.circle(screen, old_x, old_y, int(radius) , white)
        pygame.draw.line(screen, gray, (old_x, old_y), (x,y) , 3)
        pygame.draw.circle(screen, green, (x,y), 5)

    wave_list.insert(0, y)
    if len(wave_list) > 700:
        wave_list.pop()

    pygame.draw.line(screen, red, (x,y), (pos_x+offset, wave_list[0]), 3)

    for index in range(1,len(wave_list)):
        pygame.gfxdraw.line(screen, index + pos_x + offset, wave_list[index], index + pos_x + offset, wave_list[index - 1], green)
        # pygame.draw.line(screen, green, (index + pos_x + offset, wave_list[index]), (index + pos_x + offset - 1, wave_list[index - 1]), 2);
        # pygame.draw.circle(screen, green, (index + pos_x + offset, wave_list[index]), 5)
    time += 0.01

    pygame.display.update()

pygame.quit()
# https://www.youtube.com/watch?v=GKe1aGQlKDY&list=PLryDJVmh-ww1OZnkZkzlaewDrhHy2Rli2
import pygame
import sys
from game_window_class import *


WIDTH, HEIGHT = 800, 800
BACKGROUND = (199, 199, 199)
FPS = 60


def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


def update():
    game_window.update()


def draw():
    game_window.draw()
    window.fill(BACKGROUND)


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_window = Game_window(window, 10, 10)

running = True
while running:
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()


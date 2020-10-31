# https://www.youtube.com/watch?v=GKe1aGQlKDY&list=PLryDJVmh-ww1OZnkZkzlaewDrhHy2Rli2
import pygame
import sys


WIDTH, HEIGHT = 800, 800
BACKGROUND = (42, 21, 13)
FPS = 60


def get_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


def update():
    pass


def draw():
    window.fill(BACKGROUND)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()


import pygame
from settings import * 
from grid_class import *


class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.grid = Grid(self)

    def run(self):
        while self.running:
            self.get_events()
            self.update()
            self.draw()
        pygame.quit()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BG_COLOUR)
        self.grid.draw()
        pygame.display.update()
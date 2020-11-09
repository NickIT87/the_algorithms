from settings import *
from cell_class import *
import pygame


class Grid:
    def __init__(self, game):
        self.game = game
        self.pos = (0,0)
        self.cells = []
        self.make_grid()

    def make_grid(self):
        for y in range(3):
            for x in range(3):
                self.cells.append(Cell(x, y, self))
        print(self.cells)

    def update(self):
        pass
    
    def draw(self):
        pass
        #pygame.draw.rect(self.game.screen, GRID_COLOUR, (self.pos[0], self.pos[1],
        #                                                 3*CELL_SIZE, 3*CELL_SIZE), 2)
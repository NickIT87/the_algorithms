import pygame


class Cell:
    def __init__(self, surface, grid_x, grid_y):
        self.alive = False
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.grid_x*20, self.grid_y*20)

    def draw(self):
        if self.alive:
            self.image.fill((0, 0, 0))
        else:
            self.image.fill((0, 0, 0))
            pygame.draw.rect(self.image, (255, 255, 255), (2,2,18,18))
        self.surface.blit(self.image, (self.grid_x*20, self.grid_y*20))
import pygame
vec = pygame.math.Vector2


class Game_window:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = vec(x, y)
        self.width, self.height = 600, 600
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.topleft = self.pos

    def draw(self):
        self.image.fill((102, 102, 102))
        self.screen.blit(self.image, (self.pos.x, self.pos.y))
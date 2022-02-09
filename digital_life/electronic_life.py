# https://www.youtube.com/watch?v=GKe1aGQlKDY&list=PLryDJVmh-ww1OZnkZkzlaewDrhHy2Rli2
import pygame
import sys
from game_window_class import *
from button_class import *


WIDTH, HEIGHT = 800, 800
BACKGROUND = (199, 199, 199)
FPS = 60


def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)



def update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)


def draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()
    

def mouse_on_grid(pos):
    if pos[0] > 100 and pos[0] < WIDTH-100:
        if pos[1] > 180 and pos[1] < HEIGHT-20:
            return True
    return False


def click_cell(pos):
    grid_pos = [pos[0]-100, pos[1]-180]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True


def make_buttons():
    buttons = []
    buttons.append(Button(window, WIDTH//2-50, 50, 100, 30, text='RUN', 
        colour=(28, 111, 51), hover_colour=(48, 131, 81), bold_text=True))
    return buttons


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_window = Game_window(window, 100, 180)
buttons = make_buttons()

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
#sys.exit()


# https://www.youtube.com/watch?v=GKe1aGQlKDY&list=PLryDJVmh-ww1OZnkZkzlaewDrhHy2Rli2
import pygame
import sys
from game_window_class import *
from button_class import *


WIDTH, HEIGHT = 800, 800
BACKGROUND = (199, 199, 199)
FPS = 60

# -------------- SETTING FUNCTIONS ------------------
def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()


def update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)


def draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()
    
# -------------- RUNNING FUNCTIONS ------------------
def running_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()


def running_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)


def running_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()


# -------------- PAUSE FUNCTIONS ------------------
def paused_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()


def paused_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)


def paused_draw():
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
    buttons.append(Button(window, WIDTH//5-50, 50, 110, 30, text='RUN', 
                        colour=(28, 111, 51), hover_colour=(48, 131, 81), 
                        bold_text=True, function=run_game))
    buttons.append(Button(window, WIDTH//2-50, 50, 110, 30, text='PAUSE', 
                        colour=(18, 104, 135), hover_colour=(52, 168, 212), 
                        bold_text=True, function=pause_game))
    buttons.append(Button(window, WIDTH//1.26-50, 50, 110, 30, text='RESET', 
                        colour=(117, 14, 14), hover_colour=(217, 54, 54), 
                        bold_text=True, function=reset_grid))
    return buttons


def run_game():
    global state
    state = 'running'


def pause_game():
    global state
    state = 'paused'


def reset_grid():
    pass


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_window = Game_window(window, 100, 180)
buttons = make_buttons()
state = 'setting'

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    if state == 'setting':
        get_events()
        update()
        draw()
    if state == 'running':
        running_get_events()
        running_update()
        running_draw()
    if state == 'paused':
        paused_get_events()
        paused_update()
        paused_draw()
    pygame.display.update()
    clock.tick(FPS)
    print(state)
pygame.quit()
#sys.exit()


import pygame
from sys import exit
from grid import Grid

pygame.init()
info_obj = pygame.display.Info()

window_height = info_obj.current_h
window_width = info_obj.current_w
# currently just on 16:9 but * 10
cell_size = info_obj.current_w // 160
FPS = 12

#my native monitor resolution is 1920 x 1080, but I made it a little smaller to fit the screen otherwise the window glitches and becomes borderless for me.
screen = pygame.display.set_mode((window_width,window_height - 72))

pygame.display.set_caption("Game of Life") # it said it, it said the thing!!!! :O
pygame.display.set_icon(pygame.image.load("source/assets/app_icon.png"))
clock = pygame.time.Clock()

grid = Grid(window_width, window_height, cell_size)
# grid.cells[2][1] = 1

# With this loop the game will:
# automatically draw all; 
# update everything.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            # if you want to fullscreen
            pygame.display.toggle_fullscreen()
    
    # blit stands for block image transfer
    screen.fill('white')
    grid.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

import pygame
from sys import exit
from simulation import Simulation
# from grid import Grid

pygame.init()
info_obj = pygame.display.Info()

window_height = info_obj.current_h
window_width = info_obj.current_w
# currently just on 16:9 but * 10
cell_size = info_obj.current_w // 160
FPS = 12

#my native monitor resolution is 1920 x 1080, but I made it a little smaller to fit the screen otherwise the window glitches and becomes borderless for me.
screen = pygame.display.set_mode((window_width,window_height - 72))

pygame.display.set_caption("Game of Life")
pygame.display.set_icon(pygame.image.load("source/assets/app_icon.png"))
clock = pygame.time.Clock()
simulation = Simulation(window_width, window_height, cell_size)

# With this loop the game will:
# automatically draw all; 
# update everything.
while True:
    for event in pygame.event.get():
        # This is important. It allows the user to close the window. And if it didn't exist you wouldn't be able to close the window.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // cell_size
            column = pos[0] // cell_size
            simulation.toggle_cell(row, column)
        
        # Key events    
        if event.type == pygame.KEYDOWN:
            # Return(Enter) for Start, Space for Stop
            if event.key == pygame.K_RETURN:
                simulation.start()
                pygame.display.set_caption("Game of Life - Running")
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("Game of Life - Stopped")
            # F for Faster, S for Slower
            elif event.key == pygame.K_f:
                FPS += 2
            elif event.key == pygame.K_s:
                if FPS > 5:
                    FPS -= 2
            # C for Clear, R for Random
            elif event.key == pygame.K_c:
                simulation.clear()
            elif event.key == pygame.K_r:
                simulation.create_random_state()
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            # if you want to fullscreen
            pygame.display.toggle_fullscreen()
    
    simulation.update()
    screen.fill('white')
    simulation.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

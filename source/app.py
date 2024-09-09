import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Game of Life")
pygame.display.set_icon(pygame.image.load("library/app_icon.png"))

# With this loop the game will:
# automatically draw all; 
# update everything.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

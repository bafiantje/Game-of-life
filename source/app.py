import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Game of Life")
pygame.display.set_icon(pygame.image.load("source/assets/app_icon.png"))
clock = pygame.time.Clock()

test_surface = pygame.Surface((800,400))
test_surface.fill(('Red'))

# With this loop the game will:
# automatically draw all; 
# update everything.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # blit stands for block image transfer
    screen.blit(test_surface, (200,100))

    pygame.display.update()
    clock.tick(30)

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Game of Life")
pygame.display.set_icon(pygame.image.load("source/assets/app_icon.png"))
clock = pygame.time.Clock()
title_font = pygame.font.Font(None, 32)

background_surface = pygame.image.load('source/assets/placeholder_background.png').convert()
front_surface = pygame.Surface([1024,576], pygame.SRCALPHA, 32)
front_surface.convert_alpha()
front_surface.fill((55, 55, 55, 122))

title_surface = title_font.render("Game of Life", True, (0,0,0))
title_background_surface = pygame.Surface([title_surface.get_width() + 20, title_surface.get_height()], pygame.SRCALPHA, 32)
title_background_surface.convert_alpha()
title_background_surface.fill((255, 255, 255, 200))

dead_color = (255,255,255)
alive_color = (0,0,0)

# With this loop the game will:
# automatically draw all; 
# update everything.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # blit stands for block image transfer
    screen.blit(background_surface, (0,0))
    screen.blit(front_surface, (128,72))
    
    screen.blit(title_background_surface, (640 - title_background_surface.get_width() // 2, 72 - title_background_surface.get_height() - 10))
    screen.blit(title_surface, (640 - title_surface.get_width() // 2, 72 - title_surface.get_height() - 10))
    # it said it, it said the thing!!!! :O

    pygame.display.update()
    clock.tick(30)

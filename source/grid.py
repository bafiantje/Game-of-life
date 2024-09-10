import pygame, random

# The class that makes the grid. It doesn't have its own actual grid, 
# rather just made the cells one pixel smaller in height and width, and given they're already accurately placed on a x and y axis, 
# it's not necessary to draw the lines, so the background of the window in the 1 pixel missing space between each cell makes up for the grid.
class Grid:
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        
    def draw(self, window):
        for row in range(self.rows):
            for column in range(self.columns):
                color = (155, 155, 155) if self.cells[row][column] == 0 else (0, 0, 0)
                pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))
                
    def fill_random(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = random.choice([1, 0, 0, 0])
        
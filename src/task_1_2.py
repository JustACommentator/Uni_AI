import pygame
import math
from enum import Enum

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 22
HEIGHT = 22
MARGIN = 3


# ---
# Initialize your classes etc.here
# ---


class Grid:
    size_x: int
    size_y: int
    fields: []

    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.fields = []
        x = 0
        y = 0
        while x < size_x:
            while y < size_y:
                self.fields.append(Field(x, y, 0))
                y += 1
        x += 1


class Field:
    coord_x: int
    coord_y: int
    field_type: int

    def __init__(self, coord_x: int, coord_y: int, field_type: int):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.field_type = field_type


class FieldType(Enum):
    STANDARD = 0,
    BLOCKED = 1,
    START = 2,
    GOAL = 3


pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Practical 1")

done = False

clock = pygame.time.Clock()
grid = Grid(20, 20)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # ---
    # The code here ist called once per clock tick
    # Let your algorithm loop here
    # ---

    screen.fill(BLACK)

    for field in grid.fields:
        x = field.coord_x
        y = field.coord_y
        pygame.draw.rect(screen, WHITE, [(MARGIN + WIDTH) * y + MARGIN, (MARGIN + HEIGHT) * x + MARGIN, WIDTH, HEIGHT])
# ---
# The screen is empty here
# Put your 'drawing' code here
#
#   RECTANGEL EXAMPLE
#
#   The third Parameter defines the rectangles positioning etc: [y-pos,x-pos,width,height]
#   pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * y + MARGIN,
#                        (MARGIN + HEIGHT) * x + MARGIN,WIDTH,HEIGHT])
# ---


pygame.display.flip()

clock.tick(60)

pygame.quit()

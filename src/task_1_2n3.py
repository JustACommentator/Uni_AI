import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 22
HEIGHT = 22
MARGIN = 3
TEXT_OFFSET = 6


# ---
# Initialize your classes etc.here
# ---
class Grid:
    size_x: int
    size_y: int
    fields: []

    def get_field(self, coord_x, coord_y):
        for f in self.fields:
            if f.coord_x == coord_x and f.coord_y == coord_y:
                return f

    def __init__(self, size_x, size_y, use_task_configuration):
        self.size_x = size_x
        self.size_y = size_y
        self.fields = []
        x = 0
        while x < size_x:
            y = 0
            while y < size_y:
                self.fields.append(Field(x, y, 0))
                y += 1
            x += 1

        #Draw 1.3's task configuration
        if use_task_configuration:
            self.get_field(0, 19).field_type = 3
            self.get_field(19, 0).field_type = 2
            x = 0
            y = 16
            while x < 10:
                self.get_field(x, y).field_type = 1
                x += 1
            x = 10
            y = 4
            while y < 10:
                self.get_field(x, y).field_type = 1
                y += 1
            y = 9
            while x < 20:
                self.get_field(x, y).field_type = 1
                x += 1

class Field:
    #field types
    #STANDARD = 0,
    #BLOCKED = 1,
    #START = 2,
    #GOAL = 3

    coord_x: int
    coord_y: int
    field_type: int

    def __init__(self, coord_x: int, coord_y: int, field_type: int):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.field_type = field_type


pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Practical 1")

done = False
display_field_coords = False

clock = pygame.time.Clock()
grid = Grid(20, 20, True)
font = pygame.font.SysFont("arial", 15)
coord_font = pygame.font.SysFont("arial", 10)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # ---
    # The code here ist called once per clock tick
    # Let your algorithm loop here
    # ---

    screen.fill(BLACK)
    #Draw the current grid
    for field in grid.fields:
        x = field.coord_x
        y = field.coord_y
        pygame.draw.rect(screen, WHITE if field.field_type == 0 else BLACK if field.field_type == 1 else BLUE if \
            field.field_type == 2 else GREEN, [(MARGIN + WIDTH) * y + MARGIN / 2, (MARGIN + HEIGHT) * x + MARGIN / 2, \
                                               WIDTH, HEIGHT])

        if field.field_type == 2:
            label = font.render("S", True, WHITE)
            screen.blit(label, ((MARGIN + WIDTH) * y + MARGIN / 2 + TEXT_OFFSET, (MARGIN + HEIGHT) * x + MARGIN / 2))
        elif field.field_type == 3:
            label = font.render("G", True, BLACK)
            screen.blit(label, ((MARGIN + WIDTH) * y + MARGIN / 2 + TEXT_OFFSET, (MARGIN + HEIGHT) * x + MARGIN / 2))
        elif display_field_coords:
            label = coord_font.render(f"{x},{y}", True, BLACK)
            screen.blit(label, ((MARGIN + WIDTH) * y + MARGIN / 2, (MARGIN + HEIGHT) * x + MARGIN / 2))

    pygame.display.update()
pygame.display.flip()

clock.tick(60)

pygame.quit()

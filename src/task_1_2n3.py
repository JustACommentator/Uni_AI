import pygame
import math
from graph import *
from custom_queue import *
from grid import *
from a_star import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

WIDTH = 22
HEIGHT = 22
MARGIN = 3
TEXT_OFFSET = 6

# ---
# Initialize your classes etc.here
# ---


def a_star(grid: Grid, start_node: Node, goal_node: Node):
    q_open = PRIOQueue()
    q_closed = PRIOQueue()

    q_open.enqueue(start_node, 0)

    path = []

    while not q_open.is_empty():
        current_tuple = q_open.dequeue()
        cur_prio = current_tuple[0]
        cur = current_tuple[1]
        q_closed.enqueue(cur, cur_prio)
        grid.get_field_from_node(cur).field_type = 5

        if cur is goal_node:
            c = goal_node
            while c is not None:
                path.append(c.name)
                c = c.parent
            print(path)
            return path

        for end_node, cost in grid.graph.get_neighbours(cur): #[(end, cost),...]
            if grid.get_field_from_node(end_node).field_type != 1 and not q_closed.contains(end_node):
                if not q_open.contains(end_node) or cur.g + cost < end_node.g:
                    end_node.g = cur.g + cost
                    end_node.parent = cur
                    grid.get_field_from_node(end_node).field_type = 4
                    if not q_open.contains(end_node):
                        q_open.enqueue(end_node, end_node.f)

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

#a_star(grid, grid.graph.get_node_from_name('19,0'), grid.graph.get_node_from_name('0,19'))

goal_node = grid.graph.get_node_from_name('0,19')
q_open = PRIOQueue()
q_closed = PRIOQueue()

q_open.enqueue(grid.graph.get_node_from_name('19,0'), 0)

path = []
a_star = AStar(grid, grid.graph.get_node_from_name('19,0'), grid.graph.get_node_from_name('0,19'))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_path = a_star.next_step()
    clock.tick(120)

    #if q_open.is_empty():
        #for p in path:
            #.get_field_from_node(p).field_type = 6
            #clock.tick(30)

    screen.fill(BLACK)
    #Draw the current grid
    for field in grid.fields:
        x = field.coord_x
        y = field.coord_y
        pygame.draw.rect(screen, WHITE if field.field_type == 0 else BLACK if field.field_type == 1 else BLUE if \
            field.field_type == 2 else GREEN if field.field_type == 3 else YELLOW if field.field_type == 4 else RED if field.field_type == 5 else WHITE,
                         [(MARGIN + WIDTH) * y + MARGIN / 2, (MARGIN + HEIGHT) * x + MARGIN / 2, WIDTH, HEIGHT])

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



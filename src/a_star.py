import math
import sys

from graph import *
import utils
from custom_queue import *
from grid import *


class AStar:

    def __init__(self, grid, start_node, goal_node):
        self.q_open = PRIOQueue()
        self.q_closed = PRIOQueue()
        self.grid = grid
        self.start_node = start_node
        self.goal_node = goal_node
        self.path = []

        self.start_node.g = 0
        self.start_node.parent = self.start_node
        self.q_open.enqueue(self.start_node, sys.maxsize - self.get_f(self.start_node))

    def next_step(self):
        if not self.q_open.is_empty():
            current_tuple = self.q_open.dequeue()
            cur_prio = current_tuple[0]
            cur = current_tuple[1]
            self.grid.get_field_from_node(cur).field_type = 5

            if cur is self.goal_node:
                c = self.goal_node
                while c != c.parent:
                    self.grid.get_field_from_node(c).field_type = 6
                    self.path.append(c)
                    c = c.parent
                print(self.path)
                return self.path

            self.q_closed.enqueue(cur, sys.maxsize - cur_prio)

            for neighbour, cost in self.grid.graph.get_neighbours(cur):
                if self.grid.get_field_from_node(neighbour).field_type == 1 or self.q_closed.contains(neighbour):
                    continue

                if self.grid.get_field_from_node(neighbour).field_type != 5:
                    self.grid.get_field_from_node(neighbour).field_type = 4

                if not self.q_closed.contains(neighbour):
                    if not self.q_open.contains(neighbour):
                        neighbour.g = sys.maxsize
                        neighbour.parent = None
                self.update_vertex(cur, neighbour, cost)
            #return "no path found"

    def update_vertex(self, node, neighbour, cost):
        if not self.q_open.contains(neighbour) and node.g + cost < neighbour.g:
            neighbour.g = node.g + self.get_edge_cost(node, neighbour)
            neighbour.parent = node

            #if self.q_open.contains(neighbour):
                #self.q_open.remove(neighbour)

            if not self.q_open.contains(neighbour):
                self.q_open.enqueue(neighbour, sys.maxsize - self.get_f(neighbour))

    def get_f(self, node: Node):
        g_cost = 0
        c = node
        while c != c.parent:
            g_cost += self.get_edge_cost(c, c.parent)
            c = c.parent
        goal_field = self.grid.get_field_from_node(self.goal_node)
        node_field = self.grid.get_field_from_node(node)
        h_cost = math.sqrt(math.pow(goal_field.coord_x-node_field.coord_x, 2) + math.pow(goal_field.coord_y-node_field.coord_y, 2))
        return g_cost + h_cost

    def get_edge_cost(self, start, end):
        for x in self.grid.graph.nodes:
            if x == start:
                for edge in x.edges:
                    if edge.end == end:
                        return edge.value

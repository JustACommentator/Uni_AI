from graph import *
import math


class Grid:
    size_x: int
    size_y: int
    fields: []
    graph: Graph

    def get_field(self, coord_x, coord_y):
        for f in self.fields:
            if f.coord_x == coord_x and f.coord_y == coord_y:
                return f

    def get_field_from_node(self, node: Node):
        for f in self.fields:
            if f.identifier == node.name:
                return f

    def __init__(self, size_x, size_y, use_task_configuration):
        self.size_x = size_x
        self.size_y = size_y
        self.fields = []
        field_names = []
        field_links = []
        #Weise jedem Knoten eine ID zu: ID=x,y
        #Die ID ist der NodeName

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

        for fx in self.fields:
            field_names.append(fx.identifier)
            linked_nodes = [] #start, Ziel, Kosten

            if fx.coord_x > 0 and self.get_field(fx.coord_x-1, fx.coord_y).field_type != 1:
                linked_nodes.append((fx.identifier, self.get_field(fx.coord_x-1, fx.coord_y).identifier, 1))
            if fx.coord_x < size_x - 1 and self.get_field(fx.coord_x+1, fx.coord_y).field_type != 1:
                linked_nodes.append((fx.identifier, self.get_field(fx.coord_x+1, fx.coord_y).identifier, 1))
            if fx.coord_y > 0 and self.get_field(fx.coord_x, fx.coord_y-1).field_type != 1:
                linked_nodes.append((fx.identifier, self.get_field(fx.coord_x, fx.coord_y-1).identifier, 1))
            if fx.coord_y < size_y - 1 and self.get_field(fx.coord_x, fx.coord_y + 1).field_type != 1:
                linked_nodes.append((fx.identifier, self.get_field(fx.coord_x, fx.coord_y + 1).identifier, 1))
            #if fx.coord_x > 0 and fx.coord_y > 0 and self.get_field(fx.coord_x - 1, fx.coord_y - 1).field_type != 1:
            #    linked_nodes.append((fx.identifier, self.get_field(fx.coord_x-1, fx.coord_y - 1).identifier, math.sqrt(2)))
           # if fx.coord_x < size_x - 1 and fx.coord_y > 0 and self.get_field(fx.coord_x + 1, fx.coord_y - 1).field_type != 1:
           #     linked_nodes.append((fx.identifier, self.get_field(fx.coord_x + 1, fx.coord_y - 1).identifier, math.sqrt(2)))
            #if fx.coord_x > 0 and fx.coord_y < size_y-1 and self.get_field(fx.coord_x - 1, fx.coord_y + 1).field_type != 1:
            #    linked_nodes.append((fx.identifier, self.get_field(fx.coord_x - 1, fx.coord_y + 1).identifier, math.sqrt(2)))
            #if fx.coord_x < size_x - 1 and fx.coord_y < size_y-1 and self.get_field(fx.coord_x + 1, fx.coord_y + 1).field_type != 1:
            #    linked_nodes.append((fx.identifier, self.get_field(fx.coord_x + 1, fx.coord_y + 1).identifier, math.sqrt(2)))

            for fxx in linked_nodes:
                field_links.append(fxx)

        self.graph = Graph(field_names, field_links)


class Field:
    #field types
    #STANDARD = 0,
    #BLOCKED = 1,
    #START = 2,
    #GOAL = 3
    #WATCHED = 4
    #CLOSED = 5

    coord_x: int
    coord_y: int
    field_type: int
    identifier: str

    def __init__(self, coord_x: int, coord_y: int, field_type: int):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.field_type = field_type
        self.identifier = f'{self.coord_x},{self.coord_y}'


from graph import *
import utils
from custom_queue import *

class AStar:
    q_open = PRIOQueue()
    q_closed = PRIOQueue()

    def __init__(self, s_start, s_goal):
        self.q_open = PRIOQueue()
        self.q_closed = PRIOQueue()
        self.a_star_next(s_start, s_goal)

    #test
    #open and close as priority queues
    def a_star_next(self, s_start, s_goal):
        self.a_star_initialize(s_start)
        while not self.q_open.is_empty():
            s = self.q_open.dequeue()
            if s is s_goal:
                return path
            self.q_closed.enqueue(s)
            for s_o in get_neighbours(s):
                if s_o not in self.q_closed.queue and s_o not in self.q_open.queue:
                    s_o.g = -1#infinite
                    s_o.parents = None
                self.a_star_update_vertex(s, s_o)
            return "No path was found"

    def a_star_initialize(self, s_start):
        s_start.g = 0
        s_start.parent = s_start
        self.q_open.enqueue(s_start, f(s_start))
        self.q_closed.clear()

    def a_star_update_vertex(self, s, s_o):
        if s.g + c(s, s_o) < s_o.g: #c = cost
            s_o.g = s.g + c(s, s_o)
            s_o.parent = s
            if s_o in self.q_open.queue:
                self.q_open.remove(s_o)
            self.q_open.enqueue(s_o, f(s_o))
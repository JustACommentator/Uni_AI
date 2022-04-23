from graph import Node


class FIFOQueue:
    current: Node
    queue: []

    def __init__(self):
        self.current = None
        self.queue = []

    def enqueue(self, target: Node):
        self.queue.append(target)
        if len(self.queue) > 0:
            self.current = self.queue[0]
        else:
            self.current = None

    def dequeue(self):
        target = self.current
        new_queue = []
        i = 1
        while i < len(self.queue):
            new_queue.append(self.queue[i])
            i += 1
        self.queue = new_queue
        if len(self.queue) > 0:
            self.current = self.queue[0]

        return target

    def is_empty(self):
        return len(self.queue) == 0


class LIFOQueue:
    current: Node
    queue: []

    def __init__(self):
        self.current = None
        self.queue = []

    def enqueue(self, target: Node):
        self.queue.append(target)
        self.current = target

    def dequeue(self):
        target = self.current
        new_queue = []
        i = 0
        while i < (len(self.queue) - 1):
            new_queue.append(self.queue[i])
            i += 1
        self.queue = new_queue
        if len(self.queue) > 0:
            self.current = self.queue[len(self.queue) - 1]
        else:
            self.current = None
        return target

    def is_empty(self):
        return len(self.queue) == 0


class PRIOQueue:
    current: Node
    queue: []

    def __init__(self):
        self.current = None
        self.queue = []

    def enqueue(self, target: Node, priority: int):
        self.queue.append((priority, target))
        self.queue.sort(reverse=True, key=lambda x: x[0])
        self.current = self.queue[0]

    def dequeue(self):
        target = self.current
        new_queue = []
        i = 1
        while i < len(self.queue):
            new_queue.append(self.queue[i])
            i += 1
        self.queue = new_queue
        self.queue.sort(reverse=True, key=lambda x: x[0])
        if len(self.queue) > 0:
            self.current = self.queue[0]
        else:
            self.current = None
        return target

    def is_empty(self):
        return len(self.queue) == 0

    def clear(self):
        self.current = None
        self.queue = []

    def remove(self, target: Node):
        new_queue = []
        i = 1
        while i < len(self.queue):
            if self.queue[i] is not target:
                new_queue.append(self.queue[i])
            i += 1

        if target is self.current:
            self.current = self.queue[0]

        self.queue = new_queue

    def contains(self, target: Node):
        for x in self.queue:
            if x[1] is target:
                return True
        return False

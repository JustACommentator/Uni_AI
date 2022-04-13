from typing import Generic, TypeVar

T = TypeVar('T')


class FIFOQueue:
    current: T
    queue: []

    def __init__(self):
        self.current = None
        self.queue = []

    def enqueue(self, target: T):
        self.queue.append(target)
        if self.current is None:
            self.current = target

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


class LIFOQueue(Generic[T]):
    current: T
    queue: []

    def __init__(self):
        self.current = None
        self.queue = []

    def enqueue(self, target: T):
        self.queue.append(target)
        self.current = target

    def dequeue(self):
        target = self.current
        new_queue = []
        i = 0
        while i < (len(self.queue)-1):
            new_queue.append(self.queue[i])
            i += 1
        self.queue = new_queue
        return target

    def is_empty(self):
        return len(self.queue) == 0


class PRIOQueue(Generic[T]):
    current: T
    queue: []

    def __init__(self):
        self.current = None
        self.queue = []

    def enqueue(self, target: T, priority: int):
        self.queue.append((priority, target))
        self.queue.sort(reverse=True)
        self.current = self.queue[0]

    def dequeue(self):
        target = self.current
        new_queue = []
        i = 1
        while i < len(self.queue):
            new_queue.append(self.queue[i])
            i += 1
        self.queue = new_queue
        return target

    def is_empty(self):
        return len(self.queue) == 0

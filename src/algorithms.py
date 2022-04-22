from graph import *
from queue import *


def new_bfs(graph: Graph, start_node: Node, end_node: Node):
    print("BFS: " + start_node.name + " -> " + end_node.name + ":")
    visited = []
    path = []
    totalCost = 0
    queue = FIFOQueue()
    current_node = None
    queue.enqueue((start_node, None))
    visited.append((start_node, None))
    while not queue.is_empty():
        current_node = queue.dequeue()

        if current_node[0] is end_node:
            break

        for link in current_node[0].links:
            target: Node = graph.get_node_from_name(link.link_target)
            if target not in visited:
                queue.enqueue((target, current_node[0]))
                visited.append((target, current_node[0]))

    if current_node[0] is not end_node:
        print("Goal not reachable")
    else:
        while current_node[0] is not None:
            path.append(current_node[0])
            for origin, enqued_by in visited:
                if origin is current_node[1]:
                    current_node = (origin, enqued_by)
                    if origin is not start_node:
                        totalCost += graph.get_link_from_nodes(enqued_by, origin).link_cost

    path.reverse()
    print("Path:")
    for node in path:
        print(node.node_name)
    print("Cost: " + totalCost)


def bfs(graph, start, goal):
    visited = []
    queue = FIFOQueue()
    current_node = None

    visited.append((start, None))
    queue.enqueue((start, None))

    while not queue.is_empty():
        current_node = queue.dequeue()

        if current_node is goal:
            break

        for edge in current_node[0].edges:
            target = graph.get_node_from_name(edge.end)
            if target not in visited:
                queue.enqueue((target, current_node[0]))
                visited.append((target, current_node[0]))

    if current_node is not goal:
        print("Gaol not reachable")
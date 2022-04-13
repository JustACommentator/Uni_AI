from graph import Graph
from node import Node
from queue import *


def bfs(graph: Graph, start_node: Node, end_node: Node):
    print("BFS: " + start_node.node_name + " -> " + end_node.node_name)
    visited_nodes = []
    path = []
    queue = FIFOQueue()
    queue.enqueue(start_node)
    visited_nodes.append(start_node)
    while not queue.is_empty():
        current_node: Node = queue.dequeue()

        if current_node is None:
            break

        #TODO: Warum zum FFFFFFFFFFFFFFFFFFFF konvertiert der den currentNode bitte in einen str?!?!?!
        print_result = current_node.node_name + ': '

        for link in current_node.links:
            print_result += link.link_target + '(' + str(link.link_cost) + ") "
            if link.link_target not in visited_nodes:
                if link.link_target is end_node:
                    path.append((link.link_cost, link.link_target))
                    return path
                else:
                    visited_nodes.append(link.link_target)
                    queue.enqueue(link.link_target)
                    print("Enqueueing " + link.link_target)

        print(print_result)


def dfs(graph: Graph):
    print(graph)


def ucs(graph: Graph):
    print(graph)

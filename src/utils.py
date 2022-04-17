from graph import Graph
from node import Node
from queue import *


def link_list_from_node_list(graph, nodes):
    linkPath = []
    for i in range(nodes.len()):
        return



def new_bfs(graph: Graph, start_node: Node, end_node: Node):
    print("BFS: " + start_node.node_name + " -> " + end_node.node_name + ":")
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

def bfs(graph: Graph, start_node: Node, end_node: Node):
    print("BFS: " + start_node.node_name + " -> " + end_node.node_name)
    visited_nodes = []
    path = []
    queue = FIFOQueue()
    queue.enqueue(start_node)
    visited_nodes.append(start_node)
    while not queue.is_empty():
        current_node = queue.dequeue()

        if current_node is None:
            break

        node_name = current_node.node_name
        print_result = node_name + ': '

        # TODO @Tarik: eingeschlagenen Weg in path speichern + Path Cost berechnen und ausgeben
        for link in current_node.links:
            target: Node = graph.get_node_from_name(link.link_target)
            print_result += target.node_name + '(' + str(link.link_cost) + ") "
            if current_node is not end_node and target not in visited_nodes:
                visited_nodes.append(target)
                queue.enqueue(target)
        #print(print_result)

        if current_node is end_node:
            break

    print_result = "Path (Cost: " + "): "
    for node in path:
        if node is end_node:
            print_result += end_node.node_name
        else:
            print_result += node.node_name + " -> "
    print(print_result)
    return path


def dfs(graph: Graph, start_node: Node, end_node: Node):
    print("DFS:" + start_node.node_name + " -> " + end_node.node_name)
    visited_nodes = []
    path = []
    queue = LIFOQueue()
    queue.enqueue(start_node)
    visited_nodes.append(start_node)
    while not queue.is_empty():
        current_node = queue.dequeue()

        if current_node is None:
            break

        node_name = current_node.node_name
        print_result = node_name + ': '

        # TODO @Tarik: eingeschlagenen Weg in path speichern + Path Cost berechnen und ausgeben
        for link in current_node.links:
            target: Node = graph.get_node_from_name(link.link_target)
            print_result += target.node_name + '(' + str(link.link_cost) + ") "
            if current_node is not end_node and target not in visited_nodes:
                visited_nodes.append(target)
                queue.enqueue(target)

        #print(print_result)

        if current_node is end_node:
            break

    print_result = "Path (Cost: " + "): "
    for node in path:
        if node is end_node:
            print_result += end_node.node_name
        else:
            print_result += node.node_name + " -> "
    print(print_result)
    return path

#TODO ucs funktioniert nicht richtig. Siehe Nilusches Werte auf Ilias.
def ucs(graph: Graph, start_node: Node, end_node: Node):
    print("UCS:" + start_node.node_name + " -> " + end_node.node_name)
    visited_nodes = []
    path = []
    queue = PRIOQueue()
    queue.enqueue(start_node, 0)
    visited_nodes.append(start_node)
    while not queue.is_empty():
        current_prio, current_node = queue.dequeue()

        if current_node is None:
            break

        node_name = current_node.node_name
        print_result = node_name + ': '

        # TODO @Tarik: Kürzesten Weg finden und die Knoten in 'path' abspeichern + Path Cost berechnen und ausgeben
        for link in current_node.links:
            target: Node = graph.get_node_from_name(link.link_target)
            print_result += target.node_name + '(' + str(link.link_cost) + ") "
            if current_node is not end_node and target not in visited_nodes:
                visited_nodes.append(target)
                queue.enqueue(target, current_prio + 1)

        print(print_result)

        if current_node is end_node:
            break

    print_result = "Path (Cost: " + "): "
    for node in path:
        if node is end_node:
            print_result += end_node.node_name
        else:
            print_result += node.node_name + " -> "
    print(print_result)
    return path

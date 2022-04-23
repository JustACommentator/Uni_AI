from graph import Graph
from custom_queue import *
import sys


def bfs(graph: Graph, start_node_name: str, goal_node_name: str):
    print('BFS:', start_node_name, "->", goal_node_name)
    start_node = graph.get_node_from_name(start_node_name)
    goal_node = graph.get_node_from_name(goal_node_name)
    visited_nodes = []
    path = [] #(Node, ParentNode, cost)

    queue = FIFOQueue()
    queue.enqueue(start_node)
    visited_nodes.append(start_node)
    path.append((start_node, None, 0))
    while not queue.is_empty():
        current_node = queue.dequeue()

        if current_node is None:
            break

        node_name = current_node.name
        print_result = node_name + ': '

        for link in current_node.edges:
            target: Node = link.end
            print_result += target.name + '(' + str(link.value) + ") "
            if current_node is not goal_node and target not in visited_nodes:
                visited_nodes.append(target)
                queue.enqueue(target)
                path.append((target, current_node, link.value))
            elif current_node is goal_node:
                path.append((target, current_node, link.value))

        #print(print_result)

        if current_node is goal_node:
            break

    final_cost = 0
    final_path = []
    current = None
    for p in path:
        if p[0] is goal_node:
            current = p
            break

    if current is None:
        print("If you're reading this, something went wrong.")
        return

    last = current
    while current is not None:
        final_cost += current[2]
        last = current
        final_path.append(current[0])
        for x, y, z in path:
            if x is current[1]:
                current = (x, y, z)
                break

        if current is last:
            current = None

    final_path = reversed(final_path)
    print("Path Cost:", final_cost)
    print_result = "Path Result: "
    for p in final_path:
        print_result += p.name + ("->" if p is not goal_node else "")

    print(print_result)
    return final_path, final_cost


def dfs(graph: Graph, start_node_name: str, goal_node_name: str):
    print('DFS:', start_node_name, "->", goal_node_name)
    start_node = graph.get_node_from_name(start_node_name)
    goal_node = graph.get_node_from_name(goal_node_name)
    visited_nodes = []
    path = []  # (Node, ParentNode, cost)

    queue = LIFOQueue()
    queue.enqueue(start_node)
    visited_nodes.append(start_node)
    path.append((start_node, None, 0))
    while not queue.is_empty():
        current_node = queue.dequeue()

        if current_node is None:
            break

        node_name = current_node.name
        print_result = node_name + ': '

        for link in current_node.edges:
            target: Node = link.end
            print_result += target.name + '(' + str(link.value) + ") "
            if current_node is not goal_node and target not in visited_nodes:
                visited_nodes.append(target)
                queue.enqueue(target)
                path.append((target, current_node, link.value))
            elif current_node is goal_node:
                path.append((target, current_node, link.value))

        # print(print_result)

        if current_node is goal_node:
            break

    final_cost = 0
    final_path = []
    current = None
    for p in path:
        if p[0] is goal_node:
            current = p
            break

    if current is None:
        print("If you're reading this, something went wrong.")
        return

    last = current
    while current is not None:
        final_cost += current[2]
        last = current
        final_path.append(current[0])
        for x, y, z in path:
            if x is current[1]:
                current = (x, y, z)
                break

        if current is last:
            current = None

    final_path = reversed(final_path)
    print("Path Cost:", final_cost)
    print_result = "Path Result: "
    for p in final_path:
        print_result += p.name + ("->" if p is not goal_node else "")

    print(print_result)
    return final_path, final_cost


def ucs(graph: Graph, start_node_name: str, goal_node_name: str):
    print('UCS:', start_node_name, "->", goal_node_name)
    start_node = graph.get_node_from_name(start_node_name)
    goal_node = graph.get_node_from_name(goal_node_name)
    visited_nodes = []
    path = []  # (Node, ParentNode, cost)

    queue = PRIOQueue()
    queue.enqueue(start_node, 0)
    visited_nodes.append(start_node)
    path.append((start_node, None, 0))
    while not queue.is_empty():
        current_prio, current_node = queue.dequeue()

        if current_node is None:
            break

        node_name = current_node.name
        print_result = node_name + ': '

        for link in current_node.edges:
            target: Node = link.end
            print_result += target.name + '(' + str(link.value) + ") "
            if current_node is not goal_node and target not in visited_nodes:
                visited_nodes.append(target)
                cumulative_distance = link.value + (sys.maxsize-current_prio)
                queue.enqueue(target, sys.maxsize - cumulative_distance)
                path.append((target, current_node, link.value))
            elif current_node is goal_node:
                path.append((target, current_node, link.value))

        #print(print_result)

        if current_node is goal_node:
            break

    final_cost = 0
    final_path = []
    current = None
    for p in path:
        if p[0] is goal_node:
            current = p
            break

    if current is None:
        print("If you're reading this, something went wrong.")
        return

    last = current
    while current is not None:
        final_cost += current[2]
        last = current
        final_path.append(current[0])
        for x, y, z in path:
            if x is current[1]:
                current = (x, y, z)
                break

        if current is last:
            current = None

    final_path = reversed(final_path)
    print("Path Cost:", final_cost)
    print_result = "Path Result: "
    for p in final_path:
        print_result += p.name + ("->" if p is not goal_node else "")

    print(print_result)
    return final_path, final_cost


from node import Node


class Graph:
    node_names: []
    nodes: []
    paths: []

    def __init__(self, node_names, paths, is_undirected: bool = True):
        self.node_names = node_names
        self.nodes = []
        self.paths = []

        for node_name in node_names:
            used_paths = []
            for (start, end, cost) in paths:
                if start is node_name:
                    used_paths.append((end, cost))
                    self.paths.append((start, end, cost))
                elif end is node_name and is_undirected:
                    used_paths.append((start, cost))
            node = Node(node_name, used_paths)
            self.nodes.append(node)

    def __str__(self):
        result = 'Graph Data:\n\nAll Nodes:'
        for node_name in self.node_names:
            result += '\n' + node_name
        result += '\n\nAll Edges:'
        for (start, end, cost) in self.paths:
            result += '\nFrom ' + start + ' to ' + end + ': ' + str(cost)

        return result

    def get_node_from_name(self, node_name: str):
        for node in self.nodes:
            if node.node_name is node_name:
                return node

    def get_link_from_nodes(self, node1, node2):
        for link in node1.links:
            if link.link_target is node2:
                return link

        return None;
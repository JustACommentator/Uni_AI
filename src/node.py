class Node:
    node_name: str
    links: []

    def __init__(self, node_name: str, links):
        self.node_name = node_name
        self.links = []

        for (end, cost) in links:
            self.links.append(Link(end, cost))


class Link:
    link_target: Node
    link_cost: int

    def __init__(self, link_target: Node, link_cost):
        self.link_target = link_target
        self.link_cost = link_cost


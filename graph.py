from node import Node
from collections import deque


class Graph:
    def __init__(self):
        self.nodes = []

    def probe_node(self, node_name):
        for node in self.nodes:
            if node_name == node.name:
                return node.get_neighbors()

    def add_node(self, node):
        self.nodes.append(node)


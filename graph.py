from node import Node
from collections import deque


class Graph:
    def __init__(self):
        self.nodes = []

    def get_distances_from_node(self, node_name):
        # Create a dictionary to hold distances
        distances = {node.name: float('inf') for node in self.nodes}
        distances[node_name] = 0

        # Create a queue for BFS
        queue = deque([node_name])

        while queue:
            current_node_name = queue.popleft()
            current_distance = distances[current_node_name]

            # Get the neighbors of the current node
            current_node_neighbors = self.probe_node(current_node_name)

            for neighbor in current_node_neighbors:
                if distances[neighbor] == float('inf'):  # Not visited yet
                    distances[neighbor] = current_distance + 1
                    queue.append(neighbor)

        return distances

    def probe_node(self, node_name):
        for node in self.nodes:
            if node_name == node.name:
                return node.get_neighbors()

    def add_node(self, node):
        self.nodes.append(node)


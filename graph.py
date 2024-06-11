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


def create_franklin_graph():
    franklin_graph = Graph()

    a = Node("A", ["B", "C", "E"])
    b = Node("B", ["A", "D", "H"])
    c = Node("C", ["A", "F", "J"])
    d = Node("D", ["B", "G", "I"])
    e = Node("E", ["A", "F", "K"])
    f = Node("F", ["C", "E", "G"])
    g = Node("G", ["D", "F", "H"])
    h = Node("H", ["B", "G", "L"])
    i = Node("I", ["D", "J", "K"])
    j = Node("J", ["C", "I", "L"])
    k = Node("K", ["E", "I", "L"])
    l = Node("L", ["H", "J", "K"])

    franklin_graph.add_node(a)
    franklin_graph.add_node(b)
    franklin_graph.add_node(c)
    franklin_graph.add_node(d)
    franklin_graph.add_node(e)
    franklin_graph.add_node(f)
    franklin_graph.add_node(g)
    franklin_graph.add_node(h)
    franklin_graph.add_node(i)
    franklin_graph.add_node(j)
    franklin_graph.add_node(k)
    franklin_graph.add_node(l)

    return franklin_graph

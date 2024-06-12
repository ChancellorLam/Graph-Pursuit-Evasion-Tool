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


def create_loupekine_snark():
    loupekine_snark = Graph()

    a = Node("A", ["B", "C", "K"])
    b = Node("B", ["A", "F", "O"])
    c = Node("C", ["A", "H", "L"])
    d = Node("D", ["E", "G", "L"])
    e = Node("E", ["D", "J", "N"])
    f = Node("F", ["B", "I", "N"])
    g = Node("G", ["D", "H", "K"])
    h = Node("H", ["C", "G", "M"])
    i = Node("I", ["F", "J", "M"])
    j = Node("J", ["E", "I", "O"])
    k = Node("K", ["A", "G", "U"])
    l = Node("L", ["C", "D", "Q"])
    m = Node("M", ["H", "I", "P"])
    n = Node("N", ["E", "F", "R"])
    o = Node("O", ["B", "J", "V"])
    p = Node("P", ["M", "S", "T"])
    q = Node("Q", ["L", "R", "T"])
    r = Node("R", ["N", "Q", "S"])
    s = Node("S", ["P", "R", "U"])
    t = Node("T", ["P", "Q", "V"])
    u = Node("U", ["K", "S", "V"])
    v = Node("V", ["O", "T", "U"])

    loupekine_snark.add_node(a)
    loupekine_snark.add_node(b)
    loupekine_snark.add_node(c)
    loupekine_snark.add_node(d)
    loupekine_snark.add_node(e)
    loupekine_snark.add_node(f)
    loupekine_snark.add_node(g)
    loupekine_snark.add_node(h)
    loupekine_snark.add_node(i)
    loupekine_snark.add_node(j)
    loupekine_snark.add_node(k)
    loupekine_snark.add_node(l)
    loupekine_snark.add_node(m)
    loupekine_snark.add_node(n)
    loupekine_snark.add_node(o)
    loupekine_snark.add_node(p)
    loupekine_snark.add_node(q)
    loupekine_snark.add_node(r)
    loupekine_snark.add_node(s)
    loupekine_snark.add_node(t)
    loupekine_snark.add_node(u)
    loupekine_snark.add_node(v)

    return loupekine_snark


def create_double_star_snark():
    double_star_snark = Graph()

    node1 = Node("1", ["2", "9", "27"])
    node2 = Node("2", ["1", "3", "5"])
    node3 = Node("3", ["2", "7", "25"])
    node4 = Node("4", ["5", "18", "24"])
    node5 = Node("5", ["2", "4", "6"])
    node6 = Node("6", ["5", "16", "22"])
    node7 = Node("7", ["3", "8", "15"])
    node8 = Node("8", ["7", "9", "11"])
    node9 = Node("9", ["1", "8", "13"])
    node10 = Node("10", ["11", "24", "30"])
    node11 = Node("11", ["8", "10", "12"])
    node12 = Node("12", ["11", "22", "28"])
    node13 = Node("13", ["9", "14", "21"])
    node14 = Node("14", ["13", "15", "17"])
    node15 = Node("15", ["7", "14", "19"])
    node16 = Node("16", ["6", "17", "30"])
    node17 = Node("17", ["14", "16", "18"])
    node18 = Node("18", ["4", "17", "28"])
    node19 = Node("19", ["15", "20", "27"])
    node20 = Node("20", ["19", "21", "23"])
    node21 = Node("21", ["13", "20", "25"])
    node22 = Node("22", ["6", "12", "23"])
    node23 = Node("23", ["20", "22", "24"])
    node24 = Node("24", ["4", "10", "23"])
    node25 = Node("25", ["3", "21", "26"])
    node26 = Node("26", ["25", "27", "29"])
    node27 = Node("27", ["1", "19", "26"])
    node28 = Node("28", ["12", "18", "29"])
    node29 = Node("29", ["26", "28", "30"])
    node30 = Node("30", ["10", "16", "29"])

    double_star_snark.add_node(node1)
    double_star_snark.add_node(node2)
    double_star_snark.add_node(node3)
    double_star_snark.add_node(node4)
    double_star_snark.add_node(node5)
    double_star_snark.add_node(node6)
    double_star_snark.add_node(node7)
    double_star_snark.add_node(node8)
    double_star_snark.add_node(node9)
    double_star_snark.add_node(node10)
    double_star_snark.add_node(node11)
    double_star_snark.add_node(node12)
    double_star_snark.add_node(node13)
    double_star_snark.add_node(node14)
    double_star_snark.add_node(node15)
    double_star_snark.add_node(node16)
    double_star_snark.add_node(node17)
    double_star_snark.add_node(node18)
    double_star_snark.add_node(node19)
    double_star_snark.add_node(node20)
    double_star_snark.add_node(node21)
    double_star_snark.add_node(node22)
    double_star_snark.add_node(node23)
    double_star_snark.add_node(node24)
    double_star_snark.add_node(node25)
    double_star_snark.add_node(node26)
    double_star_snark.add_node(node27)
    double_star_snark.add_node(node28)
    double_star_snark.add_node(node29)
    double_star_snark.add_node(node30)

    return double_star_snark

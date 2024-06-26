from itertools import combinations

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

    def compute_distance_matrix(self):
        distance_matrix = {}
        for node in self.nodes:
            distance_matrix[node.name] = self.get_distances_from_node(node.name)
        return distance_matrix

    def get_metric_dimension(self):
        distance_matrix = self.compute_distance_matrix()

        for r in range(1, len(self.nodes) + 1):
            for candidate_set in combinations(self.nodes, r):
                if is_resolving_set(self, candidate_set, distance_matrix):
                    return r, [node.name for node in candidate_set]

        return None

    def probe_node(self, node_name):
        for node in self.nodes:
            if node_name == node.name:
                return node.get_neighbors()

    def add_node(self, node):
        self.nodes.append(node)


def is_resolving_set(graph, candidate_set, distance_matrix):
    all_distances = []

    for node in graph.nodes:
        distances = tuple(distance_matrix[node.name][cand.name] for cand in candidate_set)
        all_distances.append(distances)

    return len(all_distances) == len(set(all_distances))


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


def create_szekeres_snark():
    szekeres_snark = Graph()

    node1 = Node('A', ['B', 'E', 'C'])
    node2 = Node('B', ['D', 'O', 'A'])
    node3 = Node('C', ['A', 'N', 'F'])
    node4 = Node('D', ['KK', 'G', 'B'])
    node5 = Node('E', ['A', 'G', 'H'])
    node6 = Node('F', ['C', 'H', 'LL'])
    node7 = Node('G', ['D', 'E', 'N'])
    node8 = Node('H', ['F', 'E', 'O'])
    node9 = Node('I', ['K', 'M', 'J'])
    node10 = Node('J', ['I', 'P', 'L'])
    node11 = Node('K', ['Q', 'Y', 'I'])
    node12 = Node('L', ['J', 'Z', 'R'])
    node13 = Node('M', ['I', 'S', 'U'])
    node14 = Node('N', ['G', 'C', 'Z'])
    node15 = Node('O', ['B', 'H', 'Y'])
    node16 = Node('P', ['V', 'J', 'T'])
    node17 = Node('Q', ['W', 'K', 'S'])
    node18 = Node('R', ['L', 'T', 'X'])
    node19 = Node('S', ['P', 'BB', 'AA'])
    node20 = Node('T', ['R', 'CC', 'DD'])
    node21 = Node('U', ['M', 'W', 'II'])
    node22 = Node('V', ['P', 'X', 'JJ'])
    node23 = Node('W', ['Q', 'AA', 'U'])
    node24 = Node('X', ['R', 'DD', 'VV'])
    node25 = Node('Y', ['K', 'BB', 'O'])
    node26 = Node('Z', ['N', 'L', 'CC'])
    node27 = Node('AA', ['W', 'BB', 'TT'])
    node28 = Node('BB', ['AA', 'S', 'Y'])
    node29 = Node('CC', ['Z', 'T', 'DD'])
    node30 = Node('DD', ['CC', 'X', 'SS'])
    node31 = Node('EE', ['KK', 'FF', 'MM'])
    node32 = Node('FF', ['EE', 'GG', 'WW'])
    node33 = Node('GG', ['FF', 'HH', 'XX'])
    node34 = Node('HH', ['GG', 'LL', 'NN'])
    node35 = Node('II', ['U', 'QQ', 'OO'])
    node36 = Node('JJ', ['V', 'RR', 'PP'])
    node37 = Node('KK', ['D', 'EE', 'QQ'])
    node38 = Node('LL', ['F', 'HH', 'RR'])
    node39 = Node('MM', ['EE', 'UU', 'OO'])
    node40 = Node('NN', ['PP', 'HH', 'VV'])
    node41 = Node('OO', ['II', 'MM', 'SS'])
    node42 = Node('PP', ['JJ', 'NN', 'TT'])
    node43 = Node('QQ', ['KK', 'II', 'UU'])
    node44 = Node('RR', ['JJ', 'LL', 'VV'])
    node45 = Node('SS', ['OO', 'DD', 'WW'])
    node46 = Node('TT', ['PP', 'AA', 'XX'])
    node47 = Node('UU', ['QQ', 'MM', 'WW'])
    node48 = Node('VV', ['NN', 'XX', 'RR'])
    node49 = Node('WW', ['FF', 'UU', 'SS'])
    node50 = Node('XX', ['TT', 'GG', 'VV'])

    szekeres_snark.add_node(node1)
    szekeres_snark.add_node(node2)
    szekeres_snark.add_node(node3)
    szekeres_snark.add_node(node4)
    szekeres_snark.add_node(node5)
    szekeres_snark.add_node(node6)
    szekeres_snark.add_node(node7)
    szekeres_snark.add_node(node8)
    szekeres_snark.add_node(node9)
    szekeres_snark.add_node(node10)
    szekeres_snark.add_node(node11)
    szekeres_snark.add_node(node12)
    szekeres_snark.add_node(node13)
    szekeres_snark.add_node(node14)
    szekeres_snark.add_node(node15)
    szekeres_snark.add_node(node16)
    szekeres_snark.add_node(node17)
    szekeres_snark.add_node(node18)
    szekeres_snark.add_node(node19)
    szekeres_snark.add_node(node20)
    szekeres_snark.add_node(node21)
    szekeres_snark.add_node(node22)
    szekeres_snark.add_node(node23)
    szekeres_snark.add_node(node24)
    szekeres_snark.add_node(node25)
    szekeres_snark.add_node(node26)
    szekeres_snark.add_node(node27)
    szekeres_snark.add_node(node28)
    szekeres_snark.add_node(node29)
    szekeres_snark.add_node(node30)
    szekeres_snark.add_node(node31)
    szekeres_snark.add_node(node32)
    szekeres_snark.add_node(node33)
    szekeres_snark.add_node(node34)
    szekeres_snark.add_node(node35)
    szekeres_snark.add_node(node36)
    szekeres_snark.add_node(node37)
    szekeres_snark.add_node(node38)
    szekeres_snark.add_node(node39)
    szekeres_snark.add_node(node40)
    szekeres_snark.add_node(node41)
    szekeres_snark.add_node(node42)
    szekeres_snark.add_node(node43)
    szekeres_snark.add_node(node44)
    szekeres_snark.add_node(node45)
    szekeres_snark.add_node(node46)
    szekeres_snark.add_node(node47)
    szekeres_snark.add_node(node48)
    szekeres_snark.add_node(node49)
    szekeres_snark.add_node(node50)

    return szekeres_snark


def create_second_blanusa_snark():
    second_blanusa_snark = Graph()

    node1 = Node("A", ["B", "C", "E"])
    node2 = Node("B", ["A", "D", "K"])
    node3 = Node("C", ["A", "M", "N"])
    node4 = Node("D", ["B", "P", "Q"])
    node5 = Node("E", ["A", "F", "L"])
    node6 = Node("F", ["E", "G", "N"])
    node7 = Node("G", ["F", "H", "M"])
    node8 = Node("H", ["G", "I", "O"])
    node9 = Node("I", ["H", "J", "Q"])
    node10 = Node("J", ["I", "K", "P"])
    node11 = Node("K", ["B", "J", "R"])
    node12 = Node("L", ["E", "M", "R"])
    node13 = Node("M", ["C", "G", "L"])
    node14 = Node("N", ["C", "F", "O"])
    node15 = Node("O", ["H", "N", "P"])
    node16 = Node("P", ["D", "J", "O"])
    node17 = Node("Q", ["D", "I", "R"])
    node18 = Node("R", ["K", "L", "Q"])

    second_blanusa_snark.add_node(node1)
    second_blanusa_snark.add_node(node2)
    second_blanusa_snark.add_node(node3)
    second_blanusa_snark.add_node(node4)
    second_blanusa_snark.add_node(node5)
    second_blanusa_snark.add_node(node6)
    second_blanusa_snark.add_node(node7)
    second_blanusa_snark.add_node(node8)
    second_blanusa_snark.add_node(node9)
    second_blanusa_snark.add_node(node10)
    second_blanusa_snark.add_node(node11)
    second_blanusa_snark.add_node(node12)
    second_blanusa_snark.add_node(node13)
    second_blanusa_snark.add_node(node14)
    second_blanusa_snark.add_node(node15)
    second_blanusa_snark.add_node(node16)
    second_blanusa_snark.add_node(node17)
    second_blanusa_snark.add_node(node18)

    return second_blanusa_snark

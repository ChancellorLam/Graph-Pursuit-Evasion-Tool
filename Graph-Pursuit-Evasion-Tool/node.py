class Node:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors

    def get_name(self):
        return self.name

    def get_neighbors(self):
        return self.neighbors

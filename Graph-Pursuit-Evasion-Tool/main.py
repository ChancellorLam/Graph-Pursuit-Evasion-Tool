from graph import create_franklin_graph

if __name__ == '__main__':
    franklin_graph = create_franklin_graph()
    print("How many nodes would you like to probe?")
    num_probes = int(input())

    probe_locations = []
    for i in range(0, num_probes):
        print("What node would you like to probe?")
        user_input = probe_locations.append(input().upper())
    for probe in probe_locations:
        distances = franklin_graph.get_distances_from_node(probe)
        print(distances)

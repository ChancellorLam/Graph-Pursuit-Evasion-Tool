from graph import create_franklin_graph

if __name__ == '__main__':
    franklin_graph = create_franklin_graph()
    print("How many nodes would you like to probe?")
    num_probes = int(input())

    probe_locations = []
    for i in range(0, num_probes):
        print("What node would you like to probe?")
        user_input = probe_locations.append(input().upper())
    location_list = []
    for each_probe in probe_locations:
        # print(distances)
        distances = franklin_graph.get_distances_from_node(each_probe)
        location_list.append(distances)

    result = {}
    for location in location_list:
        for key, value in location.items():
            if key not in result:
                result[key] = []
            result[key].append(value)

    for key, values in result.items():
        print(f"{key}: {values}")

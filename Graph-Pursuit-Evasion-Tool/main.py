from graph import (create_franklin_graph, create_loupekine_snark, create_double_star_snark, create_szekeres_snark,
                   create_second_blanusa_snark)

if __name__ == '__main__':
    franklin_graph = create_franklin_graph()
    loupekine_snark = create_loupekine_snark()
    double_star_snark = create_double_star_snark()
    szekeres_snark = create_szekeres_snark()
    second_blanusa_snark = create_second_blanusa_snark()

    print("Metric Dimension: " + str(second_blanusa_snark.get_metric_dimension()))

    # # generate every list of every combination
    # graph_names = []
    # for node in franklin_graph.nodes:
    #     graph_names.append(node.name)
    #
    # test = []
    # for i in range(1, len(graph_names) + 1):
    #     els = [list(x) for x in combinations(graph_names, i)]
    #     test.extend(els)
    # print(test)

    print("How many nodes would you like to probe?")
    num_probes = int(input())

    probe_locations = []
    for i in range(0, num_probes):
        print("What node would you like to probe?")
        user_input = probe_locations.append(input().upper())
    location_list = []
    for each_probe in probe_locations:
        # print(distances)
        distances = second_blanusa_snark.get_distances_from_node(each_probe)
        location_list.append(distances)

    result = {}
    for location in location_list:
        for key, value in location.items():
            if key not in result:
                result[key] = []
            result[key].append(value)

    for key, values in result.items():
        print(f"{key}: {values}")

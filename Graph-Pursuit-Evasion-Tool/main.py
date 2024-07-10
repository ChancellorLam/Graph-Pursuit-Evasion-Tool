from graph import (create_franklin_graph, create_first_loupekine_snark, create_double_star_snark, create_szekeres_snark,
                   create_second_blanusa_snark, create_second_loupekine_snark, create_goldberg_snark,
                   create_watkins_snark)

if __name__ == '__main__':
    while True:
        franklin_graph = create_franklin_graph()
        loupekine_snark = create_first_loupekine_snark()
        double_star_snark = create_double_star_snark()
        szekeres_snark = create_szekeres_snark()
        second_blanusa_snark = create_second_blanusa_snark()
        second_loupekine_snark = create_second_loupekine_snark()
        goldberg_snark = create_goldberg_snark()
        watkins_snark = create_watkins_snark()

        # print("Metric Dimension: " + str(szekeres_snark.get_metric_dimension()))

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
            distances = szekeres_snark.get_distances_from_node(each_probe)
            location_list.append(distances)

        result = {}
        for location in location_list:
            for key, value in location.items():
                if key not in result:
                    result[key] = []
                result[key].append(value)

        # Create a dictionary to count occurrences of each list of values
        occurrences = {}
        for values in result.values():
            values_tuple = tuple(values)  # Convert the list to a tuple for immutability
            if values_tuple not in occurrences:
                occurrences[values_tuple] = 0
            occurrences[values_tuple] += 1

        uniques = 0
        non_uniques = 0
        # print number of uniques and non-uniques as well as results with asterisks for unique values
        for key, values in result.items():
            values_tuple = tuple(values)
            if occurrences[values_tuple] > 1:
                print(f"{key}: {values}")
                non_uniques = non_uniques + 1
            else:
                print(f"{key}: {values}*")
                uniques = uniques + 1

        print("Uniques: " + str(uniques))
        print("Non-Uniques: " + str(non_uniques))

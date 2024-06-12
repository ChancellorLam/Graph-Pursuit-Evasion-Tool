from graph import create_franklin_graph
from graph import create_loupekine_snark
from graph import create_double_star_snark

if __name__ == '__main__':
    franklin_graph = create_franklin_graph()
    loupekine_snark = create_loupekine_snark()
    double_star_snark = create_double_star_snark()
    print("How many nodes would you like to probe?")
    num_probes = int(input())

    probe_locations = []
    for i in range(0, num_probes):
        print("What node would you like to probe?")
        user_input = probe_locations.append(input().upper())
    location_list = []
    for each_probe in probe_locations:
        # print(distances)
        distances = double_star_snark.get_distances_from_node(each_probe)
        location_list.append(distances)

    result = {}
    for location in location_list:
        for key, value in location.items():
            if key not in result:
                result[key] = []
            result[key].append(value)

    for key, values in result.items():
        print(f"{key}: {values}")

from graph import create_franklin_graph

if __name__ == '__main__':
    franklin_graph = create_franklin_graph()
    print("What node would you like to probe?")
    user_input = input().upper()
    distances = franklin_graph.get_distances_from_node(user_input)
    print(distances)

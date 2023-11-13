from graph_functions import *
import time

def greedy_max_clique(adjancency_matrix):
    # Initialize an empty set to represent the current clique
    current_clique = set()

    # Initialize a set to keep track of vertices that have been considered
    considered_vertices = set()

    operation_counter = 0
    attempts_counter = 0

    # Iterate through all vertices in the graph
    for vertex in range(len(adjancency_matrix)):

        operation_counter += 1
        attempts_counter += 1

        # If the vertex is not in the current clique and is adjacent to all vertices in the current clique
        if vertex not in current_clique and all(adjancency_matrix[vertex][v] for v in current_clique):
            # Add the vertex to the current clique
            current_clique.add(vertex)

            # Mark the vertex and its neighbors as considered
            considered_vertices.add(vertex)
            considered_vertices.update(neighbors(adjancency_matrix, vertex))

    return list(current_clique), operation_counter, attempts_counter

if __name__ == '__main__':

    graphs = load_graphs(150)

    edge_percentage_list = [0.125, 0.25, 0.5, 0.75]

    edge_percentage_list_index = 0

    file = open("results/greedy_search.txt", "w")
    file.write(f"{'Vertices':<15} {'Edge Percentage':<15} {'Edges':<15} {'Maximum Clique':<50} {'Maximum Clique Size':<30} {'Operations':<15} {'Attempts':<15} {'Time':<15}\n")

    file_csv = open("results/greedy_search.csv", "w")
    file_csv.write("Vertices;Edge_Percentage;Edges;Maximum_Clique;Maximum_Clique_Size;Operations;Attempts;Time\n")

    for graph in graphs:

        vertices = nx.nodes(graph)
        edges = len(graph.edges)

        adj_mat = get_adjacency_matrix(graph)

        start = time.time()
        maximum_clique, n_operations, n_attempts = greedy_max_clique(adj_mat)
        end = time.time()

        maximum_clique_string = "["

        for elem in maximum_clique:
            maximum_clique_string = maximum_clique_string + str(elem) + ","

        maximum_clique_string = maximum_clique_string[:-1] + "]"

        print(f"{len(graph.nodes):<15} {edge_percentage_list[edge_percentage_list_index]:<15} {len(graph.edges):<15} {maximum_clique_string:<50} {len(maximum_clique):<30} {n_operations:<15} {n_attempts:<15} {end - start:<15}\n")
        file.write(f"{len(graph.nodes):<15} {edge_percentage_list[edge_percentage_list_index]:<15} {len(graph.edges):<15} {maximum_clique_string:<50} {len(maximum_clique):<30} {n_operations:<15} {n_attempts:<15} {end - start:<15}\n")
        file_csv.write(f"{len(graph.nodes)};{edge_percentage_list[edge_percentage_list_index]};{len(graph.edges)};{maximum_clique_string};{len(maximum_clique)};{n_operations};{n_attempts};{end - start}\n")


        if edge_percentage_list_index == len(edge_percentage_list)-1:
            edge_percentage_list_index = 0
        else:
            edge_percentage_list_index += 1
from graph_functions import *
import networkx as nx
from itertools import combinations
import time

def find_maximum_clique(adjacency_matrix, vertices):
    n = len(adjacency_matrix)
    max_clique = []

    operation_counter = 0
    attempts_counter = 0

    for size in range(n, 0, -1):
        for combination in combinations(vertices, size):
            operation_counter += 1
            attempts_counter += 1
            if is_clique(adjacency_matrix, combination):
                max_clique = list(combination)
                return max_clique, operation_counter, attempts_counter

    return max_clique, operation_counter, attempts_counter

if __name__ == '__main__':

    graphs = load_graphs(30)

    edge_percentage_list = [0.125, 0.25, 0.5, 0.75]

    edge_percentage_list_index = 0

    file_txt = open("results/exhaustive_search.txt", "w")
    file_txt.write(f"{'Vertices':<15} {'Edge Percentage':<15} {'Edges':<15} {'Maximum Clique':<50} {'Maximum Clique Size':<30} {'Operations':<15} {'Attempts':<15} {'Time':<15}\n")

    file_csv = open("results/exhaustive_search.csv", "w")
    file_csv.write("Vertices;Edge_Percentage;Edges;Maximum_Clique;Maximum_Clique_Size;Operations;Attempts;Time\n")

    for graph in graphs:

        vertices = nx.nodes(graph)
        edges = len(graph.edges)

        adj_mat = get_adjacency_matrix(graph)

        start = time.time()
        maximum_clique, n_operations, n_attempts = find_maximum_clique(adj_mat, vertices)
        end = time.time()

        maximum_clique_string = "[" + ",".join(maximum_clique) + "]"

        print(f"{len(graph.nodes):<15} {edge_percentage_list[edge_percentage_list_index]:<15} {len(graph.edges):<15} {maximum_clique_string:<50} {len(maximum_clique):<30} {n_operations:<15} {n_attempts:<15} {end - start:<15}\n")
        file_txt.write(f"{len(graph.nodes):<15} {edge_percentage_list[edge_percentage_list_index]:<15} {len(graph.edges):<15} {maximum_clique_string:<50} {len(maximum_clique):<30} {n_operations:<15} {n_attempts:<15} {end - start:<15}\n")
        file_csv.write(f"{len(graph.nodes)};{edge_percentage_list[edge_percentage_list_index]};{len(graph.edges)};{maximum_clique_string};{len(maximum_clique)};{n_operations};{n_attempts};{end - start}\n")


        if edge_percentage_list_index == len(edge_percentage_list)-1:
            edge_percentage_list_index = 0
        else:
            edge_percentage_list_index += 1
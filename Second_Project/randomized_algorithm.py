import random
from graph_functions import *
import time

def randomized_clique_algorithm(graph, max_operations=5000):
    
    graph_size = graph.number_of_nodes()

    initial_size = graph_size // 2

    current_size = initial_size

    best_clique = []
    operation_counter = 0
    attempts_counter = 0

    tested_solutions = set()

    while operation_counter < max_operations:
        vertices = random.sample(sorted(graph.nodes()), current_size)

        solution = tuple(sorted(vertices))
        
        if solution in tested_solutions:
            continue
        
        tested_solutions.add(solution)

        attempts_counter += 1

        clique = local_search(graph.subgraph(vertices))

        operation_counter += current_size **2

        if len(clique) == graph_size:
            best_clique = clique
            break
        elif len(clique) > current_size / 2:
            current_size = min(len(graph.nodes()), current_size * 2)
        else:
            current_size = max(len(best_clique)+1, current_size // 2)

        best_clique = max(clique, best_clique, key=len)

    return best_clique, operation_counter, attempts_counter

def local_search(subgraph):
    clique = []
    for node in subgraph.nodes():
        if all(node in subgraph[clique] for clique in clique):
            clique.append(node)
    return clique

def run(graphs, file_path):

    max_number_of_operations_list = [1000,2500,5000,10000,20000,100000,500000,1000000,2500000,5000000]

    for max_number_of_operations in max_number_of_operations_list:

        edge_percentage_list = [0.125, 0.25, 0.5, 0.75]

        edge_percentage_list_index = 0

        file = open(file_path + str(max_number_of_operations) + ".txt", "w")
        file.write(f"{'Vertices':<15} {'Edge Percentage':<15} {'Edges':<15} {'Maximum Clique':<50} {'Maximum Clique Size':<30} {'Operations':<15} {'Attempts':<15} {'Time':<15}\n")

        file_csv = open(file_path + str(max_number_of_operations) + ".csv", "w")
        file_csv.write("Vertices;Edge_Percentage;Edges;Maximum_Clique;Maximum_Clique_Size;Operations;Attempts;Time\n")

        for graph in graphs:

            start = time.time()
            maximum_clique, n_operations, n_attempts = randomized_clique_algorithm(graph, max_number_of_operations)
            end = time.time()

            maximum_clique_string = "["

            for elem in maximum_clique:
                maximum_clique_string = maximum_clique_string + str(elem) + ","

            maximum_clique_string = maximum_clique_string[:-1] + "]"

            file.write(f"{graph.number_of_nodes():<15} {edge_percentage_list[edge_percentage_list_index]:<15} {len(graph.edges):<15} {maximum_clique_string:<50} {len(maximum_clique):<30} {n_operations:<15} {n_attempts:<15} {end - start:<15}\n")
            file_csv.write(f"{graph.number_of_nodes()};{edge_percentage_list[edge_percentage_list_index]};{len(graph.edges)};{maximum_clique_string};{len(maximum_clique)};{n_operations};{n_attempts};{end - start}\n")

            if edge_percentage_list_index == len(edge_percentage_list)-1:
                edge_percentage_list_index = 0
            else:
                edge_percentage_list_index += 1

if __name__ == "__main__":

    graphs = load_graphs(34)
    run(graphs, "results/randomized_algorithm_my_graphs")
    sw_graphs = load_SW_graphs()
    run(sw_graphs, "results/randomized_algorithm_SW_graphs")
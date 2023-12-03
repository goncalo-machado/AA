import csv

max_number_of_operations_list = [1000,2500,5000,10000,20000,100000,500000,1000000,2500000,5000000]

exhaustive_results = []
greedy_results = []
randomized_results = {}
correct_results = {}
algorithms_accuracy = {}

with open('results/exhaustive_search_my_graphs.csv', 'r') as exhaustive_search_csv:

    correct_results["exhaustive"] = 0

    lines = csv.reader(exhaustive_search_csv, delimiter=';')
    first_line = True
    for row in lines:
        if first_line:
            first_line = False
            continue
            
        exhaustive_results.append(int(row[4]))

with open('results/greedy_search_my_graphs.csv', 'r') as exhaustive_search_csv:

    correct_results["greedy"] = 0

    lines = csv.reader(exhaustive_search_csv, delimiter=';')
    first_line = True
    for row in lines:
        if first_line:
            first_line = False
            continue
        if int(row[0]) == 33 and float(row[1]) == 0.75:
            break
            
        greedy_results.append(int(row[4]))

for max_number_of_operations in max_number_of_operations_list:

    correct_results["randomized_" + str(max_number_of_operations)] = 0

    randomized_results[max_number_of_operations] = []

    with open('results/randomized_algorithm_my_graphs' + str(max_number_of_operations) +'.csv', 'r') as randomized_algorithm_csv:
        lines = csv.reader(randomized_algorithm_csv, delimiter=';')
        first_line = True
        for row in lines:
            if first_line:
                first_line = False
                continue
            if int(row[0]) == 33 and float(row[1]) == 0.75:
                break
                
            randomized_results[max_number_of_operations].append(int(row[4]))

for i in range(len(exhaustive_results)):
    
    correct_result = exhaustive_results[i]

    correct_results["exhaustive"] += 1

    if greedy_results[i] == correct_result:
        correct_results["greedy"] += 1

    for key in randomized_results.keys():
        if randomized_results[key][i] == correct_result:
            correct_results["randomized_" + str(key)] += 1

for key in correct_results.keys():
    algorithms_accuracy[key] = correct_results[key] / len(exhaustive_results)

file = open("results/result_comparison.txt", "w")
file.write(f"{'Algorithm':<30} {'Correct_Results':<15} {'Accuracy':<15}\n")

file_csv = open("results/result_comparison.csv", "w")
file_csv.write("Algorithm;Correct_Results;Accuracy\n")

for key in algorithms_accuracy.keys():
    file.write(f"{key:<30} {correct_results[key]:<15} {algorithms_accuracy[key]:<15}\n")
    file_csv.write(f"{key};{correct_results[key]};{algorithms_accuracy[key]}\n")
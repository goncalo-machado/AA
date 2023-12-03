import csv
import math

max_number_of_operations_list = [1000,2500,5000,10000,20000,100000,500000,1000000,2500000,5000000]

exhaustive_results = []
greedy_results = []
randomized_results = {}
correct_results = {}
algorithms_accuracy = {}

exhaustive_attempts = []
greedy_attempts = []
randomized_attempts = {}
algorithm_attemps_ratio = {}
algorithm_attemps_ratio_average = {}

with open('results/exhaustive_search_my_graphs.csv', 'r') as exhaustive_search_csv:

    correct_results["exhaustive"] = 0
    algorithm_attemps_ratio["exhaustive"] = 0

    lines = csv.reader(exhaustive_search_csv, delimiter=';')
    first_line = True
    for row in lines:
        if first_line:
            first_line = False
            continue
            
        exhaustive_results.append(int(row[4]))
        exhaustive_attempts.append(int(row[6]))

with open('results/greedy_search_my_graphs.csv', 'r') as exhaustive_search_csv:

    correct_results["greedy"] = 0
    algorithm_attemps_ratio["greedy"] = 0

    lines = csv.reader(exhaustive_search_csv, delimiter=';')
    first_line = True
    for row in lines:
        if first_line:
            first_line = False
            continue
        if int(row[0]) == 33 and float(row[1]) == 0.75:
            break
            
        greedy_results.append(int(row[4]))
        greedy_attempts.append(int(row[6]))

for max_number_of_operations in max_number_of_operations_list:

    correct_results["randomized_" + str(max_number_of_operations)] = 0
    algorithm_attemps_ratio["randomized_" + str(max_number_of_operations)] = 0

    randomized_results[max_number_of_operations] = []
    randomized_attempts[max_number_of_operations] = []

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
            randomized_attempts[max_number_of_operations].append(int(row[6]))

for i in range(len(exhaustive_results)):
    
    correct_result = exhaustive_results[i]

    correct_results["exhaustive"] += 1

    if greedy_results[i] == correct_result:
        correct_results["greedy"] += 1

    for key in randomized_results.keys():
        if randomized_results[key][i] == correct_result:
            correct_results["randomized_" + str(key)] += 1

    attempts_exhaustive = exhaustive_attempts[i]

    algorithm_attemps_ratio["exhaustive"] += attempts_exhaustive / attempts_exhaustive
    
    algorithm_attemps_ratio["greedy"] +=  greedy_attempts[i] / attempts_exhaustive

    for key in randomized_attempts.keys():
        algorithm_attemps_ratio["randomized_" + str(key)] += randomized_attempts[key][i] / attempts_exhaustive

for key in correct_results.keys():
    algorithms_accuracy[key] = round(correct_results[key] / len(exhaustive_results), 2)
    algorithm_attemps_ratio_average[key] = round(algorithm_attemps_ratio[key] / len(exhaustive_results),2)

file = open("results/result_comparison.txt", "w")
file.write(f"{'Algorithm':<30} {'Correct_Results':<15} {'Accuracy':<15} {'Attempts_Ratio_Average':<15}\n")

file_csv = open("results/result_comparison.csv", "w")
file_csv.write("Algorithm;Correct_Results;Accuracy;Attempts_Ratio_Average\n")

for key in algorithms_accuracy.keys():
    file.write(f"{key:<30} {correct_results[key]:<15} {algorithms_accuracy[key]:<15} {algorithm_attemps_ratio_average[key]:<15}\n")
    file_csv.write(f"{key};{correct_results[key]};{algorithms_accuracy[key]};{algorithm_attemps_ratio_average[key]}\n")
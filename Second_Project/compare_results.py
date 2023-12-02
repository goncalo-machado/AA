import csv

exhaustive_results = []
randomized_results = []

with open('results/randomized_algorithm_my_graphs.csv', 'r') as randomized_algorithm_csv:
    lines = csv.reader(randomized_algorithm_csv, delimiter=';')
    first_line = True
    for row in lines:
        if first_line:
            first_line = False
            continue
            
        randomized_results.append(int(row[4]))

with open('results/exhaustive_search.csv', 'r') as exhaustive_search_csv:
    lines = csv.reader(exhaustive_search_csv, delimiter=';')
    first_line = True
    for row in lines:
        if first_line:
            first_line = False
            continue
            
        exhaustive_results.append(int(row[4]))

index = 0

correct_results = 0

for elem in exhaustive_results:
    print(str(elem) + " " + str(randomized_results[index]))

    if elem == randomized_results[index]:
        correct_results +=1
    index += 1

accuracy = correct_results / len(exhaustive_results)

print(accuracy)

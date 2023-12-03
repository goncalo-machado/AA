import matplotlib.pyplot as plt
import numpy as np
import csv

max_number_of_operations_list = [1000,2500,5000,10000,20000,100000,500000,1000000,2500000,5000000]
#max_number_of_operations_list = [5000000]


x = {}
y = {}

for max_number_of_operations in max_number_of_operations_list:

    x[max_number_of_operations] = []
    y[max_number_of_operations] = []

    with open('results/randomized_algorithm_my_graphs' + str(max_number_of_operations) +'.csv', 'r') as randomized_algorithm_csv:
        lines = csv.reader(randomized_algorithm_csv, delimiter=';')
        first_line = True
        for row in lines:
            if first_line:
                first_line = False
                continue
            if int(row[0]) == 33 and float(row[1]) == 0.75:
                break

            if float(row[1]) != 0.125:
                continue
                
            x[max_number_of_operations].append(int(row[0]))
            y[max_number_of_operations].append(int(row[5]))

for key in x.keys():
    plt.plot(x[key], y[key], linestyle ='dashed', marker = 'o', label = "Max " + str(key))

plt.xticks(rotation = 25)
#plt.ylim([0,0.2])
plt.xlabel('Vertices') 
plt.ylabel('Operations') 
plt.title('Number of Operations', fontsize = 20) 

plt.grid() 
plt.legend()
plt.show()
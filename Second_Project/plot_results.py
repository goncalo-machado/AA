import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

with open('results/result_comparison.csv', 'r') as greedy_search_csv:
    lines = csv.reader(greedy_search_csv, delimiter=';')
    first_line = True
    index = 0
    for row in lines:
        if first_line:
            first_line = False
            continue
            
        print(row)
        x.append(int(row[0]))
        y.append(float(row[5]))
        index += 1

plt.plot(x,y, color = 'r', linestyle ='dashed', marker = 'o', label = "Operations")
plt.xticks(rotation = 25)
#plt.ylim([0,0.2])
plt.xlabel('Vertices') 
plt.ylabel('Operations') 
plt.title('Number of Operations', fontsize = 20) 

plt.grid() 
plt.legend()
plt.show()
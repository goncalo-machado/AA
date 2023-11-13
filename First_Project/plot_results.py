import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('results/greedy_search.csv', 'r') as greedy_search_csv:
    lines = csv.reader(greedy_search_csv, delimiter=';')
    first_line = True
    for row in lines:
        if first_line:
            first_line = False
            continue
            
        print(row)
        x.append(int(row[0]))
        y.append(float(row[7]))

plt.plot(x,y, color = 'r', linestyle ='dashed', marker = 'o', label = "Test")

plt.xticks(rotation = 25)
plt.xlabel('Vertices') 
plt.ylabel('Operations') 
plt.title('Test', fontsize = 20) 
plt.grid() 
plt.legend() 
plt.show()
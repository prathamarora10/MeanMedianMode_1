import csv

with open('/Users/prathamarora/Downloads/Python_Projects/MeanMedianMode.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
total = 0

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(n_num)
    total += i

length_of_new_data = len(new_data)

print(f'Mean : {total / length_of_new_data}')

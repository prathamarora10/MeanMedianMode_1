import csv

with open('/Users/prathamarora/Downloads/Python_Projects/MeanMedianMode.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(n_num)

new_data.sort()

length = len(new_data)

if length % 2 == 0:
    m1 = float(new_data[length // 2])
    m2 = float(new_data[length // 2 - 1])
    median = ( m1 + m2 ) / 2
else:
    median = float(new_data[length // 2])

print(f'Median : {median}')
import csv
from collections import Counter

with open('/Users/prathamarora/Downloads/Python_Projects/MeanMedianMode.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(n_num)

data = Counter(new_data)
data_range = {'100-125':0, '125-150':0}

for weight, occurence in data.items():
    if(100 < float(weight) < 125):
        data_range['100-125'] += occurence
    elif(125 < float(weight) < 150):
        data_range['125-150'] += occurence

mode_range, mode_occurence = 0, 0

for range, occurence in data_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split('-')[0]), int(range.split('-')[1])], occurence

mode = float(mode_range[0] + mode_range[1]) / 2

print(f'Mode : {mode}')

import numpy
import sklearn
import csv
with open ('train_users_2.csv', 'rb') as file:
    reader = csv.reader(file, delimiter = ',')
    info_list = []
    print ("adding lists")
    for row in reader:
        info_list.append(row)
# print(info_list[1])

info_list = info_list[1:]
for i in info_list:
    if i[4] == '-unknown-':
        i[4] = 0
    elif i[4] == 'MALE':
        i[4] = 1
    else:
        i[4] = -1

print(info_list[1])
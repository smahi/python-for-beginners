import csv

with open('users_data.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)
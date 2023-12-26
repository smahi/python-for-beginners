import csv

# you can download the sample csv file in Linux OS using the following command
# wget https://github.com/smahi/python-for-beginners/raw/main/users_data.csv

with open('users_data.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)
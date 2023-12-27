import csv

# this is how we import a class from a library
from faker import Faker

# make an instance of the class Faker
fake = Faker()


lines = 0

# To generate a random data using https://www.mockaroo.com/
# you can download the sample csv file in Linux OS using the following command
# wget https://github.com/smahi/python-for-beginners/raw/main/users_data.csv

with open('users_data.csv') as f:
    reader = csv.reader(f, delimiter=',')
    lines = len(list(reader))
    for row in reader:
        # to print the whole row data
        # print(row)
        
        # to print the email only
        print(row[3])
        

# Write to csv file
# you need to install faker library using: pip install Faker
with open('users_data.csv', '+a') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow([lines, fake.first_name(), fake.last_name(), fake.email(), fake.gender(), fake.ipv4()])
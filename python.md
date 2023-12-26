# Python notes

```python
print("Hello")
```

```python
a = 5
b = 7
sum = a + b 

print(f"The sum of {a} and {b} is equal to {sum}")
```

```python
# (input) function allow reading data from the console
# (int) convert string to integer

a = int(input('Enter A value: '))
b = int(input('Enter B value: '))

sum = a + b 

print(f"The sum of {a} and {b} is equal to {sum}")
```

## String manipulations 

```python 
message = "Hello World!"

# formatting with `f`
# print(f"{message}")

# slicing 
print(message[2])
print(message[-3])
print(message[1:7])

print(message.upper())
print(message.lower())
print(message.title())

print(message.find('Wo')) # return the index, if not found it returns -1

print(message.replace('W', 'X')) # replace W with X

contains = 'World' in message
print(contains)
```

## Arithmetics

```python
# Addition
a = 5
b = 7
sum = a + b 

print(f'{a} + {b} = {sum}')


# Product
a = 5
b = 7
prod = a * b 

print(f'{a} * {b} = {prod}')

# Division
a = 15
b = 4
div = a / b 

print(f'{a} / {b} = {div}')

# Division (INT)
a = 15
b = 4
div = a // b # // returns an integer as a result

print(f'{a} // {b} = {div}')

# Division (REMAINDER)
a = 15
b = 4
div = a % b # % returns the remainder of the division

print(f'{a} % {b} = {div}')

```

## `if` statement

```python
# temperature
temp = int(input('Type the temperature: '))

if temp <= 24:
    print('cold day!')
else:
    print('hot day!')
```

```python 
# Notes

note = float(input('Type your note: '))

if note >= 10:
    print("Admis")
elif note < 10 and note >= 5:
    print("Ratrapage")
else:
    print("Ajournee")


# true or false

if not False:
    print('Hi!!!')
```

## `while` Loops

```python

x = 10

while x <= 10 and x > -1:
    print(x)
    x = x - 1
```

## `for` statement

```python
# range(1, 5) will produce a list [1, 2, 3, 4]
for x in range(1, 5):
    print(x)
```

## Lists

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[1])
print(numbers[-1])
print(numbers[2:4])

numbers.append(6) # adds 6 to the end 
numbers.insert(0, 6) # insert 6 at position 0
numbers.remove(6) # removes 6, this will remove an item
numbers.pop() # remove the last item
numbers.clear() # removes all items
numbers.index(3) # returns the first occurrence of 3
numbers.sort()
numbers.reverse()
x = numbers.copy() # returns a copy of the list

```

## Tuples

```python
# Tuples
coordinates = (1, 2, 3)

print(coordinates)

# unpack tuple
x, y, z = coordinates # variable will be assigned a value from the tuple
```

## Dictionaries

```python
# Dictionaries

customer = {
    'name': 'John Doe',
    'age': 45,
    'is_verified': True
}

print(customer)

print(customer['name'])
print(customer['age'])
print(customer['is_verified'])

customer['phone'] = '0660000000' # this will add an new entry to the dictionary

print(customer)

customer.get('blablah', 'the_default_value') # if the key does not exist then the default value is returned

# if the key does not exist it will throw an exception
# customer('key')
```

## Functions

```python
# Function without params
def add():
    # some codes....
    return 5+7

print(add())

# Function with params
def prod(x, y):
    result = x * y
    return result

print(prod(3, 5))

# Function without return
def greet(name):
    print(f'Hello, {name}')
    
greet('Mohammed')

def fullname(firstname, lastname):
    return f'{lastname} {firstname}'


print(fullname('John', 'Doe'))
```

## Working with files

```python
# Read only the file content
with open('names.txt', 'r') as f:
    print(f.readlines())
    
# Write to the file
with open('names.txt', 'w') as f:
    f.write('Meriam')
    
# Append 'a', and allow to read & write '+'
with open('names.txt', '+a') as f:
    f.write('Ahmed')
    f.seek(0) # move the cursor to the binning of the file
    print(f.readlines())
```


**NB**:

[https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)


## Working with Directories

```python
# To create a directory
import os


if not os.path.exists('test_dir'):
    os.mkdir('test_dir')


# list directory content
print(os.listdir('.'))
print(os.listdir('/home/smahi/Music'))
```

## Working with CSV files

```python
import csv

# you can download the sample csv file in Linux OS using the following command
# wget https://github.com/smahi/python-for-beginners/raw/main/users_data.csv

with open('users_data.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        # to print the whole row data
        # print(row)
        
        # to print the email only
        print(row[3])
```
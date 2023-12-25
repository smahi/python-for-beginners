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
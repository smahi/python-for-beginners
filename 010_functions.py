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
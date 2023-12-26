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
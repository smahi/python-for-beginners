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
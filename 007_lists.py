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

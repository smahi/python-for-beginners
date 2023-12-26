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
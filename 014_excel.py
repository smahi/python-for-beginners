from openpyxl import  load_workbook

# Read from Excel file 
wb = load_workbook(filename='users_data.xlsx')
ws = wb.active

print(ws['D7'].value)

# Extract all IP addresses
ip_column = ws['F']

for cell in ip_column[1:4]:
    print(cell.value)
    
# Extract by row
for row in ws.values:
    if row[4] == 'Male':
        print(row)
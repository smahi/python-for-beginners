from openpyxl import Workbook, load_workbook

# make an instance of Workbook class
wb = Workbook()

# Get the active worksheet
ws = wb.active

# Show sheet names
print(wb.get_sheet_names())

# Read from Excel file 
wb = load_workbook(filename='students.xls')
ws = wb.active

print(ws['D7'].value)
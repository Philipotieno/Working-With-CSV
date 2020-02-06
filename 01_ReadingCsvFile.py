#  Import a csv module
import csv

# csv filename
filename = "aapl.csv"

# initialize the tiltle and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as f:
    
    # creating a csv reader object
    reader = csv.reader(f)
    
    # Extracting field name through first row
    fields = next(reader)
    
    # Extracting each data row one by one
    for row in reader:
        rows.append(row)
    
    # Print total number of rows  
    print("Total row :%d"%(reader.line_num))

# Print the fields names
print("Field names are:" + ", ".join(field for field in fields))

# Print first five rows
print('\nFirst 5 rows are:\n')
for row in rows[:1]:
    # parsing each column of a row
    for col in rows[3:5]:
        print("%10s"%col),
    print('\n')
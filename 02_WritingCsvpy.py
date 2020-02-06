# Writing to a CSV file

# Import the csv module
import csv

# Field names
fileds = ['Name', 'Branch', 'Year', 'CGPA']

# Data rows of csv file
rows = [
    ['Philip', 'COE', '2002', '9.0'],
    ['Mitchell', 'COE', '2002', '9.2'],
    ['Otieno', 'IT', '2002', '9.3'],
    ['kimberly', 'SE', '2002', '9.6'],
    ['Wexler', 'MCE', '2002', '4.0'],
    ['Trevor', 'EP', '2002', '9.1']
]

# Give the csv file a name
filename = "student_records.csv"

# writing toa csv file
with open(filename, 'w') as w:
    # creating a csv writer object
    writer = csv.writer(w)
    
    # writing the feilds
    writer.writerow(fileds)
    
    # writing the data rows
    writer.writerows(rows)
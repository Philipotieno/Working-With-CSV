# Writing a dictionary to a csv file
# Import the csv module

import csv

# My data rows as dictioanry objects
mydict = [
    {'Branch': 'COE', 'CGPA': '9.5', 'Name': 'Philip', 'Year': '2020'},
    {'Branch': 'SPAS', 'CGPA': '9.0', 'Name': 'Otieno', 'Year': '2019'},
    {'Branch': 'COE', 'CGPA': '7.0', 'Name': 'Mitchell', 'Year': '2050'},
    {'Branch': 'IT', 'CGPA': '9.0', 'Name': 'Kimberly', 'Year': '2020'},
    {'Branch': 'RE', 'CGPA': '4.0', 'Name': 'Trevor', 'Year': '2020'},
    {'Branch': 'ET', 'CGPA': '9.0', 'Name': 'Big Boy', 'Year': '2020'},
    {'Branch': 'TY', 'CGPA': '9.3', 'Name': 'Rody', 'Year': '2020'}
]

# Field Names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# Name of csv file
filename = "01_studentrecords.csv"

# Writing to CSV file
with open(filename, 'w') as w:
    # creating a csv dict writer object
    writer = csv.DictWriter(w, fieldnames=fields)
    
    # writing headers (field Names)
    writer.writeheader()
    
    # writing data rows
    writer.writerows(mydict)
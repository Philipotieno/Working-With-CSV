import csv
import json

csvfile = 'SalesInvoiceTemplate.csv'
jsonfile = 'SalesInvoiceTemplate.json'

data = {}
with open(csvfile) as f:
    reader = csv.DictReader(f)
    for rows in reader:
        ContactName = rows['*ContactName']
        data[ContactName] = rows

with open(jsonfile, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
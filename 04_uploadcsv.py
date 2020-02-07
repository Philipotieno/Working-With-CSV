import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "mitch",
                            host = "localhost",
                            port = "5432",
                            database = "invoice",
                            password = "mufasa2019")
    
    cursor = connection.cursor()
    create_table = '''CREATE TABLE IF NOT EXISTS invoices(
                        id SERIAL PRIMARY KEY,
                        ContactName VARCHAR NOT NULL,
                        InvoiceNumber INT NOT NULL,
                        InvoiceDate TIMESTAMP,
                        DueDate TIMESTAMP,
                        Description VARCHAR NOT NULL,
                        Quantity INT NOT NULL,
                        UnitAmount INT NOT NULL
                    );'''
    cursor.execute(create_table)
    connection.commit()
    print("Table created successfully")
    
    csv_file_path = 'SalesInvoiceTemplate.csv'
    with open(csv_file_path, 'r') as f:
        cmd = 'COPY invoices(ContactName, InvoiceNumber, InvoiceDate, DueDate, Description, Quantity, UnitAmount) FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'
        cursor.copy_expert(cmd, f)
        connection.commit()
    
except (Exception,psycopg2.DatabaseError) as error:
    print("Error", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("connection closed")

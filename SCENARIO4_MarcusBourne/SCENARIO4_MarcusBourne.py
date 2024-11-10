import sqlite3
import csv

connection = sqlite3.connect("customers.sqlite")
cur = connection.cursor()

delete_query = """DELETE FROM Customer;"""
cur.execute(delete_query)

create_table_query = """
    CREATE TABLE Customer (
        customerID INTEGER PRIMARY KEY, 
        firstName TEXT, 
        lastName TEXT,     
        companyName TEXT, 
        address TEXT, 
        city TEXT, 
        state TEXT,
        zip TEXT
    );
"""

filename = "customers.csv"
delimiter = ","
customer_id = 0

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
      data = ', '.join(["?" for _ in row])

      insert_query = "INSERT INTO Customer VALUES (NULL, " + data + ");"
      cur.execute(insert_query, row)

select_query = "SELECT * FROM Customer"
cur.execute(select_query)
data = cur.fetchall()

for row in data:
    print(row)
connection.close()
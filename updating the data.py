import csv
import psycopg2

# Define the CSV file name and field names
filename = 'output.csv'
fields = ['ID', 'Product Name', 'Quantity','Price']

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="::1",
    database="Eden_capital",
    user="postgres",
    password="eden245"
)

# Open the CSV file in append mode
with open(filename, 'a', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Ask the user to enter a new row of data
    name = input("Enter name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")

    # Write the new row of data to the CSV file
    writer.writerow([name, age, city])

    # Insert the new row of data into the SQL table
    cursor = conn.cursor()
    cursor.execute("INSERT INTO my_table (Name, Age, City) VALUES (%s, %s, %s)", (name, age, city))
    conn.commit()

import psycopg2
import matplotlib.pyplot as plt

# Establish connection to PostgreSQL database
conn = psycopg2.connect(
    host="::1",
    database="Eden_capital",
    user="postgres",
    password="eden245"
)

# Fetch data from database using SQL query
cur = conn.cursor()
cur.execute("SELECT product_name, total_price FROM  products_cap")
data = cur.fetchall()

# Extract product names and total prices from data
product_names = [row[0] for row in data]
total_prices = [row[1] for row in data]

# Plot the data as a bar graph
plt.bar(product_names, total_prices)
plt.xlabel("Product Name")
plt.ylabel("Total Price")
plt.title("Total Price of Products")

# Set the y-axis limits to reduce the scale
plt.ylim(0, 300)       # i did this in order to get a scale for the total prices of other products.
# because if we will take a bigger y lim we will less likely to see the impotance of the other products to the
# income of the company
# Set the positions and labels of the ticks on the x-axis
plt.xticks(rotation=45)

plt.show()

# Close the database connection
cur.close()
conn.close()
import psycopg2 #this way we can communicate between the postgres and pycharm
import pandas as pd

#this the cerditinals of the my server in sql
conn = psycopg2.connect(
    host="::1",
    database="Eden_capital",
    user="postgres",
    password="eden245"
)
#the reading of the table and using him
cursor = conn.cursor()
cursor.execute("SELECT * FROM products_cap")
#the table !
rows = cursor.fetchall()
print(rows)


data = rows
df = pd.DataFrame(data, columns=['Order_Id','ID', 'Product Name', 'Quantity', 'Price', 'Total'])
df.to_excel('data_project.xlsx', index=False)

df_1 = pd.read_excel('data_project.xlsx')
df_1.to_csv('output.csv', index=False)
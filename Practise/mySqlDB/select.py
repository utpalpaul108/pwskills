import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="root",
  password="password",
  database="ecommerce"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM ecommerce.customers"

mycursor.execute(sql)

customer = mycursor.fetchone()

print(customer)

customers = mycursor.fetchall()

for customer in customers:
   print(customer)

mydb.close()


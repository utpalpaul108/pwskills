import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="root",
  password="password",
  database="ecommerce"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE if not exists ecommerce")

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
   #print(x)
   
mycursor.execute("CREATE TABLE if not exists ecommerce.customers (name VARCHAR(255), email VARCHAR(255), phone_no VARCHAR(255), address VARCHAR(255))")
mycursor.execute("CREATE TABLE if not exists ecommerce.products (name VARCHAR(250), unit VARCHAR(50), price FLOAT, SKU INT)")

mydb.close()


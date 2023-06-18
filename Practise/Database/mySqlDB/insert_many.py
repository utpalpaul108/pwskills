import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="root",
  password="password",
  database="ecommerce"
)

mycursor = mydb.cursor()

sql = "INSERT INTO ecommerce.customers (name, email, phone_no, address) VALUES (%s, %s, %s, %s)"
val = [
	("Rajesh", "rajesh@yahoo.com", "94939", "Dhaka"),
	("Hasan", "hasan@gmail.com", "32434", "Rajshi"),
	("Rakib", "rakib@hotmail.com", "30430", "Khulna")
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, " Was Inserted")

mydb.close()


import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="root",
  password="password",
  database="ecommerce"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO ecommerce.customers (name, email, phone_no, address) VALUES ('Utpal Paul', 'utpalpaul108@gamil.com', '02333', 'Bagerhat')")

mydb.commit()

mydb.close()


import mysql.connector

veritab = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

print(veritab)

mycursor = veritab.cursor()

mycursor.execute("CREATE DATABASE sirket2")

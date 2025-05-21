import mysql.connector

veritab = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

print(veritab)

mycursor = veritab.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

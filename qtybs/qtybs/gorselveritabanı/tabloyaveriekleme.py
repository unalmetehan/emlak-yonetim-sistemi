import mysql.connector

veritab = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="sirket2"
)
#  "INSERT INTO" komutu ile kayıt ekleriz.

mycursor = veritab.cursor()

sorgu = "INSERT INTO musteri (isim, adres) VALUES (%s, %s)"
deger = ("Muhammet", "KTUUZEM NO:304")
mycursor.execute(sorgu, deger)

veritab.commit()

print(mycursor.rowcount, "kayıt eklendi.")

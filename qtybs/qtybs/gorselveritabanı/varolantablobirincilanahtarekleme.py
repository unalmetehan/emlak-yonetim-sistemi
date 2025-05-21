import mysql.connector

veritab = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="sirket2"
)
# Tablo zaten varsa, ALTER TABLE anahtar sözcüğünü kullanarak PRIMARY KEY ekleyebiliriz
print(veritab)

mycursor = veritab.cursor()

mycursor.execute("ALTER TABLE musteri ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

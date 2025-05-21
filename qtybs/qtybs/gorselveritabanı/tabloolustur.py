import mysql.connector

veritab = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="sirket2"
)
# bu sefer şirket isimli belirli bir veri tabanına ulaşıp, o veri tabanına tablo ekleyecez

print(veritab)

mycursor = veritab.cursor()

mycursor.execute("CREATE TABLE musteri (isim VARCHAR(255), adres VARCHAR(255))")

# mycursor.execute komutundan sonra tüm mysql komutları kullanılabilir.

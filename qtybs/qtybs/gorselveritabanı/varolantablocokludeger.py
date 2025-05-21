import mysql.connector

veritab = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="sirket2"
)
#  "INSERT INTO" komutu ile kayıt ekleriz.Çoklu kayıt için verilerimizi bir liste içine ekleriz.

mycursor = veritab.cursor()

sorgu = "INSERT INTO musteri (isim, adres) VALUES (%s, %s)"

deger = [
  ('Ekrem', 'ANKARA 4'),
  ('Hasan', 'BÜYÜK CADDE  652'),
  ('Ali', 'İSTANBUL 21'),
  ('Ayşe', 'ADANA 345'),
  ('Mustafa', 'BODRUM blvd 2'),
  ('Elif', 'KARADENİZ TEKNİK ÜNİ 1'),
  ('Fatma', 'GELİŞİM SOKAK 331')
]

mycursor.executemany(sorgu, deger)

veritab.commit()

print(mycursor.rowcount, "kayıt eklendi.")

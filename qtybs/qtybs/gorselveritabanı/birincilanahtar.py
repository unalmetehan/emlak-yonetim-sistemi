import mysql.connector

veritab = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="sirket2"
)
# Tablo oluştururken, her kayıt için birincil anahtar içeren bir sütun da oluşturmanız gerekir.
# Bu bir PRIMARY KEY tanımlayarak yapılabilir.
print(veritab)

mycursor = veritab.cursor()

mycursor.execute("CREATE TABLE calisan (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

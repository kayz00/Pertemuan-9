import mysql.connector

db = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = '',
    database = 'pertemuan9'
)


cursor = db.cursor()
query = "INSERT INTO biodata(nama, alamat, keterangan) VALUES(%s, %s, %s)"
data = ("budi", "Yogya", "Teman")
data = ("Asep", "Bandung", "Teman")
cursor.execute(query, data)

db.commit()
print("Data berhasil di insert")
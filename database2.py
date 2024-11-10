import mysql.connector

db = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = '',
    database = 'pertemuan9'
)


cursor = db.cursor()
cursor.execute(
    """
    CREATE TABLE Biodata(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    alamat VARCHAR(100) NOT NULL,
    keterangan VARCHAR(100) NOT NULL
    )
    """
)

print("Table berhasil dibuat")
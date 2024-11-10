import mysql.connector

db = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = '',
    database = 'pertemuan9'
)

# cara membuat database
#cursor = db.cursor()
#cursor.execute("CREATE DATABASE pertemuan9")

#print("database berhasil dibuat")

if db.is_connected():
   print("berhasil")





# Melihat semua daftar database
# Membuat database
# Delete database

# Melihat semua daftar table 
# Membuat table
# Melihat Information kolom
# Delete Table

# Melihat semua data dalam table
# Menambah / insert data dalam table
# Update data dalam table
# Delete data dalam table


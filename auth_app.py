import bcrypt
import sqlite3

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()


nombre = "ian"
password = "clave123".encode('utf-8')


hashed = bcrypt.hashpw(password, bcrypt.gensalt())
cursor.execute("INSERT INTO usuarios (nombre, password) VALUES (?, ?)", (nombre, hashed))
conn.commit()
conn.close()


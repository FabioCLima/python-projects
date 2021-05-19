import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

''' cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')') '''

cursor.execute("INSERT INTO clientes (nome, peso) VALUES (?, ?)", ('Fabiana', 58.4))
cursor.execute("INSERT INTO clientes (nome, peso) VALUES (?, ?)", ('Lucas', 70.5))
connection.commit()

cursor.execute("SELECT * FROM clientes")
for linha in cursor.fetchall():
    identificador, nome, peso = linha
    print(identificador, nome, peso)

cursor.close()
connection.close()

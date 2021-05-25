''' Elabore um script que crie um banco de dados denominado
estoque.db, usando SQLite3. A tabela ESTOQUE criada deve
armazenar as seguintes informações: nome, preço e
quantidade. '''

import sqlite3

# Criando o banco de dados--> estoque.db
connection = sqlite3.connect('estoque.db')
cursor = connection.cursor()

# Criando a tabela ESTOQUE

cursor.execute("""CREATE TABLE IF NOT EXISTS ESTOQUE(
    id integer PRIMARY KEY,
    nome text UNIQUE,
    preço real NOT NULL,
    quantidade INTEGER NOT NULL
    ); """)

estoque_lista = [('1', 'Cerveja Stella Artois', '3.25', '24 caixas'), 
                 ('2', 'Cerveja Bohemia', '2.25', '50 caixas'),
                 ('3', 'Cerveja Original', '3.75', '38 caixas')]

cursor.executemany('''INSERT INTO ESTOQUE(id, nome, preço, quantidade)
                   VALUES(?, ?, ?, ?)''', estoque_lista)
print("Criação e inserção de dados feitos com sucesso!")

connection.commit()
connection.close()

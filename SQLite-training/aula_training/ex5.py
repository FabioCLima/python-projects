import sqlite3

# banco de dados -> dados_alunos.db
# tabela -> alunos

connection = sqlite3.connect('dados_alunos.db')
cursor = connection.cursor()

sql = """
CREATE TABLE IF NOT EXISTS alunos(
    id integer PRIMARY KEY,
    nome text NOT NULL,
    idade integer NOT NULL,
    telefone text ,
    profissão text);
"""
cursor.execute(sql)
dados = [('1', 'Yun', 29, '+00000000', 'Músico'),
         ('2', 'Chan', 37, '+00000000', 'Engenheiro Elétrico'),
         ('3', 'Ayumi', 41, '+00000000', 'Programador'),
         ('4', 'Hinata', 25, '+00000000', 'Professor')]

cursor.executemany(""" INSERT INTO alunos(id, nome, idade, telefone, profissão)
            VALUES(?, ?, ?, ?, ?)""", dados)

query = ('SELECT * FROM alunos')
cursor.execute(query)
results = cursor.fetchall()
for aluno in results:
    print(f"Aluno:{aluno[1]}-\7*t idade:{aluno[2]}, profissão:{aluno[4]}")

connection.commit()
connection.close()

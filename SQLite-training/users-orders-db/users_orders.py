import sqlite3

connection = sqlite3.connect('orders.db')

# a cursor object allows us to execute SQL queries against a database.
cursor = connection.cursor()

# Criando a tabela users
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
connection.commit()

# Criando a tabela  orders
cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
""")
connection.commit()

# adicionando dados na base criada nos passos anteriores
cursor.execute("""INSERT INTO users(userid, fname,lname, gender) 
   VALUES('00001', 'Nik', 'Piepenbreier', 'male');""")
connection.commit()

user = ('00002', 'Lois', 'Lane', 'Female')
cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
connection.commit()

more_users = [('00003', 'Peter', 'Parker', 'Male'), ('00004', 'Bruce','Wayne',\
             'male')]
cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
connection.commit()

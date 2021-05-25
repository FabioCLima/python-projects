import sqlite3

db = sqlite3.connect("books.db")
cursor = db.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS books(
    id integer PRIMARY KEY,
    title text NOT NULL,
    author text NOT NULL,
    price real);''')


cursor.execute(''' INSERT INTO books(id, title, author, price)
         VALUES('1', 'Untold Stories', 'Alan Bennett', '17.49')''')

books_list = [('2', 'Machine Learning Hands On', 'Aurélien Géron', '37.48'),
              ('3', 'R Cookbook', 'Long & Teetor', '57.32'),
              ('4', 'Python for Data Analysis', 'McKinney', '22.34'),
              ('5', 'Machine Learning with R', 'Brett Lantz', '42.33')
              ]
cursor.executemany(''' INSERT INTO books(id, title, author, price)
                    VALUES(?, ?, ?, ?) ''', books_list)

cursor.execute('SELECT * FROM books')
print(cursor.fetchall())

db.commit()
db.close()

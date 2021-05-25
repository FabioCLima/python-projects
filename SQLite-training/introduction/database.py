import sqlite3

conn = sqlite3.connect('customer.db')  # create customer.db

# Create a cursor
cursor = conn.cursor()

# Create a Table
cursor.execute("""
               CREATE TABLE IF NOT EXISTS customers(
            id integer PRIMARY KEY,
            first_name text NOT NULL,
            last_name text NOT NULL,
            email text NOT NULL)""")

# Insert one information on the table
cursor.execute("""
    INSERT INTO customers(id,first_name, last_name, email)
    VALUES(?, ?, ?, ?)""", ('1', 'Fabio', 'Lima', 'fabio_lima07@yahoo.com.br'))

# Insert many information on the table
customers_list = [('2', 'Fernanda', 'Santos', 'fernanda_santos37@gmail.com'),
                  ('3', 'Fabiana', 'Oliveira', 'fabi_oliveira@yahoo.com.br'),
                  ('4', 'Blenda', 'Saraiva', 'blenda_saraiva@yahoo.com.br')]

cursor.executemany("""
    INSERT INTO customers(id, first_name, last_name, email)
    VALUES(?, ?, ?, ?)""", customers_list)


# Update Records
cursor.execute(""" UPDATE customers SET last_name = 'Carvalho'
               WHERE rowid = '3'""")

# Query The Database
cursor.execute(""" SELECT * FROM customers """)
# cursor.fetchone() - take the first register from the query
# cursor.fetchmany(3) - take 3 register from  the query
# items = list of tuples
items = cursor.fetchall()  # show all the data from the query
for customer in items:
    print(f'{customer[0]} {customer[1]} | {customer[2]}')

# Query : Where clause - kind of if statement
# SELECT * FROM table WHERE predicate
cursor.execute(""" SELECT * FROM customers WHERE last_name = 'Lima'""")
item = cursor.fetchall()
print("")
print(item)


print("\nCommand executed succesfully...")
# Commit our query
conn.commit()

# Close connection to a database
conn.close()

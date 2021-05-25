# ToDo app based on  Flask Framework
# models.py

#! 1.import sqlite
import sqlite

#! 2. create a connection to DB
connection = sqlite3.connect('todo.db')

#! 3. Write your sql query
query = "<SQLite Query goes here>"

#! 4. execute the query
result = connection.execute(query)

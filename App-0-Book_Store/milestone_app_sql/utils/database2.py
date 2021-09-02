import sqlite3

"""Concerned with storing and retrieving books from a database"""

# ! ------------------------------Queries-----------------------------------
CREATE_BOOKS_TABLE = """ CREATE TABLE IF NOT EXISTS books(
    name TEXT PRIMARY KEY,
    author TEXT,
    read INTEGER);"""

INSERT_BOOKS = """INSERT INTO
    books (name, author, read) VALUES (?, ?, 0);"""

SELECT_ALL_BOOKS = "SELECT * FROM books"
SET_BOOK_READ = 'UPDATE books SET read=1 WHERE name = ?'
DELETE_BOOKS = 'DELETE FROM books WHERE name = ?'

connection = sqlite3.connect('data.db')


# ! Functions to interact with Books table
def create_book_table():
    """[Function to create the Books table]
    """
    with connection:
        connection.execute(CREATE_BOOKS_TABLE)


def add_book(name, author):
    with connection:
        connection.execute(INSERT_BOOKS, (name, author))


def get_all_books():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_BOOKS)
        books = [
            {'name': row[0], 'author': row[1], 'read': row[2]}
            for row in cursor.fetchall()
            ]
    return books


def mark_book_as_read(name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SET_BOOK_READ, (name, ))


def delete_book(name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(DELETE_BOOKS, (name,))

import sqlite3
from .connector_class import DatabaseConnection

"""Managing movie database: create, read, find """
"""Using database sqlite3 to store the movies"""
# each movie will have this format on movies database
"""
movie = id, title, director, year\n
"""


# create the movies database: create_movies_db()
def create_movies_db():
    with DatabaseConnection('MOVIES.db') as connection:
        cursor = connection.cursor()

        sql = """ CREATE TABLE IF NOT EXISTS movies(
        id integer primary key,
        title text NOT NULL,
        director text NOT NULL,
        year text NOT NULL
        )"""
        cursor.execute(sql)


def add_movie(id, title, director, year):
    with DatabaseConnection('MOVIES.db') as connection:
        cursor = connection.cursor()

        # Table movies creation
        sql = """ INSERT INTO movies(id, title, director, year)
        VALUES(?, ?, ?, ?)"""
        cursor.execute(sql, (id, title, director, year))


def get_all_movies():
    with DatabaseConnection('MOVIES.db') as connection:
        cursor = connection.cursor()
        query = 'SELECT * FROM movies'
        cursor.execute(query)
        all_movies = cursor.fetchall()
        movies = [{'id': row[0],
               'title': row[1],
               'director': row[2],
               'year': row[3]} for row in all_movies]
        return movies


def find_movie(movie_name):
    with DatabaseConnection('MOVIES.db') as connection:
        cursor = connection.cursor()
        query = """ SELECT * FROM movies WHERE title = ? """
        cursor.execute(query, (movie_name,))
        movie = cursor.fetchone()
        return movie

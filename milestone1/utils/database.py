"""Managing movie database: create, read, find """

movies = []
# each movie will have this format on movies list
"""
movie = {
    'title': title,
    'director': director,
    'year': year}
"""


def create_movies_table():
    pass


def add_movie(title, director, year):
    movies.append({'title': title,
                   'director': director,
                   'year': year})


def get_all_movies():
    return movies


def find_movie(movie_name):
    global movies
    movies = [movie for movie in movies if movie['title'] == movie_name]
    return movies

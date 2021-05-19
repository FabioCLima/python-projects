"""Managing movie database: create, read, find """
"""Using files instead lists"""

# each movie will have this format on movies list
"""
movie = {
    'title': title,
    'director': director,
    'year': year}
title, author, year\n
"""
movies_file = 'movies.txt'


def create_movies_file():
    with open(movies_file, 'w+') as file:
        pass


def add_movie(title, director, year):
    with open(movies_file, 'a') as file:
        file.write(f"{title}, {director}, {year}\n")


def get_all_movies():
    with open(movies_file, "r") as file:
        movies = [movie.strip().split(",") for movie in file.readlines()]
    return [{'title': movie[0], 'director': movie[1], 'year': movie[2]}
            for movie in movies
           ]


def find_movie(movie_name):
    movies = get_all_movies()
    for movie in movies:
        if movie['title'] ==  movie_name:
            return f"{movie['title']} by {movie['director']}--{movie['year']}"

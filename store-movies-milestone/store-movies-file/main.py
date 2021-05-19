"""
movies = {
    'name' : 'The Matrix',
    'director',
    'year' : '1994'}
"""
from utils import database

MENU_PROMPT = """
Enter:
    - a: add a movie
    - l: list movies
    - f: find a movie
    - q: to quit

Choose a option:  """


def add_movie():
    title = input('Enter the movie title: ')
    director = input('Enter the movie director: ')
    year = input('Enter the movie release year: ')

    database.add_movie(title, director, year)


def list_movies():
    movies = database.get_all_movies()
    for movie in movies:
        print(f"\nTitle:{movie['title']}, \nDirector:{movie['director']}, \nRelease year: {movie['year']}")
        print("*********************")


def find_movie():
    movie_name = input('Type the title of the movie you want to look.  ')
    movies = database.find_movie(movie_name)
    print(movies)


user_options = {"a": add_movie,
                "l": list_movies,
                "f": find_movie}


def main():
    database.create_movies_file()
    option = input(MENU_PROMPT)
    while option != 'q':
        if option in user_options:
            option_function = user_options[option]
            option_function()
        else:
            print("Unknown command. Please try again.")
        option = input(MENU_PROMPT)


main()

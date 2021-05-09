# !/milestone_app_lists/utils/database.py

"""[Concerned with storing and retrieving books from a list.]"""

books = []  # global variable


def create_book_table():
    pass


def insert_book(name: str, author: str):
    """[Adds the book's information to a list]

    Args:
        name (str): [name of the book]
        author (str): [name of the author s book]

    Returns:
        dict: [database structure that holds the books information]
    """

    books.append({'name': name, 'author': author, 'read': False})


def get_all_books():
    """[get all the books name]

    Returns:
        [list]: [all books(dictionaty structure) save on the books list]
    """
    return books


def mark_book_as_read(name):
    """[function to change the boolean condition on read book]

    Args:
        name ([str]): [name of the book the user read]
    """
    for book in books:
        if book['name'] == name:
            book['read'] = True


def delete_book(name):
    """[delete a book from the database after the user read it.]

    Args:
        name ([type]): [description]
    """
    global books
    books = [book for book in books if book["name"] != name]

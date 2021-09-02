import sqlite3
from utils import database2

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all the books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def prompt_add_book():
    """[Asks to the user the information regards to the book]
    """
    try:
        name = input("Enter the new book name:\n")
        author = input("Enter the new book author's name:\n")

        database2.add_book(name, author)
    except sqlite3.IntegrityError:
        print('The book you are trying to create already exist on database.')
        print('Try another one.')


def list_books():
    """[list all the books available in the database]
    """
    books = database2.get_all_books()
    for book in books:
        read = 'YES' if book['read'] == 1 else 'NO'
        print(f"{book['name']} by {book['author']},read:{read}")


def prompt_read_book():
    """[save the name of the book the user finished reading.]
    """
    name = input('Enter the name of the book you just finished reading: \n')
    database2.mark_book_as_read(name)


def prompt_delete_book():
    """[Asks to the user which book he/she wants to delete]
    """
    name = input("Enter the book's name you wish to delete: \n")
    database2.delete_book(name)


menu_options = {
             "a": prompt_add_book,
             "l": list_books,
             "r": prompt_read_book,
             "d": prompt_delete_book,
              }


def menu():
    """[Menu function to interact with user]"""
    database2.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in menu_options:
            menu_function = menu_options[user_input]
            menu_function()
        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICE)


menu()

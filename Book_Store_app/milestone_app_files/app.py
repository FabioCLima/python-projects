#!/milestone_app_lists/app.py

from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all the books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:  """


def menu():
    """[Menu function to interact with user]"""
    database.create_book_table
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICE)


def prompt_add_book():
    """[Asks to the user the information regards to the book]
    """
    name = input("Enter the new book name:\n")
    author = input("Enter the new book author's name:\n")

    database.insert_book(name, author)


def list_books():
    """[list all the books available in the database]
    """
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read']=='1' else 'NO'
        print(f"{book['name']} by {book['author']}, Read:{read}")


def prompt_read_book():
    """[save the name of the book the user finished reading.]
    """
    name = input('Enter the name of the book you just finished reading: \n')
    database.mark_book_as_read(name)


def prompt_delete_book():
    """[Asks to the user which book he/she wants to delete]
    """
    name = input("Enter the book's name you wish to delete: \n")
    database.delete_book(name)


menu()

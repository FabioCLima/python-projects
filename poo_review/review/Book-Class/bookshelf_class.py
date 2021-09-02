from typing import List  # Tuple, Set, etc ...


class Book:

    def __init__(self, name: str, number_of_pages: int):
        self.name = name
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"<Book {self.name} has {self.number_of_pages} pages>"


class Bookshelf:

    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."


book1 = Book("Python Cookbook", 1500)
print(book1)

# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Marks a book as checked out if it exists and is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available or doesn't exist.")

    def return_book(self, title):
        """Marks a book as returned if it exists."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' is not currently checked out or doesn't exist.")

    def list_available_books(self):
        """Lists all available (not checked out) books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        for book in available_books:
            print(f"{book.title} by {book.author}")

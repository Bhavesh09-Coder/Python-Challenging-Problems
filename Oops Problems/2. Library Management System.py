class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  # Initialize book with title and author

class Borrower:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # Initialize borrower with name and an empty list of borrowed books

    def borrow_book(self, book):
        self.borrowed_books.append(book)  # Add book to borrower's borrowed books list
        print(f"{self.name} borrowed {book.title}")

    def return_book(self, book):
        self.borrowed_books.remove(book)  # Remove book from borrower's borrowed books list
        print(f"{self.name} returned {book.title}")

class Library:
    def __init__(self):
        self.books = []  # Initialize library with an empty list of books
        self.borrowers = []  # Initialize library with an empty list of borrowers

    def add_book(self, book):
        self.books.append(book)  # Add book to the library's list of books
        print(f"Added book: {book.title} by {book.author}")

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)  # Add borrower to the library's list of borrowers
        print(f"Added borrower: {borrower.name}")

if __name__ == "__main__":
    library = Library()  # Create a Library instance
    book1 = Book("1984", "George Orwell")  # Create a Book instance
    book2 = Book("To Kill a Mockingbird", "Harper Lee")  # Create another Book instance

    borrower = Borrower("Bob")  # Create a Borrower instance

    library.add_book(book1)  # Add book1 to the library
    library.add_book(book2)  # Add book2 to the library
    library.add_borrower(borrower)  # Add borrower to the library

    borrower.borrow_book(book1)  # Borrower borrows book1
    borrower.return_book(book1)  # Borrower returns book1

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.__copies = copies

    def get_copies(self):
        return self.__copies

    def borrow(self):
        if self.__copies > 0:
            self.__copies -= 1
            return True
        else:
            print(f"Sorry, '{self.title}' is currently not available for borrowing.")
            return False
           
    def return_book(self):
        self.__copies += 1
        return f"'{self.title}' has been returned. Total copies: {self.__copies}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    print(f"You have borrowed '{book.title}' by {book.author}.")
                return
        print(f"Sorry, '{title}' is not available for borrowing.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                print(f"You have returned '{book.title}' by {book.author}.")

    def show_all_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Copies: {book.get_copies()}")

b1 = Book("JavaScript: The Good Parts", "Douglas Crockford", 3)
b2 = Book("Python Crash Course", "Eric Matthes", 2)
b3 = Book("Clean Code", "Robert C. Martin", 1)


library = Library()
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

library.show_all_books()

library.borrow_book("Clean Code")
library.borrow_book("Clean Code")
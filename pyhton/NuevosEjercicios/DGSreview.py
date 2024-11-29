""" 
1   Create a Book class to represent a book in the library.
    Each book should have:
        A title (str).
        An author (str).
        A status (bool) indicating whether the book is available.

2   Create a Library class that manages the collection of books.
    It should:
        Have a list of books.
        Provide methods to:
            List available books.
            Borrow a book (by title).
            Return a book (by title).

3   Handle the following exceptions:
    Raise a BookNotAvailableException if a user tries to borrow a book that is already borrowed.
    Raise a BookNotFoundException if a user tries to borrow or return a book that does not exist in the library.

4   Write functions to:
    Add books to the library.
    Simulate a user borrowing and returning books. 
"""
class BookNotAvailableException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return f"{self.message}"
    
class BookNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return f"{self.message}"
    
class Book:
    def __init__(self,title,author,status = True):
        self.title = title
        self.author = author
        self.status = status

    def getTitle (self):
        return self.title
    
    def getStatus (self):
        return self.status

    def setStatus (self,status):
        self.status = status

    def __str__(self):
        return f"Title : {self.title}     Author : {self.author}     Status : {self.status}"

class Library:
    def __init__(self,books):
        self.books = books

    def printAvailable(self):
        for book in self.books:
            if(book.getStatus() == True):
                print(str(book))

    def borrowBook (self,ID):
        for book in self.books:
            if (book.getTitle()==ID):
                if book.getStatus() == False:
                    raise BookNotAvailableException("Book not available")
                else:
                    book.setStatus(False)
                    print("Book borrowed")
                return
        raise BookNotFoundException("Book not found")

    def returnBook (self,ID):
        for book in self.books:
            if (book.getTitle()==ID):
                book.setStatus(True)
                print("Book returned")
                return
        raise BookNotFoundException("Book not found")
    
    def __str__(self):
        ListBooks = ""
        for book in self.books:
            ListBooks+="\n"+str(book)
        return f"BOOKS:\n{ListBooks}"

""" Exceptions """
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

""" Clase Book """
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
        return f"Title : {self.title}       Author : {self.author}      Status : {self.status}"

""" Clase Library """
class Library:
    def __init__(self,books):
        self.books = books

    def printAvailable(self):
        for book in self.books:
            if(book.getStatus() == True):
                print(str(book))

    def addBook (self,book):
        self.books.append(book)

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
            ListBooks+="\n\t"+str(book)
        return f"BOOKS:{ListBooks}"


""" Código : """

libros = [
    Book("Cien años de soledad","Gabriel García Márquez"),
    Book("1984","George Orwell"),
    Book("El principito","Antoine de Saint-Exupéry"),
    Book("Orgullo y prejuicio","Jane Austen"),
    Book("Rayuela","Julio Cortázar")
    ]

library = Library(libros)

library.addBook(Book("Don Quijote de la Mancha","Miguel de Cervantes"))

try:
    library.borrowBook("Rayuela")
    library.borrowBook("Orgullo y prejuicio")
    library.borrowBook("El principito")
    library.borrowBook("Este libro no existe")
except BookNotAvailableException  as e:
    print(e)
except BookNotFoundException as e:
    print(e)


try:
    library.borrowBook("Rayuela")
except BookNotAvailableException as e:
    print(e)
except BookNotFoundException as e:
    print(e)

library.printAvailable()

try:
    library.returnBook("Rayuela")
    library.returnBook("Este libro no existe")
except BookNotAvailableException as e:
    print(e)
except BookNotFoundException as e:
    print(e)

library.printAvailable()
print(library)

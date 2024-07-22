class Book:
    def __init__(self, book_id: str, title: str, author: str) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed: bool = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            print(f'Il libro "{self.title}" è già preso in prestito.')

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            print(f'Il libro "{self.title}" non è attualmente in prestito.')

    def __repr__(self):
        return f'Book(book_id={self.book_id}, title="{self.title}", author="{self.author}")'

class Member:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f'Il libro "{book.title}" è già preso in prestito.')

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        else:
            print(f'Il libro "{book.title}" non è stato preso in prestito da questo membro.')

class Library:
    def __init__(self) -> None:
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}

    def add_book(self, book_id: str, title: str, author: str):
        if book_id not in self.books:
            book = Book(book_id, title, author)
            self.books[book_id] = book
        else:
            print(f'Il libro con ID {book_id} esiste già.')

    def register_member(self, member_id: str, name: str):
        if member_id not in self.members:
            member = Member(member_id, name)
            self.members[member_id] = member
        else:
            print(f'Il membro con ID {member_id} è già registrato.')

    def borrow_book(self, member_id: str, book_id: str):
        if member_id not in self.members or book_id not in self.books:
            print('Membro o libro non trovato.')
        else:
            book = self.books[book_id]
            member = self.members[member_id]
            if book.is_borrowed:
                print(f'Il libro "{book.title}" è già in prestito.')
            else:
                book.borrow()
                member.borrow_book(book)
    
    def return_book(self, member_id: str, book_id: str):
        if member_id not in self.members or book_id not in self.books:
            print('Membro o libro non trovato.')
        else:
            book = self.books[book_id]
            member = self.members[member_id]
            if book not in member.borrowed_books:
                print(f'Il libro "{book.title}" non è stato preso in prestito da questo membro.')
            else:
                member.return_book(book)
        
    def get_borrowed_books(self, member_id: str):
        if member_id in self.members:
            return self.members[member_id].borrowed_books
        else:
            print('Membro non trovato.')
            return []

# Esempio di utilizzo
library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Registrazione membri
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Prestito di libri
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Dovrebbe stampare: [Book(book_id='B001', title='The Great Gatsby', author='F. Scott Fitzgerald')]
print(library.get_borrowed_books("M002"))  # Dovrebbe stampare: [Book(book_id='B002', title='1984', author='George Orwell')]

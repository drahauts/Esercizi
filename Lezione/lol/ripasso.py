class Book:
    def __init__(self, book_id: str, title: str, author: str) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            return 'Errore'

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            return 'Errore.'

class Member:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books:list[Book] = []
    
    def borrow_book(self, book: Book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            return 'Errore'
    
    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        else:
            return 'Errore.'

class Library:
    def __init__(self) -> None:
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}

    def add_book(self, book_id: str, title: str, author: str):
        if book_id not in self.books:
            book = Book(book_id, title, author)
            self.books[book_id] = book
        else:
            raise ValueError('Errore.')
    
    def register_member(self, member_id: str, name: str):
        if member_id not in self.members:
            member = Member(member_id, name)
            self.members[member_id] = member
        else:
            raise ValueError('Errore.')
    
    def borrow_book(self, member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            if not book.is_borrowed:
                member.borrow_book(book)
            else:
                raise ValueError('Book is already borrowed.')
        else:
            raise ValueError('Book not found')
    
    def return_book(self,member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            if book in member.borrowed_books:
                member.return_book(book)
            else:
                raise ValueError('Book not borrowed by this member.')
        else:
            return ValueError('Book not borrowed by this member')
        
    def get_borrowed_books(self, member_id: str):
        if member_id in self.members:
            return [book.title for book in self.members[member_id].borrowed_books]
        else:
            return []
        

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  # Expected output: ['1984']
class Book:

    def __init__(self,title,author,isbn,availability="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability

    def get_book_info(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Availability : {self.availability}")
        print()

    def mark_as_borrowed(self):
        self.availability = "Borrowed"

    def mark_as_returned(self):
        self.availability = "Available"


class Member:
    def __init__(self,librarian_id,name,id):
        self.librarian_id = librarian_id
        self.member_id = id
        self.name = name
        self.borrowed_books = []

    def display_info(self):

        print(f"Name : {self.name}")
        print(f"Member ID : {self.member_id}")
        print(f"Borrowed Books : {len(self.borrowed_books)}")
        print()

    def borrow_book(self,book):
        librarian = libraries.librarians[self.librarian_id]
        book_info = librarian.books[book]
        if(book_info.availability == "Borrowed"):
            print("Book already has been borrowed.")
            return
        librarian.issue_book(self.member_id,book)


    def return_book(self,book):
        librarian = libraries.librarians[self.librarian_id]
        librarian.collect_book(self.member_id,book)


    def display_borrowed_books(self):
        print(self.borrowed_books)


class Librarian:

    book_id = 1
    member_id = 1

    def __init__(self,id):
        self.librarian_id = id
        self.books : dict[str, Book] = {}
        self.members : dict[int, Member] = {}

    def add_book(self,title,author):

        self.books[title] = Book(title,author,self.book_id)
        self.book_id += 1

    def add_member(self,name) -> Member:

        self.members[self.member_id] = Member(self.librarian_id,name,self.member_id)
        self.member_id += 1
        return self.members[self.member_id - 1]

    def issue_book(self,member_id,book):
        self.books[book].mark_as_borrowed()
        self.members[member_id].borrowed_books.append(book)

    def collect_book(self,member_id,book):
        self.books[book].mark_as_returned()
        self.members[member_id].borrowed_books.remove(book)

class Library:

    id = 1

    def __init__(self):
        self.librarians : dict[int,Librarian] = {}

    def add_librarian(self) -> Librarian:
        self.librarians[self.id] = Librarian(self.id)
        self.id += 1
        return self.librarians[self.id - 1]


books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"title": "Moby-Dick", "author": "Herman Melville"},
    {"title": "Pride and Prejudice", "author": "Jane Austen"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"title": "War and Peace", "author": "Leo Tolstoy"},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky"},
    {"title": "Brave New World", "author": "Aldous Huxley"}
]

libraries = Library()
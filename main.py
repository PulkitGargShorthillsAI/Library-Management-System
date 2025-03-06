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
    def __init__(self,name,id):
        
        self.member_id = id
        self.name = name
        self.borrowed_books = []

    def display_info(self):

        print(f"Name : {self.name}")
        print(f"Member ID : {self.member_id}")
        print(f"Borrowed Books : {len(self.borrowed_books)}")
        print()

    def borrow_book(self,book):
        book_info = l1.books[book]
        if(book_info.availability == "Borrowed"):
            print("Book already has been borrowed.")
            return
        l1.issue_book(self.member_id,book)


    def return_book(self,book):
        l1.collect_book(self.member_id,book)


    def display_borrowed_books(self):
        print(self.borrowed_books)


class Librarian:

    book_id = 1
    member_id = 1

    def __init__(self):

        self.books : dict[str, Book] = {}
        self.members : dict[int, Member] = {}

    def add_book(self,title,author):

        self.books[title] = Book(title,author,self.book_id)
        self.book_id += 1

    def add_member(self,name) -> Member:

        self.members[self.member_id] = Member(name,self.member_id)
        self.member_id += 1
        return self.members[self.member_id - 1]

    def issue_book(self,member_id,book):
        self.books[book].mark_as_borrowed()
        self.members[member_id].borrowed_books.append(book)

    def collect_book(self,member_id,book):
        self.books[book].mark_as_returned()
        self.members[member_id].borrowed_books.remove(book)




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


l1 = Librarian()

for book in books:
    l1.add_book(book['title'],book['author'])
    l1.books[book['title']].get_book_info()


Pulkit = l1.add_member("Pulkit")
Naman = l1.add_member("Naman")
Pulkit.display_info()
Pulkit.borrow_book('1984')
Pulkit.display_borrowed_books()
print()

Pulkit.borrow_book('The Hobbit')
Pulkit.display_borrowed_books()
print()

Pulkit.return_book('The Hobbit')

Naman.borrow_book('The Hobbit')
Naman.display_borrowed_books()
print()

for member in l1.members.values():
    member.display_info()


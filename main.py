from library_system import *

l1 = libraries.add_librarian()

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


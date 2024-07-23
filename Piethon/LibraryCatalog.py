class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self):
        print("Enter the book details:")
        title = input("Title: ")
        author = input("Author: ")
        year = input("Publication Year: ")
        isbn = input("ISBN: ")
        book = Book(title, author, year, isbn)
        self.books.append(book)
        print("Book added successfully!")

    def remove_book(self):
        isbn = input("Enter the isbn of the book to remove: ")
        for book in self.books:
            if book.isbn == isbn:
                self.book.remove(book)
                print("Book removed successfully!")
                return
        print("Book not found in the catalog")

    def search_book(self):
        search_term = input("Enter the title, author, or ISBN to search for: ")
        found_books = []
        for book in self.books:
            if (
                    search_term.lower() in book.title.lower()
                    or search_term.lower in book.author.lower()
                    or search_term.lower == book.isbn.lower()
            ):
                found_books.append(book)
        if found_books:
            print("Search results:")
            for book in found_books:
                print(f"Title: {book.title} | Author: {book.author} | Year: {book.year} | ISBN: {book.isbn}")
        else:
            print("No books found matching the search term.")

    def display_books(self):
        if self.books:
            print("Library Catalog:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. Title: {book.title} | Author: {book.author} | Year: {book.year} | ISBN: {book.isbn}")
        else:
            print("The catalog is empty!")

def main():
    catalog = Catalog()
    print("Welcome to the Library Catalog Management System!")

    while True:
        print("\n1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display a book")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            catalog.add_book()
        elif choice == "2":
            catalog.remove_book()
        elif choice == "3":
            catalog.search_book()
        elif choice == "4":
            catalog.display_books()
        elif choice == "5":
            print("Thank you for using the Library Catalog Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

"""
self.availability = True

def borrow_book(self):
    for book in self.books:
        if book.title == title:
            if book.availability:
                book.aailability = False
                print("Book borrowed successfully!")
                return
            else:
                print("Book is already borrowed.")
                return
    print("Book not found.")

def return_book(self):
    for book in self.books:
        if book.title == title:
            if not book.availability:
                book.availability = True
                print("Book returned successfully.")
                return
            else:
                print("Book is already available.")
                return
    print("Book not found")
"""

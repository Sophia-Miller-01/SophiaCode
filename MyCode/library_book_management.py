class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def display_books(self):
        print("Library Books:")
        for book in self.books:
            print(book)

def main():
    library = Library()
    book1 = Book("To Kill a Mockingbird", "Harper Lee")
    book2 = Book("1984", "George Orwell")
    library.add_book(book1)
    library.add_book(book2)
    library.display_books()

if __name__ == "__main__":
    main()

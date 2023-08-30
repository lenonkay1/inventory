class Book:
    def __init__(self, title, author, genre, price, quantity, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity
        self.pages = pages

class BookstoreInventory:
    def __init__(self):
        self.inventory = []

    def add_book(self, book):
        self.inventory.append(book)

    def view_inventory(self, sort_by):
        sorted_inventory = sorted(self.inventory, key=lambda book: getattr(book, sort_by))
        self.display_books(sorted_inventory)

    def search_books(self, search_term):
        found_books = [book for book in self.inventory if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]
        self.display_books(found_books)

    def update_inventory(self, book_title, new_quantity):
        for book in self.inventory:
            if book.title == book_title:
                book.quantity = new_quantity
                print(f"Updated quantity of '{book.title}' to {new_quantity}")
                return
        print("Book not found")

    def delete_book(self, book_title):
        for book in self.inventory:
            if book.title == book_title:
                self.inventory.remove(book)
                print(f"Book '{book.title}' has been removed from inventory")
                return
        print("Book not found")

    @staticmethod
    def display_books(books):
        for book in books:
            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Price: {book.price}, Quantity: {book.quantity}, Pages: {book.pages}")
            
def main():
    bookstore = BookstoreInventory()

    while True:
        print("\nOptions:")
        print("1. Add Book")
        print("2. View Inventory")
        print("3. Search Books")
        print("4. Update Inventory")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            pages = int(input("Enter number of pages: ")) 
            new_book = Book(title, author, genre, price, quantity, pages)
            bookstore.add_book(new_book)
            
        elif choice == '2':
            sort_by = input("Sort by 'genre' or 'author': ").lower()
            bookstore.view_inventory(sort_by)

        elif choice == '3':
            search_term = input("Enter search term: ")
            bookstore.search_books(search_term)
            
        elif choice == '4':
            book_title = input("Enter book title: ")
            new_quantity = int(input("Enter new quantity: "))
            bookstore.update_inventory(book_title, new_quantity)
            
        elif choice == '5':
            book_title = input("Enter book title: ")
            bookstore.delete_book(book_title)
            
        elif choice == '6':
            print("Exiting the bookstore inventory management system")
            break
        
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()


from book import Book
from member import Member
from library import Library
from data_manger import DataManager
def display_menu():
    print("\n" + "=" * 45)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add book")
    print("2. Add membr")
    print("3. Issue book")
    print("4. Return book")
    print("5. View all books")
    print("6. View all members")
    print("7. Search for a book")
    print("8. View library report")
    print("9. Exit")
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")
def add_book_menu(library):
    print("\n--- Add a Book ---")
    book_id = get_non_empty_input("ENter book ID: ")
    title = get_non_empty_input("Enter book title: ")
    author = get_non_empty_input("Enter aurhor name: ")
    category = get_non_empty_input("Enter category: ")
    new_book = Book(book_id, title, author, category)
    if library.add_book(new_book):
        DataManager.save_data(library)
        print("Book added successfully.")
    else:
        print("A book with this ID already exists.")
def add_member_menu(library):
    print("\n--- Add Member ---")
    member_id = get_non_empty_input("Enter member ID: ")
    name = get_non_empty_input("Enter member name: ")
    email = get_non_empty_input("Enter email: ")
    new_member = Member(member_id, name, email)
    if library.add_member(new_member):
        DataManager.save_data(library)
        print("Member added successfully.")
    else:
        print("A member with this ID already exists.")
def issue_book_menu(library):
    print("\n--- Issue a Book ---")
    book_id = get_non_empty_input("Enter book ID: ")
    member_id = get_non_empty_input("Enter member ID: ")
    success, message = library.issue_book(book_id, member_id)
    if success:
        DataManager.save_data(library)
    print(message)
def return_book_menu(library):
    print("\n--- Return a Book ---")
    book_id = get_non_empty_input("Enter book ID: ")
    member_id = get_non_empty_input("Enter member ID: ")
    success, message = library.return_book(book_id, member_id)
    if success:
        DataManager.save_data(library)
    print(message)
def view_books_menu(library):
    print("\n--- All Books ---")
    if not library.books:
        print("No books found.")
        return
    for book in library.books:
        print(book)
def view_members_menu(library):
    print("\n--- All Members ---")
    if not library.members:
        print("No members found")
        return
    for member in library.members:
        print(member)
def search_book_menu(library):
    print("\n--- Search for a Book ---")
    book_id = get_non_empty_input("Enter book ID: ")
    book = library.find_book(book_id)
    if book is None:
        print("Book not found.")
    else:
        print(book)
def report_menu(library):
    print("\n--- Library Report ---")
    report = library.library_report()
    print(f"Total books: {report['total_books']}")
    print(f"Issued books: {report['issued_books']}")
    print(f"Available books: {report['available_books']}")
    print(f"Total members: {report['total_members']}")
def main():
    library = Library()
    DataManager.load_data(library)
    print("Saved library data loaded successfully")
    while True:
        display_menu()
        choice = input("Choose an option (1-9): ").strip()
        if choice == "1":
            add_book_menu(library)
        elif choice == "2":
            add_member_menu(library)
        elif choice == "3":
            issue_book_menu(library)
        elif choice == "4":
            return_book_menu(library)
        elif choice == "5":
            view_books_menu(library)
        elif choice == "6":
            view_members_menu(library)
        elif choice == "7":
            search_book_menu(library)
        elif choice == "8":
            report_menu(library)
        elif choice == "9":
            DataManager.save_data(library)
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 9.")
        input("\nPress Enter to contiue...")
main()
            


        


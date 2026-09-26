from book import Book
from member import Member
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                return False
        self.books.append(book)
        return True 
    def add_member(self, member):
        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                return False
        self.members.append(member)
        return True
    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book 
        return None 
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    def issue_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        if book is None or member is None:
            return False, "Book or member not found."
        if book.is_issued:
            return False, "This book is already issued."
        book.issue_book()
        member.borrow_book(book_id)
        return True, "Book issued successfully."
    def return_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        if book is None or member is None:
            return False, "Book or member not found."
        if not book.is_issued:
            return False, "This book is not currently issued."
        if book_id not in member.borrowed_books:
            return False, "This member did not borrow this book."
        book.return_book()
        member.return_book(book_id)
        return True, "Book returned successfully."
    def available_books(self):
        return [book for book in self.books if not book.is_issued]
    def library_report(self):
        total_books = len(self.books)
        issued_books = len([book for book in self.books if book.is_issued])
        available_books = total_books - issued_books
        total_members = len(self.members)
        return {
            "total_books": total_books,
            "issued_books": issued_books,
            "available_books": available_books,
            "total_members": total_members
        }

        


        

    
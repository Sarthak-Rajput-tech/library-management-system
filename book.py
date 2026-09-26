class Book:
    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.is_issued = False
    def issue_book(self):
        self.is_issued = True
    def return_book(self):
        self.is_issued = False
    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "is_issued": self.is_issued
        }
    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["category"]
        )
        book.is_issued = data["is_issued"]
        return book
    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"ID: {self.book_id} | {self.title} by {self.author} | {self.category} | {status}"
    
        
        
        

    
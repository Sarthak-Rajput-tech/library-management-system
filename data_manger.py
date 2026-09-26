import json 
import os
from book import Book 
from member import Member
class DataManager:
    FILE_NAME = "library_data.json"
    @classmethod
    def save_data(cls, library):
        data = {
            "books": [book.to_dict() for book in library.books],
            "members": [member.to_dict() for member in library.members]
        }
        with open(cls.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)
    @classmethod
    def load_data(cls, library):
        if not os.path.exists(cls.FILE_NAME):
            return
        with open(cls.FILE_NAME, "r") as file:
            data = json.load(file)
        library.books = [
            Book.from_dict(book_data)
            for book_data in data.get("books", [])
        ]
        library.members = [
            Member.from_dict(member_data)
            for member_data in data.get("members", [])
        ]


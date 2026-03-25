import json
import os
from src.books.book import Book
from src.books.book_repository_protocol import BookRepositoryProtocol
from src.books.book_repository_abc import BookRepositoryABC

class BookRepository(BookRepositoryABC):
    def __init__(self, filepath: str="books.json"):
        self.filepath = filepath

    def add_book(self, book:Book) -> str:

        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([book.to_dict()], f, indent=2)
                return book.book_id

        books = self.get_all_books()
        books.append(book)
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([b.to_dict() for b in books], f, indent=2)
        return book.book_id
    
    def get_all_books(self) -> list[Book]:

        if not os.path.exists(self.filepath):
            return []

        with open(self.filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Book.from_dict(item) for item in data]

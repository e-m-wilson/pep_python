from typing import Protocol
from src.books.book import Book

class BookRepositoryProtocol(Protocol):
    def add_book(self, book:Book) -> str:
        ...

    def get_all_books(self) -> list[Book]:
        ...
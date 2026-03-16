from src.books.book_repository_protocol import BookRepositoryProtocol
from src.books.book import Book

class BookService:
    def __init__(self, repo:BookRepositoryProtocol):
        self.repo = repo

    def add_book(self, book:Book) -> str:
        return self.repo.add_book(book)
    
    def get_all_books(self) -> list[Book]:
        return self.repo.get_all_books()
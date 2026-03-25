from abc import ABC, abstractmethod
from src.books.book import Book

class BookRepositoryABC(ABC):
    '''
        have notes about the class
    '''
    @abstractmethod
    def add_book(self, book:Book) -> str:
        pass

    @abstractmethod
    def get_all_books(self) -> list[Book]:
        pass

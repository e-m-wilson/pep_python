from sqlalchemy.orm import Session
from src.books.book import Book
from src.books.book_repository_protocol import BookRepositoryProtocol

class BookRepositorySQL(BookRepositoryProtocol):
    def __init__(self, session: Session):
        self.session = session

    def get_all_books(self) -> list[Book]:
        return self.session.query(Book).all()
    
    def add_book(self, book:Book) -> str:
        self.session.add(book)
        self.session.commit()
        return str(book.book_id)

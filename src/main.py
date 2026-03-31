from uuid import UUID
from fastapi import Depends, FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from sqlalchemy.orm import Session

from src.db.deps import get_db
from src.books.book import Book
from src.books.book_dto import BookCreate, BookRead

from src.books.book_repository_sql import BookRepositorySQL
from src.books.book_service import BookService


app = FastAPI(title="Book API")


'''
    This section sets up dependency injections for our FastAPI endpoints to make use of.
    If we ever need to change anything, i.e. a service or repo, we can simply change it here instead of 
    having to edit multiple endpoints
'''
def get_book_repository(db: Session = Depends(get_db)) -> BookRepositorySQL:
    return BookRepositorySQL(db)

def get_book_service(repo: BookRepositorySQL = Depends(get_book_repository)) -> BookService:
    return BookService(repo)


'''
        ENDPOINTS
'''

@app.get("/books", response_model=list[BookRead])
def list_books(
    svc: BookService = Depends(get_book_service)
):
    return svc.get_all_books()


@app.post("/books", response_model=str)
def create_book(
    payload: BookCreate,
    svc: BookService = Depends(get_book_service)
):
    book = Book(**payload.model_dump())
    book_id = svc.add_book(book)
    return book_id

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.book import create_book, get_books
from app.database.connection import get_db
from app.schemas.book import BookCreate, BookResponse


router = APIRouter(prefix="/books",tags=["Books"],)


# Create a new book
@router.post("/", response_model=BookResponse, status_code=201)
def create_book_route(book: BookCreate, db: Session = Depends(get_db),):
    return create_book(db, book)

# Get all books
@router.get("/", response_model=list[BookResponse])
def get_books_route(db: Session = Depends(get_db)):
    return get_books(db)
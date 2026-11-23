from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate


# Create a new book
def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.model_dump())

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book

# Get all books
def get_books(db: Session):
    return db.scalars(select(Book)).all()
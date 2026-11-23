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

# Get an existing book
def get_book(db:Session, book_id: int):
    return db.get(Book, book_id)

# Update an existing book
def update_book(db: Session, book_id: int, book_data: BookCreate):
    db_book = db.get(Book, book_id)

    if db_book is None:
        return None

    for key, value in book_data.model_dump().items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)

    return db_book

# Delete an existing book
def delete_book(db: Session, book_id: int):
    db_book = db.get(Book, book_id)

    if db_book is None:
        return None

    db.delete(db_book)
    db.commit()

    return True
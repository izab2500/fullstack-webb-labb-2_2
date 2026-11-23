from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine
from app.models.book import Book
from app.routes.book import router as book_router

app = FastAPI(title="Book API", description="A REST API for managing books")

# Create database tables
Base.metadata.create_all(bind=engine)

# Root endpoint to check if the API is running
@app.get("/")
def root():
    return {"message": "Book API is running"}

# Register the book router
app.include_router(book_router)
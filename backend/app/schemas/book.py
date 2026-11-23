from pydantic import BaseModel, ConfigDict, Field


# Data needed to create a book
class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    author: str = Field(min_length=1, max_length=255)
    publication_year: int = Field(gt=0)
    is_read: bool = False


# Data returned when a book is requested
class BookResponse(BookCreate):
    id: int

    # Allow data from SQLAlchemy models
    model_config = ConfigDict(from_attributes=True)
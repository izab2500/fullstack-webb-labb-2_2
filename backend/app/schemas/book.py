from pydantic import BaseModel, ConfigDict, Field, field_validator


# Data needed to create a book
class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    author: str = Field(min_length=1, max_length=255)
    publication_year: int = Field(gt=0)
    is_read: bool = False

    @field_validator("title", "author")
    @classmethod
    def validate_text(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty or contain only whitespace")

        return value


# Data returned when a book is requested
class BookResponse(BookCreate):
    id: int

    # Allow data from SQLAlchemy models
    model_config = ConfigDict(from_attributes=True)
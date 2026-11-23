from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Book(Base):
    # Database table name
    __tablename__ = "books"

    # Primary key
    id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True,)

    # Book title
    title: Mapped[str] = mapped_column(String(255), nullable=False)

    # Book author
    author: Mapped[str] = mapped_column(String(255), nullable=False)

    # Year the book was published
    publication_year: Mapped[int] = mapped_column(Integer, nullable=False)

    # Indicates whether the book has been read
    is_read: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
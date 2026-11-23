from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


# Create the database engine
engine = create_engine(settings.DATABASE_URL)


# Create a database session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# Provide a database session for each request
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

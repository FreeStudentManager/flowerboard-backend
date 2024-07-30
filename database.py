from sqlmodel import create_engine

from config import DATABASE_URL, DEBUG

engine = create_engine(DATABASE_URL, echo=DEBUG)

__all__ = ['engine']

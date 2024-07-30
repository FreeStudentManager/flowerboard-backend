from sqlmodel import create_engine

from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

__all__ = ['engine']

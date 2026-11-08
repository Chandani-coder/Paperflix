from pathlib import Path

from sqlalchemy import create_engine, event
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_PATH = Path(__file__).resolve().parent / "paperflix.db"

DATABASE_URL = f"sqlite:///{DB_PATH.as_posix()}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

@event.listens_for(engine, "connect")
def enable_foreign_keys(connection, record):
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.close()

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(
    bind= engine,
    autoflush=False,
    autocommit = False
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

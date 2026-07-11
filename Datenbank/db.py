from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, DeclarativeBase


#Verbindung der Datenbank zum SQL - Container
DATABASE_URL = (
    "postgresql+psycopg://max:geheim@localhost:5432/testdb"
)

# Erstellung einer Engine 
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False
    )

# Verbindung testen 
with engine.connect() as connection:
    print("Verbindung erfolgreich!")

# Session erzeugen 
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    """Basisklasse für alle ORM-Modelle."""
    pass


@contextmanager
def get_session():
    """Session mit garantiertem Aufräumen – wie 'with open()' für Dateien."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
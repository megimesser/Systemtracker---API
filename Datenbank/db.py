from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import DATABASE_PW,DATABASE_DB,DATABASE_USER

#Verbindung der Datenbank zum SQL - Container
DATABASE_URL = (
    f"postgresql+psycopg://{DATABASE_USER}:{DATABASE_PW}@localhost:5433/{DATABASE_DB}"
)

#Verbindung deaful

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

Base = DeclarativeBase()


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
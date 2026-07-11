from db import engine, Base, DATABASE_URL
import models  # noqa: F401 – Import nötig, damit die Modelle registriert werden


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Tabellen erstellt.")


if __name__ == "__main__":
    print(DATABASE_URL)
    #init_db()

from db import engine, Base
import models  # noqa: F401 – Import nötig, damit die Modelle registriert werden


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Tabellen erstellt.")


if __name__ == "__main__":
    init_db()

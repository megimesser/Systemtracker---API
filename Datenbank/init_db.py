from Datenbank.db import engine, Base, DATABASE_URL
import Datenbank.models  # noqa: F401 – Import nötig, damit die Modelle registriert werden


def init_db():
    Base.metadata.drop_all(bind=engine)     # löscht ALLE Tabellen – Daten weg!
    Base.metadata.create_all(bind=engine)
    print("Drop/Create wird ausgeführt")
    print("Tabellen erstellt.")


if __name__ == "__main__":
    #print(DATABASE_URL)
    init_db()

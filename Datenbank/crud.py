#from sqlalchemy import select 
from Datenbank.db import get_session
from Datenbank.models import Datentraeger
import json
from config import DISK


def opener(data):
    with open (data,"r") as f:
        return json.load(f)





def speichere_positionen(daten: list[dict]) -> str:
    with get_session() as session:
        objekte = [
            Datentraeger(
                filesystem=eintrag["filesystem"],
                size=eintrag["size"],
                used=eintrag["used"],
                available=eintrag["available"],
                capacity=eintrag["capacity"],
                mounted_on=eintrag["mounted_on"],
            )
            for eintrag in daten
        ]
        session.add_all(objekte)
        return len(objekte)

if __name__ == "__main__":
    speichere_positionen(opener(DISK))
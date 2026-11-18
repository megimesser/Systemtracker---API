import json
from config import HOST_DATA


def lade_hostname(pfad: str) -> str:
    with open(pfad, encoding="utf-8") as f:
        host_daten = json.load(f)
    return host_daten[0]["hostname"]
import json

from config import HOST_DATA

with open(HOST_DATA, encoding="utf-8") as f:
    host_daten = json.load(f)


print(host_daten[0]["hostname"])
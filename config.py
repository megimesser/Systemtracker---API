import os 
from pathlib import Path 
import json


BASE_DIR = Path(__file__).resolve().parent

DISK = BASE_DIR / "Systemtracker" / "disk.json"

DISK_DATA = BASE_DIR / "data" / "disk.json"
RAM_DATA = BASE_DIR / "data" / "ram.json"
UPTIME_DATA = BASE_DIR / "data" / "uptime.json"
DOCKER_DATA = BASE_DIR / "data" / "docker.json"
TEMP_DATA = BASE_DIR / "data" / "temp.json"
JOURNAL_DATA = BASE_DIR / "data" / "journal.json"
MEM_DATA = BASE_DIR / "data" / "mem.json"



 
#Befehlskette 
# Diese Befehlskette sollen beim Aufruf des Systemtrackers alle durchgeführt werden 

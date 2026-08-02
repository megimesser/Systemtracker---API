import os 
from pathlib import Path 
import json
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent

DISK = BASE_DIR / "Systemtracker" / "disk.json"

DISK_DATA = BASE_DIR / "data" / "disk.json"
RAM_DATA = BASE_DIR / "data" / "ram.json"
UPTIME_DATA = BASE_DIR / "data" / "uptime.json"
DOCKER_DATA = BASE_DIR / "data" / "docker.json"
TEMP_DATA = BASE_DIR / "data" / "temp.json"
JOURNAL_DATA = BASE_DIR / "data" / "journal.json"
MEM_DATA = BASE_DIR / "data" / "mem.json"
CPU_DATA = BASE_DIR / "data" / "cpu.json"



load_dotenv(BASE_DIR / ".env")

DATABASE_PW = os.getenv("DATABASE_PW")
 
#Befehlskette 
# Diese Befehlskette sollen beim Aufruf des Systemtrackers alle durchgeführt werden 

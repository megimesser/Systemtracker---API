#from sqlalchemy import select 
from Datenbank.db import get_session
from Datenbank.models import Datentraeger, Ram,Sysinfo,Docker,Temp,Proc,Cpu
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


def speichere_positionen_ram(daten: list[dict]) -> str:
    with get_session() as session:
        objekte = [
            Ram(
                total=eintrag["marker"],
                size=eintrag["total"],
                used=eintrag["used"],
                available=eintrag["available"],
                free=eintrag["free"],
            )
            for eintrag in daten
        ]
        session.add_all(objekte)
        return len(objekte)


def speichere_positionen_sys(daten: list[dict]) -> str:
    with get_session() as session:
        objekte = [
            Sysinfo(
                uptime=eintrag["uptime"],
                users=eintrag["users"],
                load_averages =eintrag["load_averages"],
            )
            for eintrag in daten
        ]
        session.add_all(objekte)
        return len(objekte)


def speichere_positionen_docker(daten: list[dict]) -> str:
    with get_session() as session:
        objekte = [
            Docker(
                image=eintrag["container"],
                runtime=eintrag["runtime"],
                status = eintrag["status"]
            )
            for eintrag in daten
        ]
        session.add_all(objekte)
        return len(objekte)
    


def speichere_positionen_temp(daten: list[dict]) -> str:
    with get_session() as session:
        objekte = [
            Temp(
                temp=eintrag["temp"],   
            )
            for eintrag in daten
        ]
        session.add_all(objekte)
        return len(objekte)
    

def speichere_positionen_proc(daten: list[dict]) -> str:
    with get_session() as session:
        objekte = [
            Proc(
                user=eintrag["User"],  
                pid=eintrag["PID"], 
                mem=eintrag["%MEM"], 
            )
            for eintrag in daten
        ]
        session.add_all(objekte)
        return len(objekte)


def speichere_positionen_cpu(daten: list[dict]) -> str:
    with get_session() as session:
        objekte = [
            Proc(
                user=eintrag["User"],  
                pid=eintrag["PID"], 
                cpu=eintrag["%CPU"], 
            )
            for eintrag in daten
        ]
        session.add_all(objekte)
        return len(objekte)
    






if __name__ == "__main__":
    speichere_positionen(opener(DISK))
    speichere_positionen_ram(opener(DISK))
    speichere_positionen_sys(opener(DISK))
    speichere_positionen_docker(opener(DISK))
    speichere_positionen_temp(opener(DISK))
    speichere_positionen_proc(opener(DISK))
    speichere_positionen_cpu(opener(DISK))
    
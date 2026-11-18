#from sqlalchemy import select 
from Datenbank.db import get_session
from Datenbank.helper import lade_hostname
from Datenbank.models import Datentraeger, Ram,Sysinfo,Docker,Temp,Proc,Cpu,Host
import json
from config import DISK_DATA,RAM_DATA,UPTIME_DATA,DOCKER_DATA,TEMP_DATA,JOURNAL_DATA,MEM_DATA,CPU_DATA,HOST_DATA,COUNTER_DATA


def opener(data):
    try:
        with open(data, "r") as f:
            return json.load(f)

    except json.JSONDecodeError as err:
        print(f"Die Datei {data} kann leider nicht verarbeitet werden")
        print(err)
        raise

    except TypeError as err_t:
        print(f"Fehler: {err_t}")
        raise



def counter(data, field, number):

    
    # JSON laden
    with open(data, "r", encoding="utf-8") as file:
        f = json.load(file)

    # Wert ändern
    f[field] = number

    # Dictionary wieder speichern
    with open(data, "w", encoding="utf-8") as file:
        json.dump(f, file, indent=4, ensure_ascii=False)


def speichere_positionen(counter_path,daten: list[dict], hostname: str) -> int:
    with get_session() as session:
        objekte = [
            Datentraeger(
                hostname = hostname,
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

        counter(counter_path,"DATA",len(objekte))
        return print(len(objekte))


def speichere_positionen_ram(counter_path,daten: list[dict], hostname: str) -> int:
    with get_session() as session:
        objekte = [
            Ram(
                hostname = hostname,
                marker=eintrag["marker"],
                total=eintrag["total"],
                used=eintrag["used"],
                available=eintrag["available"],
                free=eintrag["free"],
            )
            for eintrag in daten
        ]
        session.add_all(objekte)

        counter(counter_path,"RAM",len(objekte))
        return print(len(objekte))


def speichere_positionen_sys(counter_path,daten: list[dict], hostname: str) -> int:
    with get_session() as session:
        objekte = [
            Sysinfo(
                hostname = hostname,
                uptime=eintrag["uptime"],
                users=eintrag["users"],
                load_averages =eintrag["load_averages"],
            )
            for eintrag in daten
        ]
        session.add_all(objekte)

        counter(counter_path,"SYS",len(objekte))
        return print(len(objekte))


def speichere_positionen_docker(counter_path,daten: list[dict], hostname: str) -> int:
    with get_session() as session:
        objekte = [
            Docker(
                hostname = hostname,
                image= eintrag["image"],
                name=eintrag["container"],
                runtime=eintrag["runtime"],
                status = eintrag["status"],
                ports=eintrag["ports"]
            )
            for eintrag in daten
        ]
        session.add_all(objekte)

        counter(counter_path,"DOCKER",len(objekte))
        return len(objekte)
    


def speichere_positionen_temp(counter_path,daten: list[dict], hostname: str) -> int:
    with get_session() as session:
        objekte = [
            Temp(
                hostname = hostname,
                temp=eintrag["temp"],   
            )
            for eintrag in daten
        ]
        session.add_all(objekte)

        counter(counter_path,"TEMP",len(objekte))
        return len(objekte)
    

def speichere_positionen_proc(counter_path,daten: list[dict], hostname: str) -> int:
    with get_session() as session:
        objekte = [
            Proc(
                hostname = hostname,
                user=eintrag["User"],  
                pid=eintrag["PID"], 
                Mem=eintrag["%MEM"], 
            )
            for eintrag in daten
        ]
        session.add_all(objekte)

        counter(counter_path,"PROC",len(objekte))
        return len(objekte)


def speichere_positionen_cpu(counter_path,daten: list[dict],hostname: str) -> int:
    with get_session() as session:
        objekte = [
            Cpu(
                hostname = hostname,
                user=eintrag["User"],  
                pid=eintrag["PID"], 
                CPU=eintrag["%CPU"], 
            )
            for eintrag in daten
        ]
        session.add_all(objekte)

        counter(counter_path,"CPU",len(objekte))
        return len(objekte)
    

def speichere_positionen_host(counter_path,daten: list[dict], hostname: str) -> int:
    with get_session() as session:
        objekte = [
            Host(
                hostname = hostname,
                hostname=eintrag["hostname"],  
                system=eintrag["system"], 
                kernel=eintrag["kernel"], 
                architecture=eintrag["architecture"]
            )
            for eintrag in daten
        ]
        session.add_all(objekte)
        print("host ist drin")

        counter(counter_path,"HOST",len(objekte))
        return len(objekte)
    






if __name__ == "__main__":
    speichere_positionen(COUNTER_DATA,opener(DISK_DATA),lade_hostname(HOST_DATA))
    speichere_positionen_ram(COUNTER_DATA,opener(RAM_DATA),lade_hostname(HOST_DATA))
    speichere_positionen_sys(COUNTER_DATA,opener(UPTIME_DATA),lade_hostname(HOST_DATA))
    speichere_positionen_docker(COUNTER_DATA,opener(DOCKER_DATA),lade_hostname(HOST_DATA))
    speichere_positionen_temp(COUNTER_DATA,opener(TEMP_DATA),lade_hostname(HOST_DATA))
    speichere_positionen_proc(COUNTER_DATA,opener(MEM_DATA),lade_hostname(HOST_DATA))
    speichere_positionen_cpu(COUNTER_DATA,opener(CPU_DATA),lade_hostname(HOST_DATA))
    speichere_positionen_host(COUNTER_DATA,opener(HOST_DATA),lade_hostname(HOST_DATA))

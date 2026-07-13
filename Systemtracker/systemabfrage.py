import subprocess 
import shlex
from rich.console import Console
from rich.panel import Panel
from Systemtracker.helper import df,free, uptime, docker_ps, temp
import json
from config import DISK_DATA,RAM_DATA,UPTIME_DATA,DOCKER_DATA,TEMP_DATA

print(DISK_DATA)


#Systemkette soll nach Implementierung hier integriert werden 
# Level der Befehlsausführung könnten eventuell durch unterschiedliche Level angegeben werden
# Weitere Befehle:

# Logs -> journalctl | tail -20
# Temperatru -> vcgencmd measure_temp
# Benutzer anzeigen -> who
# Topram Prozesse -> ps aux --sort=-%mem | head -10 
# ps aux --sort=-%cpu | head -10

befehlskette = ["df -h","free -h","uptime","docker ps","vcgencmd measure_temp"]


console = Console()

def systemabruf(befehlskette):
    for befehl in befehlskette:
        try: 
            befehl = shlex.split(befehl)


            result = subprocess.run(
                befehl,
                capture_output= True, # Ausgabe erscheint nicht direkt im Terminal --> wird in Python gespeichert 
                text = True, # Konvertiert die Ausgabe von Bytes (bytes) in einen String (str)
                check = True  # Überprüft automatisch den Rückgabecode (returncode)
            )

            lines = result.stdout.splitlines()
            print(befehl)

            if befehl == ['df', '-h']:
                df(lines,DISK_DATA)#"disk.json")

            if befehl == ['free', '-h']:
                free(lines,RAM_DATA)
                            
            if befehl == ['uptime']:
                uptime(lines,UPTIME_DATA)
                

            if befehl == ['docker', 'ps']:
                docker_ps(lines,DOCKER_DATA)

            if befehl == ['vcgencmd', 'measure_temp']:
                temp(lines,TEMP_DATA)




            
            
            #print(result.stdout)

            """

            console.print(
                        Panel.fit(
                result.stdout,
                title="💾 Festplatten",
                border_style="cyan"
            )

            """


            

        except subprocess.CalledProcessError as e:
            print(f"Befehl fehlgeschlagen, returncode {e.returncode}")
        except FileNotFoundError:
            print("Tool ist auf diesem System nicht installiert")



if __name__ == "__main__":
    print(systemabruf(befehlskette))
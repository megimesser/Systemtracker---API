import subprocess 
import shlex
from rich.console import Console
from rich.panel import Panel
import json



#Systemkette soll nach Implementierung hier integriert werden 
# Level der Befehlsausführung könnten eventuell durch unterschiedliche Level angegeben werden

befehlskette = ["df -h","free -h"]
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
                header = lines[0].split()

                entries = []

                for line in lines[1:]:
                    parts = line.split()

                    entries.append({
                        "filesystem": parts[0],
                        "size": parts[1],
                        "used": parts[2],
                        "available": parts[3],
                        "capacity": parts[4],
                        "mounted_on": parts[-1],
                    })

                with open("disk.json", "w") as f:
                    json.dump(entries, f, indent=4)


            if befehl == ['free', '-h']:

                entries = []

                for line in lines[1:]:
                    parts = line.split()

                    entries.append({
                        "marker": parts[0],
                        "total": parts[1],
                        "used": parts[2],
                        "free": parts[3],
                        #"shared": parts[4],
                        "available": parts[-1],
                    })

                with open("ram.json", "w") as f:
                    json.dump(entries, f, indent=4)
            
            print(result.stdout)

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
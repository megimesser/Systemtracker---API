import subprocess 
import shlex
#from rich.console import Console
#from rich.panel import Panel
from Systemtracker.helper import df,free, uptime, docker_ps, temp, journal, process
import json
import re
from config import DISK_DATA,RAM_DATA,UPTIME_DATA,DOCKER_DATA,TEMP_DATA,JOURNAL_DATA, MEM_DATA

print(DISK_DATA)


#Systemkette soll nach Implementierung hier integriert werden 
# Level der Befehlsausführung könnten eventuell durch unterschiedliche Level angegeben werden
# Weitere Befehle:


# Benutzer anzeigen -> who
# Topram Prozesse -> ps aux --sort=-%mem | head -10 
# ps aux --sort=-%cpu | head -10

befehlskette = ["df -h","free -h","uptime","docker ps","vcgencmd measure_temp"]
befehlskette_pipe = ["journalctl | tail -20", "ps aux --sort=-%mem | head -10" ]


#console = Console()

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
            print(f"Befehl fehlgeschlagen, returncode {e.returncode} : Befehl")
        except FileNotFoundError:
            print("Tool ist auf diesem System nicht installiert")


def systemabruf_pipe(befehlskette_pipe):
    for befehl in befehlskette_pipe:
        #try:
            match = re.search("\|", befehl)

            if match:
                davor = befehl[:match.start()].strip()
                danach = befehl[match.end():].strip()
                print(davor)
                print(danach)


                befehl_1 = befehl = shlex.split(davor)
                befehl_2 = befehl = shlex.split(danach)

                ps = subprocess.Popen(
                    befehl_1,
                    stdout=subprocess.PIPE,
                    text=True
                )

                ps_2 = subprocess.run(
                    befehl_2,
                    stdin = ps.stdout,
                    capture_output = True,
                    text = True
                )

                ps.stdout.close()
                ps.wait()

                #print(ps_2.stdout)
                print(befehl_1 + befehl_2)

                lines = ps_2.stdout.splitlines()
                print(lines)


            
                if befehl_1 + befehl_2 == ['journalctl', 'tail', '-20']:
                    journal(lines,JOURNAL_DATA)


                if befehl_1 + befehl_2 == ['ps', 'aux', '--sort=-%mem',  'head', '-10']:
                    process(ps_2.stdout,MEM_DATA)

                    
        
        #except subprocess.CalledProcessError as e:
         #   print(f"Befehl fehlgeschlagen, returncode {e.returncode} : Befehl")



        


if __name__ == "__main__":
    #print(systemabruf(befehlskette))
    print(systemabruf_pipe(befehlskette_pipe))
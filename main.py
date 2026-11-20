from Datenbank.crud import opener,speichere_positionen,speichere_positionen_ram,speichere_positionen_docker,speichere_positionen_proc,speichere_positionen_sys,speichere_positionen_temp,speichere_positionen_cpu,speichere_positionen_host
from config import DISK_DATA,RAM_DATA,UPTIME_DATA,DOCKER_DATA,TEMP_DATA,JOURNAL_DATA,MEM_DATA,CPU_DATA,HOST_DATA,COUNTER_DATA
from Systemtracker.systemabfrage import systemabruf,systemabruf_pipe
from befehle import BEFEHLSKETTE,BEFEHLSKETTE_PIPE


print(systemabruf(BEFEHLSKETTE))
print(systemabruf_pipe(BEFEHLSKETTE_PIPE))



speichere_positionen(COUNTER_DATA,opener(DISK_DATA),lade_hostname(HOST_DATA))
speichere_positionen_ram(COUNTER_DATA,opener(RAM_DATA),lade_hostname(HOST_DATA))
speichere_positionen_sys(COUNTER_DATA,opener(UPTIME_DATA),lade_hostname(HOST_DATA))
speichere_positionen_docker(COUNTER_DATA,opener(DOCKER_DATA),lade_hostname(HOST_DATA))
speichere_positionen_temp(COUNTER_DATA,opener(TEMP_DATA),lade_hostname(HOST_DATA))
speichere_positionen_proc(COUNTER_DATA,opener(MEM_DATA),lade_hostname(HOST_DATA))
speichere_positionen_cpu(COUNTER_DATA,opener(CPU_DATA),lade_hostname(HOST_DATA))
speichere_positionen_host(COUNTER_DATA,opener(HOST_DATA),lade_hostname(HOST_DATA))
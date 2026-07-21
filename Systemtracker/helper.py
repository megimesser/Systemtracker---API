import json
import re



def df(lines,path):
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

    with open(path, "w") as f:
        json.dump(entries, f, indent=4)
    


def free(lines,path):
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

    with open(path, "w") as f:
        json.dump(entries, f, indent=4)



def uptime(lines,path):
    print(lines)

    entries = []

                
    for line in lines:
        parts = line.split(',')


        #print(parts[1])

        entries.append({
            "uptime": parts[0] + parts[1],
            "users": parts[2],
            "load_averages": parts[3]
                    })

    with open(path, "w") as f:
        json.dump(entries, f, indent=4)

    
def docker_ps(lines,path):
    muster = [1-9]
    entries = []
    match = re.search(line,muster)

    for line in lines[1:]:
        parts = line.split()
        #parts = line.strip()
        #print(line)
        print(parts)
        

        if parts 
                    
        entries.append({
            "container": parts[1],
            "runtime": parts[3],
            "status": parts[4]
            })

    #print(entries)

    with open(path,"w") as f:
            json.dump(entries,f,indent=4)



def temp(lines,path):
    entries = []

    for line in lines:
        parts = line.split()
        temp = parts[5:]
                     
        entries.append({
            "temp": parts[0],
            })

    with open(path,"w") as f:
            json.dump(entries,f,indent=4)
    

def journal(lines,path):
    entries = []

    for line in lines:
        #parts = line.split()
        #temp = parts[5:]
        #print(line)
        entries.append(line)
    

    with open(path,"w") as f:
            json.dump(entries,f,indent=4)




def process_mem(lines,path):
    entries = []

    for line in lines[1:]:
        line = line.split()
        
        #parts = lines.split()
        #print(line)
        

        entries.append({
            "User" : line[0],
            "PID" : line[1],
            "%MEM" : line[3]
        })
    
    with open(path,"w") as f:
            json.dump(entries,f,indent=4)



def process_cpu(lines,path):
    entries = []

    for line in lines[1:]:
        line = line.split()
        
        #parts = lines.split()
        #print(line)
        #print("pipeline")
        

        entries.append({
            "User" : line[0],
            "PID" : line[1],
            "%CPU" : line[2]
        })
    
    with open(path,"w") as f:
            json.dump(entries,f,indent=4)


import json



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


        print(parts[1])

        entries.append({
            "uptime": parts[0] + parts[1],
            "users": parts[2],
            "load_averages": parts[3]
                    })

    with open(path, "w") as f:
        json.dump(entries, f, indent=4)

    
def docker_ps(lines,path):
    entries = []

    for line in lines:
        parts = line.split()
                    
        entries.append({
            "Container Image": parts[0],
            "Runtime": parts[3]
            })

                
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
    print("match")
    entries = ""

    for line in lines:
        #parts = line.split()
        #temp = parts[5:]
        entries += f"\nline\n"
    

    with open(path,"w") as f:
        f.write(entries)





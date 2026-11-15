import json
import os 
from config import DISK_DATA

def remover(data):
    try:
        with open (data, "w") as f:
            json.dump(f,indent=4, ensure_ascii=False)
    except json.JSONDecodeError as err:
        print(err)
        raise
    except TypeError as err_t:
        print(err_t)




if __name__ == "__main__":
    remover(DISK_DATA)
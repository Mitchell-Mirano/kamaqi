import json
from pathlib import Path

def read_project_file():
    with open("kamaqi.json",mode="r") as f:
        data=json.load(f)
        f.close()
    
    return data

def save_project_file(data:dict):

    with open("kamaqi.json", "w") as outfile:
        json.dump(data, outfile,indent=4)
        outfile.close()

def add_kamaqi_file(path:Path,data:dict):

    with open(path, "w") as outfile:
        json.dump(data, outfile)
        outfile.close()
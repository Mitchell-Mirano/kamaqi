import json
from pathlib import Path

def read_project_file():
    with open("kamaqi/settings.json",mode="r") as f:
        data=json.load(f)
        f.close()
    
    return data

def save_project_file(data:dict):

    with open("kamaqi/settings.json", "w") as outfile:
        json.dump(data, outfile)
        outfile.close()

def create_empty_file(path:Path):

    with open(path, "w") as outfile:
        outfile.close()

def read_template_file(path:Path)->str:
    
    with open(path, "r") as outfile:
        text = outfile.read()
        outfile.close()

    return text

def add_template_file(path:Path,data:str):

    with open(path, "w") as outfile:
        outfile.write(data)
        outfile.close()
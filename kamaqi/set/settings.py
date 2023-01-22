import typer
import os
import json
from pathlib import Path
from kamaqi.utils.files import read_project_file, save_project_file
from kamaqi.app.settings import APP_NAME
from rich import print

app=typer.Typer()

@app.command(name="project_path")
def set_project_path(project_path:Path):

    if not Path(project_path).exists():
        os.mkdir(project_path)

    data={
        "project_path":f"{str(project_path)}",
        "apps":[],
        "db":{}
    }
    
    with open(f"{str(project_path)}/km_settings.json", "w") as outfile:
        json.dump(data, outfile)
        outfile.close()

@app.command(name="db_conection")
def set_db_conection(user:str=typer.Option(...,prompt=True),
                     password:str=typer.Option(...,prompt=True,confirmation_prompt=True, hide_input=True),
                     host:str=typer.Option(...,prompt=True),
                     port:str=typer.Option(...,prompt=True),
                     name:str=typer.Option(...,prompt=True)):

    db_data={"user":user, 
             "password":password,
             "host":host,
             "port":port,
             "name":name}

    project_file=read_project_file()
    project_file["db"]=db_data
    save_project_file(project_file)


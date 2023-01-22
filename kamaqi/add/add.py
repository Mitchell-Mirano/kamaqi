import os
from typer import Typer
from rich import print
from typing import List

from kamaqi.utils.files import (read_project_file,
                         save_project_file)

app=Typer()

@app.command(name="app")
def create_app(app_name:str):

    project_data=read_project_file()

    if app_name in project_data["apps"]:
        print(f"App {app_name} already exists")
    else:
        project_data["apps"].append(app_name)

    save_project_file(project_data)

@app.command(name="apps")
def create_apps(apps:List[str]):

    project_data=read_project_file()

    for app_name in apps:
        if app_name in project_data["apps"]:
            print(f"App {app_name} already exists")
        else:
            project_data["apps"].append(app_name)
    
    save_project_file(project_data)




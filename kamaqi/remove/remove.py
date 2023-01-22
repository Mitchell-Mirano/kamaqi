from typer import Typer
from typing import List
from kamaqi.utils.files import read_project_file, save_project_file


app=Typer()

@app.command(name="app")
def remove_app(app_name:str):

    project_data=read_project_file()

    if app_name not in project_data["apps"]:
        print(f"App {app_name} not found")
    else:
        project_data["apps"].remove(app_name)

    save_project_file(project_data)

@app.command(name="apps")
def remove_apps(apps:List[str]):

    project_data=read_project_file()

    for app_name in apps:
        if app_name not in project_data["apps"]:
            print(f"App {app_name} not found")
        else:
            project_data["apps"].remove(app_name)
    
    save_project_file(project_data)

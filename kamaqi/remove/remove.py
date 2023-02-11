from typer import Typer
from typing import List
from kamaqi.utils.files import read_project_file, save_project_file


app=Typer(help="Remove your apps")

@app.command(name="app",
             help="Remove an app from your project")
def remove_app(app_name:str):

    project_data=read_project_file()

    if app_name not in project_data["apps"].keys():
        print(f"App {app_name} not found")
    else:
        del project_data["apps"][app_name]
    save_project_file(project_data)

@app.command(name="apps",
             help="Remove multiple apps from your project")
def remove_apps(apps:List[str]):

    project_data=read_project_file()

    for app_name in apps:
        if app_name not in project_data["apps"].keys():
            print(f"App {app_name} not found")
        else:
            del project_data["apps"][app_name]
    
    save_project_file(project_data)

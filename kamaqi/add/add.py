import os
from typer import Typer
from rich import print
from typing import List

from kamaqi.utils.files import read_project_file,save_project_file

app=Typer(help="Add apps to your project")

@app.command(name="app",
             help="Add an app to your project")
def create_app(app_name:str):

    project_data=read_project_file()
    project_apps_names=project_data["apps"].keys()

    if app_name in project_apps_names:
        print(f"App {app_name} already exists")
    else:
        project_data["apps"][app_name] = {"status":"added"}

    save_project_file(project_data)

@app.command(name="apps",
            help="Add multiple apps to your project")
def create_apps(apps:List[str]):

    project_data=read_project_file()
    project_apps_names=project_data["apps"].keys()

    for app_name in apps:
        if app_name in project_apps_names:
            print(f"App {app_name} already exists")
        else:
             project_data["apps"][app_name] = {"status":"added"}
    
    save_project_file(project_data)

@app.command(name="dep",
            help="Add a python dependency")
def add_python_dependency(dependency:str):
    
    project_data=read_project_file()
    project_type=project_data["project_type"]
    project_name=project_data["project_name"]

    if project_type == "normal":
        os.system(f". ./env/bin/activate && pip install {dependency}")
        os.system(f". ./env/bin/activate && pip freeze > requirements.txt")

    if project_type == "docker":
        os.system(f". ./env/bin/activate && pip install {dependency}")
        os.system(f"docker-compose exec {project_name} pip install {dependency}")
        os.system(f"docker-compose exec {project_name} pip freeze > requirements.txt")
  





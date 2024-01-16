import os
from typer import Typer
from rich import print
from typing import List

from kamaqi.utils.files import read_project_file,save_project_file

app=Typer(help="Add apps and python deps")

@app.command(name="app",
             help="Add an app")
def create_app(app_name:str):

    app_name = app_name.lower().strip()

    project_data=read_project_file()
    project_apps_names=project_data["apps"].keys()

    if app_name in project_apps_names:
        print(f"App {app_name} already exists")
    elif not app_name.endswith("s"):
        print(f"App {app_name} must end with 's', Kamaqi wait app names in plural form")
    else:
        project_data["apps"][app_name] = {"status":"added"}

    save_project_file(project_data)

@app.command(name="apps",
             help="Add multiple apps")
def create_apps(apps:List[str]):
    
    apps = [app.lower().strip() for app in apps]

    project_data=read_project_file()
    project_apps_names=project_data["apps"].keys()

    for app_name in apps:
        if app_name in project_apps_names:
            print(f"App {app_name} already exists")
        elif not app_name.endswith("s"):
            print(f"App {app_name} must end with 's', Kamaqi wait app names in plural form")
        else:
             project_data["apps"][app_name] = {"status":"added"}
    
    save_project_file(project_data)

@app.command(name="dep",
            help="Add a python dep")
def add_dep(dep:str):
    
    project_data=read_project_file()
    project_type=project_data["project_type"]
    project_name=project_data["project_name"]

    if project_type == "normal":
        os.system(f". ./env/bin/activate && pip install {dep}")
        os.system(f". ./env/bin/activate && pip freeze > requirements.txt")

    if project_type == "docker":
        os.system(f"docker-compose exec {project_name} pip3 install {dep}")
        os.system(f"docker-compose exec {project_name} pip3 freeze > requirements.txt")

@app.command(name="deps",
            help="Add a multiple python deps")
def add_deps(deps_list:List[str]):
    
    project_data=read_project_file()
    project_type=project_data["project_type"]
    project_name=project_data["project_name"]

    deps_text =" ".join(deps_list)

    if project_type == "normal":
        os.system(f". ./env/bin/activate && pip install {deps_text}")
        os.system(f". ./env/bin/activate && pip freeze > requirements.txt")

    if project_type == "docker":
        os.system(f"docker-compose exec {project_name} pip3 install {deps_text}")
        os.system(f"docker-compose exec {project_name} pip3 freeze > requirements.txt")
  





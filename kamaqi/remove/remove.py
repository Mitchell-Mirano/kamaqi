import os
from pathlib import Path
from typer import Typer
from typing import List
from kamaqi.utils.files import read_project_file, save_project_file


app=Typer(help="Remove apps and python deps")

@app.command(name="app",
             help="Remove an app")
def remove_app(app_name:str):

    project_data=read_project_file()

    if app_name not in project_data["apps"].keys():
        print(f"App {app_name} not found")
    else:
        del project_data["apps"][app_name]
    save_project_file(project_data)

@app.command(name="apps",
             help="Remove multiple apps")
def remove_apps(apps:List[str]):

    project_data=read_project_file()

    for app_name in apps:
        if app_name not in project_data["apps"].keys():
            print(f"App {app_name} not found")
        else:
            del project_data["apps"][app_name]
    
    save_project_file(project_data)

@app.command(name="dep",
            help="Romeve a python dep")
def remove_dep(dep:str):
    project_data=read_project_file()
    proyect_type = project_data["project_type"]
    project_name = project_data["project_name"]

    if proyect_type == "normal":
        if os.name == "posix":
            env_path = Path("./env/bin/activate").resolve()
            os.system(f". {str(env_path)} && pip uninstall {dep}")
            os.system(f". {str(env_path)} && pip freeze > requirements.txt")
        if os.name == "nt":
            env_path = Path("./env/Scripts/activate").resolve()
            os.system(f"{str(env_path)} && pip uninstall {dep}")
            os.system(f"{str(env_path)} && pip freeze > requirements.txt")
    
    if proyect_type == "docker":
        os.system(f"docker-compose exec {project_name} pip3 uninstall {dep}")
        os.system(f"docker-compose exec {project_name} pip3 uninstall > requirements.txt")

@app.command(name="deps",
            help="Remove  multiple python deps")
def add_deps(deps_list:List[str]):
    
    project_data=read_project_file()
    project_type=project_data["project_type"]
    project_name=project_data["project_name"]

    deps_text =" ".join(deps_list)

    if project_type == "normal":
        if os.name == "posix":
            env_path = Path("./env/bin/activate").resolve()
            os.system(f". {str(env_path)} && pip uninstall {deps_text}")
            os.system(f". {str(env_path)} && pip freeze > requirements.txt")
        if os.name == "nt":
            env_path = Path("./env/Scripts/activate").resolve()
            os.system(f"{str(env_path)} && pip uninstall {deps_text}")
            os.system(f"{str(env_path)} && pip freeze > requirements.txt")

    if project_type == "docker":
        os.system(f"docker-compose exec {project_name} pip3 uninstall {deps_text}")
        os.system(f"docker-compose exec {project_name} pip3 freeze > requirements.txt")

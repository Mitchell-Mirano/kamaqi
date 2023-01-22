from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from kamaqi.utils.files import read_project_file,save_project_file

def add_project_path(path:Path):
    data=read_project_file()
    data["project_path"]=str(path)
    save_project_file(data)

def get_project_path():
    data=read_project_file()
    return data["project_path"]

def add_app_to_project_config(app_name:str):

    data=read_project_file()
    if data["apps"]:
        data["apps"].append(app_name)
    else:
        data["apps"]=[app_name]
    save_project_file(data)

def get_project_apps():
    data=read_project_file()
    return data["apps"]

def update_project_main_apps():

    environment = Environment(loader=FileSystemLoader("kamaqi/templates"))
    template = environment.get_template("main.txt")
    project_apps=get_project_apps()
    content = template.render(apps=project_apps)

    project_dir=get_project_path()

    with open(f"{project_dir}/main.py", mode="w", encoding="utf-8") as main_file:
        main_file.write(content)
        print(f"update main")
        main_file.close()
    




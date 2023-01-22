import os 
import typer
from jinja2 import Environment, FileSystemLoader
from kamaqi.utils.functions import get_project_path
from kamaqi.utils.files import add_template_file, read_template_file,read_project_file


app=typer.Typer()


@app.command(name="init_files")
def create_init_files():

    project_path=get_project_path()
    environment = Environment(loader=FileSystemLoader("kamaqi/templates"))


    os.mkdir(f"{project_path}/app/")

    template = environment.get_template("router.txt")
    app_router_text=template.render(app="app")
    add_template_file(f"{project_path}/app/router.py",app_router_text)

    template = environment.get_template("schemas.txt")
    app_schemas_text=template.render(app="app")
    add_template_file(f"{project_path}/app/schemas.py",app_schemas_text)
    

    settings_text=read_template_file("kamaqi/templates/app_settings.txt")
    add_template_file(f"{project_path}/app/settings.py",settings_text)


    os.mkdir(f"{project_path}/database/")
    db_text=read_template_file("kamaqi/templates/database.txt")
    add_template_file(f"{project_path}/database/database.py",db_text)

    env_text=read_template_file("kamaqi/templates/env.txt")
    add_template_file(f"{project_path}/.env",env_text)

@app.command(name="apps")
def create_apps():
    environment = Environment(loader=FileSystemLoader("kamaqi/templates"))

    project_file = read_project_file()

    project_path = project_file["project_path"]
    apps_list=project_file["apps"]
    
    for app in apps_list:
        os.mkdir(f"{project_path}/{app}/")

        template = environment.get_template("router.txt")
        app_router_text=template.render(app=app)
        add_template_file(f"{project_path}/{app}/router.py",app_router_text)

        template = environment.get_template("schemas.txt")
        app_schemas_text=template.render(app=app)
        add_template_file(f"{project_path}/{app}/schemas.py",app_schemas_text)
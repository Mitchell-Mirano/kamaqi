import os 
import typer
from pathlib import Path
from kamaqi.utils.files import read_project_file
from kamaqi.utils.files import add_kamaqi_file
from kamaqi.templates.get_templates import get_app_template
from kamaqi.templates.get_templates import get_project_template
from kamaqi.templates.get_templates import get_database_template


app=typer.Typer(help="Create files for your apps")

@app.command(name="apps",
             help="Create files for multiple apps")
def upgrade_apps():

    project_data = read_project_file()
    project_path = Path(project_data["project_path"])
    project_type = project_data["project_type"]
    apps_list=[]
    
    for app, data in project_data["apps"].items():
        if data["status"] == "added":
            apps_list.append(app)

    base_dir_files: Path
    if project_type=="normal":
        base_dir_files=project_path.resolve()
    else:
        base_dir_files=project_path.joinpath("src").resolve()

    for app_name in apps_list:
        base_dir_files.joinpath(app_name).resolve().mkdir()

        for template_name in ["router", "schemas","crud"]:
            template = get_app_template(template_name)
            template_text=template.render(app=app_name[:-1])
            file_path = base_dir_files.joinpath(f"{app_name}/{template_name}.py").resolve()
            file_path.write_text(template_text,encoding="utf-8")
            
    template = get_project_template("main")
    template_text=template.render(**project_data)
    file_path = base_dir_files.joinpath("main.py").resolve()
    file_path.write_text(template_text,encoding="utf-8")

    new_apps = [app[:-1] for app in apps_list]

    template = get_database_template("model")
    models_path = base_dir_files.joinpath("database/models.py").resolve()
    models_text = models_path.read_text()

    for app in new_apps:
        template_text=template.render(app=app)
        models_text+="\n\n"+ template_text
    
    models_path.write_text(models_text,encoding="utf-8")

    for app_name in apps_list:
        project_data["apps"][app_name]["status"]="upgraded"

    project_file_path = project_path.joinpath("kamaqi.json").resolve()

    add_kamaqi_file(project_file_path,project_data)


@app.command(name="tables",
             help="Upgrade your database tables")
def upgrade_tables(message:str=typer.Option(...,"--message","-m")):

    project_data:dict = read_project_file()
    project_name:str = project_data["project_name"]

    if project_data["project_type"] == "normal":
        os.system(f"""alembic revision --autogenerate -m"{message}" """)
        os.system("alembic upgrade head")
        #os.system(f"alembic revision --autogenerat -m{message}")

    if project_data["project_type"] == "docker":
        os.system(f"""docker-compose exec {project_name} alembic revision --autogenerate -m"{message}" """)
        os.system(f"docker-compose exec {project_name} alembic upgrade head")

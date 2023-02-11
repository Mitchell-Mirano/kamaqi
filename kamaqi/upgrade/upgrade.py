import os 
import typer
from pathlib import Path
from kamaqi.utils.files import read_project_file
from kamaqi.utils.files import add_kamaqi_file
from kamaqi.app.settings import get_kamaqi_template


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
        project_path.joinpath(app_name).resolve().mkdir()

        for template_name in ["router", "schemas","crud"]:
            template = get_kamaqi_template(template_name)
            template_text=template.render(app=app_name[:-1])
            file_path = base_dir_files.joinpath(f"{app_name}/{template_name}.py").resolve()
            file_path.write_text(template_text,encoding="utf-8")
            
    template = get_kamaqi_template("main")
    template_text=template.render(**project_data)
    file_path = base_dir_files.joinpath("main.py").resolve()
    file_path.write_text(template_text,encoding="utf-8")

    new_apps = [app[:-1] for app in apps_list]

    template = get_kamaqi_template("model")
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
    
    

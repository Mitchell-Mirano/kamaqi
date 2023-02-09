import os 
import typer

from kamaqi.utils.files import add_template_file
from kamaqi.utils.files import read_project_file
from kamaqi.utils.files import add_kamaqi_file
from kamaqi.app.settings import get_kamaqi_template


app=typer.Typer(help="Create files for your apps")

@app.command(name="apps",
             help="Create files for multiple apps")
def upgrade_apps():

    project_data = read_project_file()
    project_path = project_data["project_path"]
    project_type = project_data["project_type"]
    apps_list=[]
    
    for app, data in project_data["apps"].items():
        if data["status"] == "added":
            apps_list.append(app)

    base_dir_files=""
    if project_type=="normal":
        base_dir_files=f"{project_path}"
    else:
        base_dir_files=f"{project_path}/src"

    for app_name in apps_list:
        os.mkdir(f"{base_dir_files}/{app_name}/")

        for template_name in ["router", "schemas","crud"]:
            template = get_kamaqi_template(template_name)
            template_text=template.render(app=app_name[:-1])
            add_template_file(f"{base_dir_files}/{app_name}/{template_name}.py",template_text)
            
    template = get_kamaqi_template("main")
    template_text=template.render(**project_data)
    add_template_file(f"{base_dir_files}/main.py",template_text)

    new_apps = [app[:-1] for app in apps_list]

    template = get_kamaqi_template("model")
  
    with open(f"{base_dir_files}/database/models.py",mode="r") as f:
        models_text = f.read()
        f.close()

    for app in new_apps:
        template_text=template.render(app=app)
        models_text+="\n\n"+ template_text
    
    add_template_file(f"{base_dir_files}/database/models.py",models_text)

    for app_name in apps_list:
        project_data["apps"][app_name]["status"]="upgraded"

    add_kamaqi_file(f"{str(project_path)}/kamaqi.json",project_data)
    
    

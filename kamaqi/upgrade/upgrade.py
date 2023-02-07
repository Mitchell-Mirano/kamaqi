import os 
import typer

from kamaqi.utils.files import add_template_file,read_project_file
from kamaqi.app.settings import get_kamaqi_template


app=typer.Typer(help="Create files for your apps")


@app.command(name="app",
             help="Create files for an app")
def upgrade_app(app_name:str):

    project_file = read_project_file()
    project_path = project_file["project_path"]
    project_name = project_file["project_name"]
    project_type = project_file["project_type"]
    apps_list=project_file["apps"]
    apps_list.remove(project_name)

    base_dir_files=""
    if project_type=="normal":
        base_dir_files=f"{project_path}"
    else:
        base_dir_files=f"{project_path}/src"

    os.mkdir(f"{base_dir_files}/{app_name}/")

    for template_name in ["router", "schemas","crud"]:
        template = get_kamaqi_template(template_name)
        template_text=template.render(app=app_name[:-1])
        add_template_file(f"{base_dir_files}/{app_name}/{template_name}.py",template_text)
    
    
    template = get_kamaqi_template("main")
    template_text=template.render(**project_file)
    add_template_file(f"{base_dir_files}/main.py",template_text)

    new_apps = [app[:-1] for app in apps_list]

    template = get_kamaqi_template("models")
    template_text=template.render(apps=new_apps)
    add_template_file(f"{base_dir_files}/database/models.py",template_text)
 

@app.command(name="apps",
             help="Create files for multiple apps")
def upgrade_apps():

    project_file = read_project_file()
    project_path = project_file["project_path"]
    project_name = project_file["project_name"]
    project_type = project_file["project_type"]
    apps_list=project_file["apps"]
    apps_list.remove(project_name)

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
    template_text=template.render(**project_file)
    add_template_file(f"{base_dir_files}/main.py",template_text)

    new_apps = [app[:-1] for app in apps_list]

    template = get_kamaqi_template("models")
    template_text=template.render(apps=new_apps)
    add_template_file(f"{base_dir_files}/database/models.py",template_text)
    

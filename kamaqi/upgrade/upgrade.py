import os 
import typer

from kamaqi.utils.files import add_template_file,read_project_file
from kamaqi.app.settings import get_kamaqi_template


app=typer.Typer()


@app.command(name="app")
def upgrade_app(app_name:str):

    project_file = read_project_file()
    project_path = project_file["project_path"]
    project_name = project_file["project_name"]
    apps_list=project_file["apps"]
    apps_list.remove(project_name)

    os.mkdir(f"{project_path}/{app_name}/") 
    for template_name in ["router", "schemas","crud"]:
        template = get_kamaqi_template(template_name)
        template_text=template.render(app=app_name[:-1])
        add_template_file(f"{project_path}/{app_name}/{template_name}.py",template_text)
    
    
    template = get_kamaqi_template("main")
    main_data={
        "project_name": project_name,
        "apps":apps_list
    }
    template_text=template.render(**main_data)
    add_template_file(f"{project_path}/main.py",template_text)

    new_apps = [app[:-1] for app in apps_list]

    template = get_kamaqi_template("models")
    template_text=template.render(apps=new_apps)
    add_template_file(f"{project_path}/database/models.py",template_text)


@app.command(name="apps")
def upgrade_apps():

    project_file = read_project_file()
    project_path = project_file["project_path"]
    project_name = project_file["project_name"]
    apps_list=project_file["apps"]
    apps_list.remove(project_name)

    for app in apps_list:
       os.mkdir(f"{project_path}/{app}/") 
#
       for template_name in ["router", "schemas","crud"]:
           template = get_kamaqi_template(template_name)
           template_text=template.render(app=app[:-1])
           add_template_file(f"{project_path}/{app}/{template_name}.py",template_text)

    template = get_kamaqi_template("main")
    main_data={
        "project_name": project_name,
        "apps":apps_list
    }
    template_text=template.render(**main_data)
    add_template_file(f"{project_path}/main.py",template_text)

    new_apps = [app[:-1] for app in apps_list]

    template = get_kamaqi_template("models")
    template_text=template.render(apps=new_apps)
    add_template_file(f"{project_path}/database/models.py",template_text)
    

import os 
from rich import print
import json
from pathlib import Path
from typer import Typer
import subprocess
from kamaqi.app.settings import get_kamaqi_template
from kamaqi.utils.files import add_template_file
app = Typer()

@app.command(name="project")
def set_project_path(project_name:str):

    project_path = Path(f"{os.getcwd()}/{project_name}")
    
    if not project_path.exists():
        os.mkdir(project_path)
        os.mkdir(f"{project_path}/{project_name}")
        os.mkdir(f"{project_path}/database")

    open_ssl= subprocess.run(['openssl', 'rand','-hex','32'], stdout=subprocess.PIPE)
    open_ssl=open_ssl.stdout.decode('utf-8').split('\n')[0]

    env_data={
        "project_name":project_name,
        "open_ssl":open_ssl
    }
    env_template=get_kamaqi_template("env")
    env_text= env_template.render(**env_data)
  
    with open(f"{str(project_path)}/.env", "w") as outfile:
        outfile.write(env_text)
        outfile.close()


    project_templates=["router", "settings", "schemas", "exceptions","database"]

    for template_name in project_templates:
        template=get_kamaqi_template(f"app_{template_name}")
        template_text=template.render(app=project_name)
        if template_name=="database":
            add_template_file(f"{project_path}/database/{template_name}.py",template_text)
        else:
            add_template_file(f"{project_path}/{project_name}/{template_name}.py",template_text)

    template=get_kamaqi_template("requirements")
    template_text=template.render(app=project_name)
    add_template_file(f"{project_path}/requirements.txt",template_text)

    template=get_kamaqi_template("main")
    main_data={
        "project_name":project_name,
        "apps":[]
    }
    template_text=template.render(**main_data)
    add_template_file(f"{project_path}/main.py",template_text)
        

    data={
        "project_path":f"{str(project_path)}",
        "project_name":project_name,
        "apps":[project_name],
        "db":"postgresql",
    }
    
    with open(f"{str(project_path)}/kamaqi.json", "w") as outfile:
        json.dump(data, outfile)
        outfile.close()

    os.chdir(project_path)
    os.system("python3 -m venv env")
    os.system("source env/bin/activate")
    os.system("pip install -r requirements.txt")
    
    
    
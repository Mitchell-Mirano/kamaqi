import os 
import subprocess
from rich import print
from typer import Typer
from pathlib import Path
from kamaqi.app.settings import get_kamaqi_template
from kamaqi.utils.files import add_template_file
from kamaqi.utils.files import add_kamaqi_file
from kamaqi.app.settings import choose_project_type
from kamaqi.app.settings import choose_database_type

app = Typer(help="Init and configure your project")

@app.command(name="project",
            help="Init your project")
def set_project_path(project_name:str):

    project_path = Path(f"{os.getcwd()}/{project_name}")
    project_type=choose_project_type()
    database_type=choose_database_type(project_type)

    secret_key= subprocess.run(['openssl', 'rand','-hex','32'], stdout=subprocess.PIPE)
    secret_key=secret_key.stdout.decode('utf-8').split('\n')[0]

    project_data={
        "project_path": str(project_path),
        "project_name":project_name,
        "project_type":project_type,
        "database_type":database_type,
        "secret_key":secret_key,
        "apps":{project_name:{"status":"added"}}
        }
    
    base_dir_files=""

    os.mkdir(project_path)
    if project_type == 'normal': 
        os.mkdir(f"{project_path}/{project_name}/")
        os.mkdir(f"{project_path}/database/")
        base_dir_files=project_path
    else:
        os.mkdir(f"{project_path}/src/")
        os.mkdir(f"{project_path}/src/{project_name}/")
        os.mkdir(f"{project_path}/src/database/")
        base_dir_files=f"{project_path}/src"

    env_template=get_kamaqi_template("env")
    env_text= env_template.render(**project_data)
    env_path=f"{base_dir_files}/.env"
    add_template_file(env_path, env_text)

    project_templates=["auth","router", "settings", "schemas", "exceptions","database"]

    for template_name in project_templates:
        template=get_kamaqi_template(f"app_{template_name}")
        template_text=template.render(**project_data)

        if template_name=="database":
            add_template_file(f"{base_dir_files}/database/{template_name}.py",template_text)
        else:
            add_template_file(f"{base_dir_files}/{project_name}/{template_name}.py",template_text)
          

    template=get_kamaqi_template("models")
    template_text=template.render(**project_data)
    add_template_file(f"{base_dir_files}/database/models.py",template_text)

    template=get_kamaqi_template("requirements")
    template_text=template.render(**project_data)
    template_text=template_text.replace("\n\n","\n")
    template_text=template_text.replace("\n\n","\n")
    add_template_file(f"{project_path}/requirements.txt",template_text)

    
    template=get_kamaqi_template("main")
    template_text=template.render(**project_data)
    add_template_file(f"{base_dir_files}/main.py",template_text)
  
    project_data["apps"][project_name]={"status":"upgraded"}
    del project_data["secret_key"]
    add_kamaqi_file(f"{str(project_path)}/kamaqi.json",project_data)

    os.chdir(project_path)

    if project_type=="docker":
        print("Creating docker image...")
        template=get_kamaqi_template("docker_file")
        template_text=template.render(**project_data)
        add_template_file(f"{project_path}/Dockerfile",template_text)

        template=get_kamaqi_template("docker_compose")
        template_text=template.render(**project_data)
        add_template_file(f"{project_path}/docker-compose.yaml",template_text)

        try:
            os.system("docker-compose stop")
            os.system("docker container prune --force")
            os.system("docker system prune --force")
            os.system(f"docker image rm {project_name.lower()}_image:latest")
        except:
            pass
        os.system(f"docker build  -t {project_name.lower()}_image .")

    if project_type=="normal":
        print(" Creating  a virtual environment ...")
        os.system("python3 -m venv env")
        os.system("source env/bin/activate")
        os.system("pip install -r requirements.txt")

    print(" Yor project was created successfully")
        
    

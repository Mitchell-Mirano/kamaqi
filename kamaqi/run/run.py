import os
from typer import Typer
from kamaqi.utils.files import read_project_file

app = Typer(help="Run your project")

@app.command(name="project",
             help="Run your project")
def run_project():

    project_file = read_project_file()
    project_name = project_file["project_name"]

    if project_file["project_type"] == "normal":
        
        if os.name=="posix":
            os.system("source env/bin/activate")

        if os.name=="nt":
            os.system(f".\env\Scripts\\activate")

        os.system("uvicorn main:app --reload")

    if  project_file["project_type"] == "docker":
        os.system(f"docker-compose up -d && docker-compose logs -f {project_name}")

    
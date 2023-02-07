from typer import Typer
import os
from kamaqi.utils.files import read_project_file

app = Typer()

@app.command(name="project")
def run_project():

    project_file = read_project_file()
    project_name = project_file["project_name"]

    if project_file["project_type"] == "normal":
        os.system("source env/bin/activate")
        os.system("uvicorn main:app --reload")

    if  project_file["project_type"] == "docker":
        os.system(f"docker-compose up -d && docker-compose logs -f {project_name}")

    
import os
from typer import Typer
from pathlib import Path
from kamaqi.utils.files import read_project_file

app = Typer(help="Run your project")

@app.command(name="project",
             help="Run your project")
def run_project():

    project_file = read_project_file()
    project_name = project_file["project_name"]

    if project_file["project_type"] == "normal":
        
        env_path: Path
        
        if os.name == "posix":
            env_path = Path("env/bin/activate").resolve()
            os.system(f". {str(env_path)} && uvicorn main:app --reload")
        
        if os.name == "nt":
            env_path = Path("env/Scripts/activate").resolve()
            os.system(f"{str(env_path)} && uvicorn main:app --reload")

    if  project_file["project_type"] == "docker":
        os.system(f"docker-compose up -d && docker-compose logs -f {project_name}")

    
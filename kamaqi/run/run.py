import os
from rich import print
import typer
from typing import Optional
from pathlib import Path
from kamaqi.utils.files import read_project_file

app = typer.Typer(help="Run your project")

@app.command(name="project",
             help="Run your project")
def run_project(build: Optional[bool] = typer.Option(False, "--build","-b",help="Rebuild the project image")):

    project_file = read_project_file()
    project_name = project_file["project_name"]
    project_type = project_file["project_type"]

    if build and project_type == "normal":
        print("You can't build in normal projects")
        typer.Exit()

    if project_file["project_type"] == "normal":
        env_path: Path
        if os.name == "posix":
            env_path = Path("env/bin/activate").resolve()
            os.system(f". {str(env_path)} && uvicorn main:app --reload")
        
        if os.name == "nt":
            env_path = Path("env/Scripts/activate").resolve()
            os.system(f"{str(env_path)} && uvicorn main:app --reload")

    if  project_file["project_type"] == "docker":
        if build:
            os.system(f"sudo docker build -t {project_name.lower()}_image .")
        os.system(f"docker-compose up -d && docker-compose logs -f {project_name}")

    
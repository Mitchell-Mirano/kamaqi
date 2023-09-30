import os
import typer
from kamaqi.utils.files import read_project_file
from pathlib import Path

app=typer.Typer(help="Update your database")

@app.command(name="tables",
             help="Upgrade your database tables")
def upgrade_tables(message:str=typer.Option(...,"--message","-m")):

    project_data:dict = read_project_file()
    project_name:str = project_data["project_name"]

    if project_data["project_type"] == "normal":
        env_path: Path
        if os.name == "posix":
            env_path = Path("env/bin/activate").resolve()
        if os.name == "nt":
            env_path = Path("env/Scripts/activate").resolve()

        os.system(f""". {str(env_path)}  && alembic revision --autogenerate -m"{message}" """)
        os.system(f". {str(env_path)} alembic upgrade head")

    if project_data["project_type"] == "docker":
        os.system(f"""docker-compose exec {project_name} alembic revision --autogenerate -m"{message}" """)
        os.system(f"docker-compose exec {project_name} alembic upgrade head")
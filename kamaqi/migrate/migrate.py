import os
import typer
from kamaqi.utils.files import read_project_file

app=typer.Typer(help="Update your database")

@app.command(name="tables",
             help="Upgrade your database tables")
def upgrade_tables(message:str=typer.Option(...,"--message","-m")):

    project_data:dict = read_project_file()
    project_name:str = project_data["project_name"]

    if project_data["project_type"] == "normal":
        os.system(f"""alembic revision --autogenerate -m"{message}" """)
        os.system("alembic upgrade head")

    if project_data["project_type"] == "docker":
        os.system(f"""docker-compose exec {project_name} alembic revision --autogenerate -m"{message}" """)
        os.system(f"docker-compose exec {project_name} alembic upgrade head")
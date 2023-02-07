from typer import Typer
from rich import print
from kamaqi.utils.files import read_project_file

app=Typer(help="Show apps, endpoints and models")

@app.command(name="apps",
             help="Show apps and their metadata")
def list_apps():
    
    project_file = read_project_file()
    project_apps = project_file["apps"]
    for app in project_apps:
        print(f">> {app}")

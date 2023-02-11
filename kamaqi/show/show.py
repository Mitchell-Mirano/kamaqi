from typer import Typer
from rich import print
from rich.table import Table
from kamaqi.utils.files import read_project_file

app=Typer(help="Show apps, endpoints and models")

@app.command(name="apps",
             help="Show apps and their metadata")
def list_apps():

    project_file = read_project_file()
    project_apps = project_file["apps"]
    apps_table = Table("App","Status")

    for app,data in project_apps.items():
        app_status = data["status"].capitalize()
        app_name = app.capitalize()
        if app_status == "Upgraded":
            app_status = f"[bold green]{app_status}[/bold green]"
        if app_status == "Added":
            app_status = f"[bold yellow]{app_status}[/bold yellow]"
            
        apps_table.add_row(app_name,app_status)

    print(apps_table)

@app.command(name="config",
            help="Show kamaqi.json")
def show_config():
    project_file=read_project_file()
    print(project_file)

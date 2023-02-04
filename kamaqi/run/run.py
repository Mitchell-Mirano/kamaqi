from typer import Typer
import os

app = Typer()

@app.command(name="project")
def run_project():
    os.system("source env/bin/activate")
    os.system("uvicorn main:app --reload")
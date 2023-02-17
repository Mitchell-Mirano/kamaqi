import typer
from typing import Optional
from kamaqi.start import start
from kamaqi.run import run
from kamaqi.add import add
from kamaqi.show import show
from kamaqi.remove import remove
from kamaqi.upgrade import upgrade

app = typer.Typer(help="A command line app for creating Backends with FastAPI")

__version__ = "0.1.9"


def version_callback(value: bool):
    if value:
        print(f"Kamaqi version: {__version__}")
        raise typer.Exit()


@app.callback()
def main(version: Optional[bool] = typer.Option(None, "--version", callback=version_callback)):
    pass

app.add_typer(start.app, name="start")
app.add_typer(run.app, name="run")
app.add_typer(add.app, name="add")
app.add_typer(show.app, name="show")
app.add_typer(remove.app, name="remove")
app.add_typer(upgrade.app, name="upgrade")

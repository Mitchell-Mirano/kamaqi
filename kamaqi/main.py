import typer

from kamaqi.init import init
from kamaqi.run import run
from kamaqi.add import add
from kamaqi.show import show
from kamaqi.remove import remove
from kamaqi.upgrade import upgrade

app = typer.Typer()

app.add_typer(init.app,name="init")
app.add_typer(run.app,name="run")
app.add_typer(add.app,name="add")
app.add_typer(show.app,name="show")
app.add_typer(remove.app,name="remove")
app.add_typer(upgrade.app,name="upgrade")



if __name__ == "__main__":
    app()

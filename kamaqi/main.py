import typer


from kamaqi.set import settings
from kamaqi.add import add
from kamaqi.show import show
from kamaqi.remove import remove
from kamaqi.create import create

app = typer.Typer()

app.add_typer(settings.app, name="set")
app.add_typer(add.app,name="add")
app.add_typer(show.app,name="show")
app.add_typer(remove.app,name="remove")
app.add_typer(create.app,name="create")



if __name__ == "__main__":
    app()

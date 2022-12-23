import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    Awesome Kamaqi
    """


@app.command()
def shoot():
    """
    Shoot the Kamaqi
    """
    typer.echo("Shooting Kamaqi")


@app.command()
def load():
    """
    Load the Kamaqi
    """
    typer.echo("Loading Kamaqi")

if __name__ == "__main__":
    app()

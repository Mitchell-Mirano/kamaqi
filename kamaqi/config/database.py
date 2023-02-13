import os
from typer import prompt

databases={
    "1": "MySQL",
    "2": "PostgreSQL",
    "3": "SQLite"}

def choose_database_type(project_type):
    print("Setting your project")
    print("Choose an database option")

    posible_dbs=databases.copy()

    if project_type=="docker":
        del posible_dbs["3"]

    for key, vale in posible_dbs.items():
        print(f"[{key}] >> Use {vale}")

    db_option = prompt("Your option is? ")
    os.system("clear")

    return databases[db_option]

import os 
from typer import prompt

project_types={
    "1": "normal",
    "2": "docker"
    }

def choose_project_type():
    print("Setting your project")
    print("Choose an option")
    print("[1] >> Create a  normal project")
    print("[2] >> Create a project with Docker")
    project_option = prompt("Your option is? ")
    os.system("clear")

    return project_types[project_option]
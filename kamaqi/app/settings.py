import os
from typer import prompt
from jinja2 import Environment, BaseLoader
from kamaqi.templates import app_auth,app_database,app_exceptions
from kamaqi.templates import app_schemas,app_router,app_exceptions
from kamaqi.templates import main,app_settings,env,requirements
from kamaqi.templates import router,schemas,models,crud,model
from kamaqi.templates import docker_file,docker_compose

APP_NAME="kamaqi"

environment = Environment(loader=BaseLoader)

def get_kamaqi_template(template_name:str):
    
    templates_dict={
        "app_router":app_router.APP_ROUTER,
        "app_settings":app_settings.APP_SETTINGS,
        "requirements":requirements.REQUIREMENTS,
        "app_auth":app_auth.APP_AUTH,
        "app_database":app_database.APP_DATABASE,
        "app_exceptions":app_exceptions.APP_EXCEPTIONS,
        "app_schemas":app_schemas.APP_SCHEMAS,
        "main":main.MAIN,
        "env":env.ENV,
        "router":router.ROUTER,
        "schemas":schemas.SCHEMAS,
        "models":models.MODELS,
        "model":model.MODEL,
        "crud":crud.CRUD,
        "docker_file":docker_file.DOCKER_FILE,
        "docker_compose":docker_compose.DOCKER_COMPOSE,

    }
    template=environment.from_string(templates_dict[template_name])
    return template

project_types={
    "1": "normal",
    "2": "docker"}

databases={
    "1": "MySQL",
    "2": "PostgreSQL",
    "3": "SQLite"}


def choose_project_type():
    print("Setting your project")
    print("Choose an option")
    print("[1] >> Create a  normal project")
    print("[2] >> Create a project with Docker")
    project_option = prompt("Your option is? ")
    os.system("clear")

    return project_types[project_option]

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

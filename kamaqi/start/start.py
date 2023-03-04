import os
import subprocess
from rich import print
from typer import Typer
from pathlib import Path
from kamaqi.utils.files import add_kamaqi_file
from kamaqi.config.database import choose_database_type
from kamaqi.config.project import choose_project_type
from kamaqi.templates.get_templates import get_project_template
from kamaqi.templates.get_templates import get_database_template
from kamaqi.templates.get_templates import get_migration_template
from kamaqi.templates.get_templates import get_docker_template

app = Typer(help="Start and configure your project")


@app.command(name="project",
             help="Start a project")
def set_project_path(project_name: str):

    print("Setting project path ...")
    if project_name == ".":
        project_path = Path(f"{os.getcwd()}").resolve()
        project_name = Path(project_path).resolve().parts[-1]
    else:
        project_path = Path(f"{os.getcwd()}/{project_name}").resolve()

    project_type = choose_project_type()
    database_type = choose_database_type(project_type)

    secret_key = subprocess.run(['openssl', 'rand', '-hex', '32'], stdout=subprocess.PIPE)
    secret_key = secret_key.stdout.decode('utf-8').split('\n')[0]

    project_data = {
        "project_path": str(project_path),
        "project_name": project_name,
        "project_type": project_type,
        "database_type": database_type,
        "secret_key": secret_key,
        "apps": {project_name: {"status": "added"}}
    }

    print("Creating project directories...")
    base_dir_files: Path
    file_path: Path

    if not project_path.exists():
        project_path.mkdir()
    if project_type == 'normal':
        project_path.joinpath(project_name).resolve().mkdir()
        project_path.joinpath("database").resolve().mkdir()
        base_dir_files = project_path
    else:
        project_path.joinpath("src").resolve().mkdir()
        project_path.joinpath(f"src/{project_name}").resolve().mkdir()
        project_path.joinpath(f"src/database").resolve().mkdir()
        base_dir_files = project_path.joinpath("src").resolve()

    print("Setting environment variables...")
    env_template = get_project_template("env")
    env_text = env_template.render(**project_data)
    file_path = base_dir_files.joinpath(".env").resolve()
    file_path.write_text(env_text, encoding="utf-8")

    print("Creating project files...")
    project_templates = ["auth", "router", "settings", "schemas", "exceptions"]

    for template_name in project_templates:
        template = get_project_template(template_name)
        template_text = template.render(**project_data)
        file_path = base_dir_files.joinpath(f"{project_name}/{template_name}.py").resolve()
        file_path.write_text(template_text, encoding="utf-8")

    print("Setting database ...")
    database_templates = ["database", "models"]
    for template_name in database_templates:
        template = get_database_template(template_name)
        template_text = template.render(**project_data)
        file_path = base_dir_files.joinpath(f"database/{template_name}.py").resolve()
        file_path.write_text(template_text, encoding="utf-8")

    print("Setting database migrations...")
    migrations_templates = ["ini", "env", "script_py_mako"]
    base_dir_files.joinpath("migrations").resolve().mkdir()
    base_dir_files.joinpath("migrations/versions").resolve().mkdir()
    for template_name in migrations_templates:
        template = get_migration_template(template_name)
        template_text = template.render(**project_data)
        if template_name == "ini":
            file_path = base_dir_files.joinpath("alembic.ini").resolve()
        if template_name == "env":
            file_path = base_dir_files.joinpath("migrations/env.py").resolve()
        if template_name == "script_py_mako":
            file_path = base_dir_files.joinpath("migrations/script.py.mako").resolve()
        file_path.write_text(template_text, encoding="utf-8")

    print("Setting python libraries ...")
    template = get_project_template("requirements")
    template_text = template.render(**project_data)
    file_path = project_path.joinpath("requirements.txt").resolve()
    file_path.write_text(template_text, encoding="utf-8")

    template = get_project_template("main")
    template_text = template.render(**project_data)
    file_path = base_dir_files.joinpath("main.py").resolve()
    file_path.write_text(template_text, encoding="utf-8")
    
    project_data["apps"][project_name] = {"status": "upgraded"}
    del project_data["secret_key"]
    project_file_path = project_path.joinpath("kamaqi.json").resolve()
    add_kamaqi_file(project_file_path, project_data)

    os.chdir(project_path)

    if project_type == "docker":
        print("Creating a docker image...")
        template = get_docker_template("docker_file")
        template_text = template.render(**project_data)
        file_path = project_path.joinpath("Dockerfile").resolve()
        file_path.write_text(template_text, encoding="utf-8")
        template = get_docker_template("docker_compose")
        template_text = template.render(**project_data)
        file_path = project_path.joinpath("docker-compose.yaml").resolve()
        file_path.write_text(template_text, encoding="utf-8")

        try:
            os.system("docker-compose stop")
            os.system("docker container prune --force")
            os.system("docker system prune --force")
            os.system(f"docker image rm {project_name.lower()}_image:latest")
        finally:
            pass

        print("Building  your project image")
        os.system(f"docker build -t {project_name.lower()}_image .")
        os.system(f"docker run {project_name.lower()}_image pip freeze > requirements.txt")
        
    if project_type == "normal":
        print("Creating  a virtual environment ...")
        os.system("python3 -m venv env")

        env_path: Path
        print("Installing dependencies")

        if os.name == "posix":
            env_path = Path("env/bin/activate").resolve()
            os.system(f". {str(env_path)} && pip install -r requirements.txt")
            os.system(f". {str(env_path)} && pip freeze > requirements.txt")
            
        if os.name == "nt":
            env_path = Path("env/Scripts/activate").resolve()
            os.system(f"{str(env_path)} && pip install -r requirements.txt")
            os.system(f"{str(env_path)} && pip freeze > requirements.txt")

    print(" Yor project was created successfully")

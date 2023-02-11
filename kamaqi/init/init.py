import os
import subprocess
from rich import print
from typer import Typer
from pathlib import Path
from kamaqi.app.settings import get_kamaqi_template
from kamaqi.utils.files import add_kamaqi_file
from kamaqi.app.settings import choose_project_type
from kamaqi.app.settings import choose_database_type

app = Typer(help="Init and configure your project")


@app.command(name="project",
             help="Init your project")
def set_project_path(project_name: str):
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

    base_dir_files: Path

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

    env_template = get_kamaqi_template("env")
    env_text = env_template.render(**project_data)
    env_path = base_dir_files.joinpath(".env").resolve()
    env_path.write_text(env_text, encoding="utf-8")

    project_templates = ["auth", "router", "settings", "schemas", "exceptions", "database"]

    for template_name in project_templates:
        template = get_kamaqi_template(f"app_{template_name}")
        template_text = template.render(**project_data)

        file_path: Path
        if template_name == "database":
            file_path = base_dir_files.joinpath(f"database/{template_name}.py").resolve()
        else:
            file_path = base_dir_files.joinpath(f"{project_name}/{template_name}.py").resolve()
        file_path.write_text(template_text, encoding="utf-8")

    template = get_kamaqi_template("models")
    template_text = template.render(**project_data)
    file_path = base_dir_files.joinpath("database/models.py").resolve()
    file_path.write_text(template_text, encoding="utf-8")

    template = get_kamaqi_template("requirements")
    template_text = template.render(**project_data)
    file_path = project_path.joinpath("requirements.txt").resolve()
    file_path.write_text(template_text, encoding="utf-8")

    template = get_kamaqi_template("main")
    template_text = template.render(**project_data)
    file_path = base_dir_files.joinpath("main.py").resolve()
    file_path.write_text(template_text, encoding="utf-8")

    project_data["apps"][project_name] = {"status": "upgraded"}
    del project_data["secret_key"]
    project_file_path = project_path.joinpath("kamaqi.json").resolve()
    add_kamaqi_file(project_file_path,project_data)

    os.chdir(project_path)

    if project_type == "docker":
        print("Creating docker image...")
        template = get_kamaqi_template("docker_file")
        template_text = template.render(**project_data)
        file_path = project_path.joinpath("Dockerfile").resolve()
        file_path.write_text(template_text, encoding="utf-8")
        template = get_kamaqi_template("docker_compose")
        template_text = template.render(**project_data)
        file_path = project_path.joinpath("docker-compose.yaml").resolve()
        file_path.write_text(template_text, encoding="utf-8")

        try:
            os.system("docker-compose stop")
            os.system("docker container prune --force")
            os.system("docker system prune --force")
            os.system(f"docker image rm {project_name.lower()}_image:latest")
        except:
            pass
        os.system(f"docker build  -t {project_name.lower()}_image .")

    if project_type == "normal":
        print(" Creating  a virtual environment ...")
        os.system("python3 -m venv env")

        if os.name=="posix":
            os.system("source env/bin/activate")

        if os.name=="nt":
            os.system(f".\env\Scripts\\activate")

        os.system("pip install -r requirements.txt")

    print(" Yor project was created successfully")

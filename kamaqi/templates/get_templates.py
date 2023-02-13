from jinja2 import Environment, BaseLoader

from kamaqi.templates.project import project_requirements,project_env
from kamaqi.templates.project import project_auth, project_exceptions
from kamaqi.templates.project import project_schemas, project_settings
from kamaqi.templates.project import project_router,project_main

from kamaqi.templates.database import database, model,models

from kamaqi.templates.migrations import migrations_env, migrations_ini, migrations_script_py_mako

from kamaqi.templates.docker import docker_compose,docker_file

from kamaqi.templates.app import app_crud, app_router, app_schemas

environment = Environment(loader=BaseLoader)

def get_project_template(template_name:str):
    
    templates_dict={
        "requirements":project_requirements.PROJECT_REQUIREMENTS,
        "router":project_router.PROJECT_ROUTER,
        "settings":project_settings.PROJECT_SETTINGS,
        "exceptions":project_exceptions.PROJECT_EXCEPTIONS,
        "schemas":project_schemas.PROJECT_SCHEMAS,
        "auth":project_auth.PROJECT_AUTH,
        "env":project_env.PROJECT_ENV,
        "main":project_main.PROJECT_MAIN,
    }

    template=environment.from_string(templates_dict[template_name])
    return template

def get_database_template(template_name:str):
    
    templates_dict={
        "database":database.APP_DATABASE,
        "models":models.MODELS,
        "model":model.MODEL,

    }

    template=environment.from_string(templates_dict[template_name])
    return template

def get_migration_template(template_name:str):
    
    templates_dict={
        "ini":migrations_ini.ALEMBIC_INI,
        "env":migrations_env.MIGRATIONS_ENV,
        "script_py_mako":migrations_script_py_mako.SCRIPT_PY_MAKO,
    }

    template=environment.from_string(templates_dict[template_name])
    return template

def get_docker_template(template_name:str):

    templates_dict={
        "docker_file":docker_file.DOCKER_FILE,
        "docker_compose":docker_compose.DOCKER_COMPOSE,

    }

    template=environment.from_string(templates_dict[template_name])
    return template

def get_app_template(template_name:str):
    
    templates_dict={
        "router":app_router.ROUTER,
        "schemas":app_schemas.SCHEMAS,
        "crud":app_crud.CRUD,
    }

    template=environment.from_string(templates_dict[template_name])
    return template
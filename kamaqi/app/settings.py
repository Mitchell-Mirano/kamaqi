from jinja2 import Environment, BaseLoader
from kamaqi.templates import app_auth,app_database,app_exceptions
from kamaqi.templates import app_schemas,app_router,app_exceptions
from kamaqi.templates import main,app_settings,env,requirements
from kamaqi.templates import router,schemas,models,crud

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
        "crud":crud.CRUD

    }
    template=environment.from_string(templates_dict[template_name])
    return template
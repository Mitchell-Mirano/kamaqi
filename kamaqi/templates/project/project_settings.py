PROJECT_SETTINGS=\
"""
from fastapi_mail import ConnectionConfig
from functools import lru_cache
from pydantic import BaseSettings
from pydantic import EmailStr



class {{project_name.capitalize()}}Settings(BaseSettings):
    BACKEND_HOST:str
    class Config:
        env_file =".env"

@lru_cache()
def get_{{project_name}}_settings():
    return {{project_name.capitalize()}}Settings()


class TokensConfig(BaseSettings):
    SECRET_KEY:str
    JMV_ALGORITHM:str
    TIME_DELTA:int
    class Config:
        env_file = ".env"

@lru_cache()
def get_tokens_config()->TokensConfig:
    return TokensConfig()

class EmailsSettings(BaseSettings):
    MAIL_USERNAME:str
    MAIL_PASSWORD:str
    MAIL_FROM:EmailStr
    MAIL_FROM_NAME:str
    MAIL_PORT:int
    MAIL_SERVER:str
    MAIL_TLS:bool
    MAIL_SSL:bool
    TEMPLATE_FOLDER:str

    class Config:
        env_file = ".env"

@lru_cache()
def get_email_settings():
    email_settings=EmailsSettings()
    return ConnectionConfig(**email_settings.dict())


class DatabaseSettings(BaseSettings):
    DATABASE_USER:str
    DATABASE_PASSWORD:str
    DATABASE_HOST:str
    DATABASE_PORT:str
    DATABASE_NAME:str
    class Config:
        env_file = ".env"

def get_database_string_conection():
    {% if database_type == "SQLite" %}
    connection_string="sqlite:///./sql_{{project_name}}.db"
    {% else %}
    database_settings=DatabaseSettings()
    {% if database_type == "PostgreSQL" %}
    connection_string="postgresql+psycopg2://user:password@host:port/database_name"
    {% endif %}
    {% if database_type == "MySQL" %}
    connection_string="mysql+pymysql://user:password@host:port/database_name"
    {% endif %}
    connection_string=connection_string\\
                      .replace("user",database_settings.DATABASE_USER)\\
                      .replace("password",database_settings.DATABASE_PASSWORD)\\
                      .replace("host",database_settings.DATABASE_HOST)\\
                      .replace("port",database_settings.DATABASE_PORT)\\
                      .replace("database_name",database_settings.DATABASE_NAME)
    {% endif %}  
    return connection_string
"""
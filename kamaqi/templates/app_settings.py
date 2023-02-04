APP_SETTINGS=\
"""
from fastapi_mail import ConnectionConfig
from functools import lru_cache
from pydantic import BaseSettings
from pydantic import EmailStr



class {{app.capitalize()}}Settings(BaseSettings):
    BACKEND_HOST:str
    class Config:
        env_file =".env"

@lru_cache()
def get_{{app}}_settings():
    return {{app.capitalize()}}Settings()


class TokensConfig(BaseSettings):
    SECRET_KEY:str
    JMV_ALGORITHM:str
    TIME_DELTA:int
    class Config:
        env_file = ".env"

@lru_cache()
def get_tokens_config()->TokensConfig:
    return TokensConfig()

class FileSettings(BaseSettings):
    DF_COLUMNS:str

    def get_df_columns(self)->list[str]:
        return [column.strip() for column in self.DF_COLUMNS.split(',')]

    class Config:
        env_file = ".env"

@lru_cache()
def get_file_settings()->FileSettings:
    return FileSettings()

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
    database_settings=DatabaseSettings()
    conection_string="postgresql+psycopg2://user:password@host:port/database_name"
    conection_string=conection_string.replace("user",database_settings.DATABASE_USER)\
                    .replace("password",database_settings.DATABASE_PASSWORD)\
                    .replace("host",database_settings.DATABASE_HOST)\
                    .replace("port",database_settings.DATABASE_PORT)\
                    .replace("database_name",database_settings.DATABASE_NAME)
    return conection_string                                                                              

"""
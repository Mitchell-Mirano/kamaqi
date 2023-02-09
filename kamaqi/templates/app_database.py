APP_DATABASE=\
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from {{project_name}}.settings import get_database_string_conection


DATABASE_URL=get_database_string_conection()
{% if database_type=='SQLite' %}
engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})
{% else %}
engine = create_engine(DATABASE_URL)
{% endif %}

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
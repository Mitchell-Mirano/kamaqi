CRUD=\
"""
#Python
from pydantic import EmailStr

#{{app.capitalize()}}
from {{app}}s.schemas import {{app.capitalize()}}Create

#Database
from sqlalchemy.orm import Session
from database.models import {{app.capitalize()}}

def create_{{app}}(db: Session, 
                {{app}}:{{app.capitalize()}}Create):

    {{app}}_dict = {{app}}.dict()

    db_{{app}} = models.{{app.capitalize()}}(**{{app}}_dict)
    db.add(db_{{app}})
    db.commit()
    db.refresh(db_{{app}})

    return db_{{app}}

def get_{{app}}_by_id(db: Session, id: int):

    return db.query(models.{{app.capitalize()}})\\
           .filter(models.{{app.capitalize()}}.id == id).first()
"""
CRUD=\
"""
#Python

#{{app.capitalize()}}
from {{app}}s.schemas import {{app.capitalize()}}Create, {{app.capitalize()}}Update

#Database
from sqlalchemy.orm import Session
from database import models

def insert_{{app}}(db: Session, 
                      {{app}}:{{app.capitalize()}}Create):

    {{app}}_dict = {{app}}.dict()

    db_{{app}} = models.{{app.capitalize()}}(**{{app}}_dict)
    db.add(db_{{app}})
    db.commit()
    db.refresh(db_{{app}})

    return db_{{app}}

def select_{{app}}_by_id(db: Session, id: int):

    db_{{app}}= db.query(models.{{app.capitalize()}})\\
                .filter(models.{{app.capitalize()}}.id == id)\\
                .first()
                
    return db_{{app}}

def select_all_{{app}}s(db:Session):

    db_{{app}}s= db.query(models.{{app.capitalize()}}).all()
    return db_{{app}}s

def update_{{app}}_in_db(db: Session, id: int, 
                        {{app}}:{{app.capitalize()}}Update):

    db_{{app}} = select_{{app}}_by_id(db, id)

    db_{{app}}.name={{app}}.name
    db.add(db_{{app}})
    db.commit()
    db.refresh(db_{{app}})

    return db_{{app}}

def delete_{{app}}_in_db(db: Session, id: int):
    
    db_user = select_{{app}}_by_id(db, id)

    db.delete(db_user)
    db.commit()
"""
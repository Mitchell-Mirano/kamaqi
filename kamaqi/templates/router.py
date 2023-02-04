ROUTER=\
"""
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database.database import get_db

from {{app}}s.schemas import  {{app.capitalize()}}Create
from {{app}}s.schemas import  {{app.capitalize()}}Read
from {{app}}s.schemas import  {{app.capitalize()}}Update
from {{app}}s.schemas import  {{app.capitalize()}}Delete

from {{app}}s.crud import create_{{app}},get_{{app}}_by_id

{{app}}s_routs= APIRouter()


@{{app}}s_routs.post(path='/api/v1/{{app}}s/create/',
                    tags=["{{app.capitalize()}}s"])

async def create_{{app}}({{app}}_data:{{app.capitalize()}}Create,
                         db=Depends(get_db)):
    db_{{app}}=create_{{app}}(db,{{app}}_data)
    return db_{{app}}

@{{app}}s_routs.get(path='/api/v1/{{app}}s/{id}/',
                    tags=["{{app.capitalize()}}s"])

async def get_one_{{app}}(id:int,db=Depends(get_db)):
    db_{{app}}=get_{{app}}_by_id(db,id)
    return db_{{app}}

"""

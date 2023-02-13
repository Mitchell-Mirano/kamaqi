ROUTER=\
"""
from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db

from {{app}}s.schemas import {{app.capitalize()}}Create
from {{app}}s.schemas import {{app.capitalize()}}Read
from {{app}}s.schemas import {{app.capitalize()}}Update

from {{app}}s.crud import insert_{{app}},select_{{app}}_by_id
from {{app}}s.crud import select_all_{{app}}s,update_{{app}}_in_db
from {{app}}s.crud import delete_{{app}}_in_db

{{app}}s_routs= APIRouter(prefix="/api/v1/{{app}}s")


@{{app}}s_routs.post(path="/create/",
                     tags=["{{app.capitalize()}}s"],
                     response_model={{app.capitalize()}}Read,
                     status_code=status.HTTP_201_CREATED)
async def create_{{app}}({{app}}_data:{{app.capitalize()}}Create,
                        db:Session=Depends(get_db)):

    return insert_{{app}}(db,{{app}}_data)

@{{app}}s_routs.get(path="/get/all/",
                    tags=["{{app.capitalize()}}s"],
                    response_model=List[{{app.capitalize()}}Read],
                    status_code=status.HTTP_200_OK)
async def get_all_{{app}}s(db:Session=Depends(get_db)):

    db_{{app}}s=select_all_{{app}}s(db)
    if not db_{{app}}s:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="{{app}}s not found")
    
    return db_{{app}}s

@{{app}}s_routs.get(path="/get/{id}/",
                    tags=["{{app.capitalize()}}s"],
                    response_model={{app.capitalize()}}Read,
                    status_code=status.HTTP_200_OK)
async def get_{{app}}(id:int,db:Session=Depends(get_db)):

    db_{{app}}=select_{{app}}_by_id(db,id)
    if not db_{{app}}:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="{{app}} not found")
    return db_{{app}}

@{{app}}s_routs.put(path="/update/{id}/",
                tags=["{{app.capitalize()}}s"],
                response_model={{app.capitalize()}}Read,
                status_code=status.HTTP_200_OK)
async def update_{{app}}(id:int,
                        {{app}}_data:{{app.capitalize()}}Update,
                        db:Session=Depends(get_db)):

    return update_{{app}}_in_db(db,id,{{app}}_data)

@{{app}}s_routs.delete(path="/delete/{id}/",
                    tags=["{{app.capitalize()}}s"],
                    status_code=status.HTTP_200_OK)
async def delete_{{app}}(id:int,db:Session=Depends(get_db)):

    delete_{{app}}_in_db(db,id)

    return JSONResponse(content={"detail":"{{app}} deleted"},
                        status_code=status.HTTP_200_OK)

"""

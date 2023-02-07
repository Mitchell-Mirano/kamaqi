SCHEMAS=\
"""
from pydantic import BaseModel

class {{app.capitalize()}}Create(BaseModel):
    name:str

class {{app.capitalize()}}Read(BaseModel):
    id:int
    name:str

    class Config:
        orm_mode = True

class {{app.capitalize()}}Update(BaseModel):
    name:str
"""

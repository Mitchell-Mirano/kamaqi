SCHEMAS=\
"""
from pydantic import BaseModel, ConfigDict

class {{app.capitalize()}}Create(BaseModel):
    name:str

class {{app.capitalize()}}Read(BaseModel):
    id:int
    name:str
    
    model_config = ConfigDict(from_attributes=True)
    
class {{app.capitalize()}}Update(BaseModel):
    name:str
"""

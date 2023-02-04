SCHEMAS=\
"""
from pydantic import BaseModel

class {{app.capitalize()}}Create(BaseModel):
    pass

class {{app.capitalize()}}Read(BaseModel):
    pass

class {{app.capitalize()}}Update(BaseModel):
    pass

class {{app.capitalize()}}Delete(BaseModel):
    pass
"""

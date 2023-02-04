APP_ROUTER=\
"""
from fastapi import APIRouter,Depends
from fastapi.responses import RedirectResponse
from {{app}}.settings import {{app.capitalize()}}Settings,get_{{app}}_settings

{{app}}_routs= APIRouter()

@{{app}}_routs.get(path="/",
                   include_in_schema=False)
def documentation({{app}}_settings:{{app.capitalize()}}Settings=Depends(get_{{app}}_settings)):
    return RedirectResponse(url={{app}}_settings.BACKEND_HOST +"/docs/")
"""

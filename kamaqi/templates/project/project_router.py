PROJECT_ROUTER=\
"""
from fastapi import APIRouter,Depends
from fastapi.responses import RedirectResponse
from {{project_name}}.settings import {{project_name.capitalize()}}Settings,get_{{project_name}}_settings

{{project_name}}_routes= APIRouter()

@{{project_name}}_routes.get(path="/",
                   include_in_schema=False)
def documentation({{project_name}}_settings:{{project_name.capitalize()}}Settings=Depends(get_{{project_name}}_settings)):
    return RedirectResponse(url={{project_name}}_settings.BACKEND_HOST +"/docs/")
"""

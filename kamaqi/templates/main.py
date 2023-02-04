MAIN=\
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routs
from {{project_name}}.router import {{project_name}}_routs
{%  for app in apps %}
from {{app}}.router import {{app}}_routs
{%  endfor %}


app = FastAPI(title="{{project_name}} API")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# Include routs
app.include_router({{project_name}}_routs)
{%  for app in apps %}
app.include_router({{app}}_routs)
{%  endfor %}
""" 
PROJECT_MAIN=\
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Import routs
{%  for app in apps.keys() %}
from {{app}}.router import {{app}}_routs
{%  endfor %}

app = FastAPI(title="{{project_name.capitalize()}} API",
              description="A powerful API for {{project_name.capitalize()}} project",
              version="1.0.0")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# Include routs
{%  for app in apps.keys() %}
app.include_router({{app}}_routs)
{%  endfor %}
""" 
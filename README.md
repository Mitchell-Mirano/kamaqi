# Kamaqi
A command line app for creating Backends with **FastAPI**, inspired in **Artisan** from **Laravel** and **manage.py** from **Django**.

# Content
- [The key features are](#the-key-features-are)
- [Installation](#installation)
- [Basic usage](#basic-usage)
- [Project Status](#project-status)

## The key features are:

- Creates a normal project or a project with **Docker**.
- Chooses a **MySQL**, **PostgreSQL** or **SQLite** database.
- Works as with **Django** creating  apps.
- Every application created with **Kamaqi** contains a minimum **CRUD**.
- Integration between **SQLAlchemy** and **Alembic** for migrations.

### What is an app?
An application is a module of your project, which manages the logic of an actor of your application, for example (users, products, shops ... etc). Generally, an app is associated with a table in the database on which you want to do CRUD operations and they are named in the plural.


Every app created with Kamaqi contains the following
files. For example:

```bash
users
├── crud.py
├── router.py
└── schemas.py
```
- The **schemas.py** file contains classes of validation for input and output  data using
Pydantic. For example:

```python
from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    name:str
    email:EmailStr
    password:str

class UserRead(BaseModel):
    id:int
    name:str
    email:EmailStr
```
- The **router.py** contains an APIRouter and endpoint functions. for example:
```python
from fastapi import APIRouter,Depends,status
from users.schemas import UserCreate
from users.schemas import UserRead
from users.crud import insert_user

from sqlalchemy.orm import Session
from database.database import get_db

users_routes= APIRouter(prefix="/api/v1/users")

@users_routes.post(path="/create/",
                 tags=["Users"],
                 response_model=UserRead,
                 status_code=status.HTTP_201_CREATED)
async def create_user(user_data:UserCreate,
                      db:Session=Depends(get_db)):

    return insert_user(db,user_data)
```

- The **crud.py** contains a CRUD functions for your modules as insert_app, update_app, select_app ... etc. For example:

```python
from users.schemas import UserCreate
from sqlalchemy.orm import Session
from database import models

def insert_user(db: Session, 
                user:UserCreate):

    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_app
```
This is just an example, in a real development environment, before
inserting the user into the database should encrypt the password, check if the user is not registered...etc.

### Project Structure

When creates a new project with Kamaqi this can have the following structures.

- A projects with Docker following the next structure.

```bash
project_name
├── db_volume
├── docker-compose.yaml
├── Dockerfile
├── kamaqi.json
├── requirements.txt
└── src
    ├── alembic.ini
    ├── database
    │   ├── database.py
    │   ├── models.py
    ├── main.py
    ├── .env
    ├── migrations
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    ├── users
    │   ├── crud.py
    │   ├── router.py
    │   └── schemas.py
    └── project_name
        ├── auth.py
        ├── exceptions.py
        ├── router.py
        ├── schemas.py
        └── settings.py
```
- The normal projects following the nex structure.

```bash 
project_name
├── alembic.ini
├── database
│   ├── database.py
│   └── models.py
├── env
├── kamaqi.json
├── main.py
├── .env
├── migrations
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── requirements.txt
├── users
│   ├── crud.py
│   ├── router.py
│   └── schemas.py
└── project_name
    ├── auth.py
    ├── exceptions.py
    ├── router.py
    ├── schemas.py
    └── settings.py
```
- In normal projects the env directory is the
Python virtual environment.

- The .env file contains the environment
variables.

- The project_name is the main app in to the project.
- **auth.py** contains functions for hashing passwords, verify passwords and create access tokens. 
- **exceptions.py** contains some exceptions.
- **settings.py** contains classes and functions that provide environment variables like secret keys, database connection parameters...etc. These variables are taken from the .env file.


## Installation:

Install Kamaqi in the global environment.
```bash 
pip install kamaqi
```
For help on Kamaqi commands and parameters, use.
```bash
kamaqi --help 
kamaqi command --help
```
## Basic Usage:

### Init your project
- Start project in a new directory
```bash
kamaqi start project project_name
```
- Start project in the current directory
```bash
kamaqi start project .
```
Choose the options, for setting your project. Remember for create projects
with docker requires **docker** and **docker-compose** installed.

### Run your project
```bash
cd project_name
```
```bash
kamaqi run project
```
- Explore the FastAPI documentation.
- For Kamaqi the default port is the 8000.
- Open in your browser http://localhost:8000/docs
### Add apps to your project
Add an app 
```bash
kamaqi add app users
```
Add multiple apps
```bash
kamaqi add apps users products sales ... etc
```
### Create files for your apps
```bash
Kamaqi upgrade apps 
```
- Refresh files in your editor.
- Refresh the FastAPI documentation.
### Review your project settings
```bash
kamaqi show config
```
### Review your project apps
```bash
kamaqi show apps
```
### Database migrations
For update your database tables.
```bash
kamaqi upgrade tables -m"A description about your changes"
```
### To connect to MySQL or PostgreSQL database use.

- For projects with Docker, review the **docker-compose.yaml**
and use the database environment variables
or use the following parameters.
```bash
DATABASE_USER = project_name_user
DATABASE_PASSWORD = project_name_password
DATABASE_NAME = project_name_db
DATABASE_PORT = MySQL 3306  and PostgreSQL 5432
```
- For normal projects use your settings and in the .env and edit the connection parameters.

- For SQLite databases use a editor extension or a other 
software.

## Project Status
- The project is currently under development and may contain errors.

- You can contribute to this project, reporting bugs, writing documentation, writing tests, with pull requests... etc.

For more information, visit [GitHub repository](https://github.com/Mitchell-Mirano/kamaqi)






# Kamaqi
A command line app for creating Backends with **FastAPI**, inspired in **Artisan** from **Laravel** and **manage.py** from **Django**.

## The key features are:

- Creates a normal project or a project with **Docker**.
- Chooses a **MySQL**, **PostgreSQL** or **SQLite** database.
- Works as with **Django** creating  apps.
- Every application created with **Kamaqi** contains a minimum **CRUD**.

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

### Init your project:
```bash
kamaqi init project you_project_name
```
Choose the options, for setting your project. Remember for create projects
with docker requires **docker** and **docker-compose** installed.

### Run your project
```bash
cd your_project_name
```
```bash
kamaqi run project you_project_name
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
DATABASE_USER = your_project_name_user
DATABASE_PASSWORD = your_project_name_password
DATABASE_NAME = your_project_name_db
DATABASE_PORT = MySQL 3306  and PostgreSQL 5432
```
- For normal projects use your settings and in the .env and edit the connection parameters.

- For SQLite databases use a editor extension or a other 
software.

## Project Status
- The project is currently under development and may contain errors.

- You can contribute to this project, reporting bugs, writing documentation, writing tests, with pull requests... etc.

For more information, visit [GitHub repository](https://github.com/Mitchell-Mirano/kamaqi)






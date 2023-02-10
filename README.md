# Kamaqi

A command line app for creating Backends with FastAPI, inspired in Artisan from Laravel and manage.py from Django.

## The key features are:

- Create a normal project and a project with `Docker`.
- Choose a different databases  `MySQL`, `PostgreSQL` and `SQLite`.
- Work as `Djando` creating apps.
- Every app created with Kamaqi, contains a minimal CRUD.

## Installation:

Install Kamaqi in the global environment.
```bash 
pip install kamaqi
```
For explore Kamaqi commands and options use.
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
- Explore your API documentation
- For default kamaqi use the port 8000
- Open in your browser http://localhost:8000/docs
### Add apps to your project
Add an app 
```bash
kamaqi add app users
```
Add multiple apps
```bash
kamaqi add apps users products sales... etc
```
### Create files for your apps
```bash
Kamaqi upgrade apps 
```
- Refresh files in your editor.
- Refresh your API documentation
### Review your project settings
```bash
kamaqi show config
```
### Review your project apps
```bash
kamaqi show apps
```

## Project Status
- The project currently is in  development and will be
bugs.

- Your can contribute to this project, reporting bugs, writing documentation, writing tests, with pull requests ... etc.

For more information visit [GitHub repository](https://github.com/Mitchell-Mirano/kamaqi)






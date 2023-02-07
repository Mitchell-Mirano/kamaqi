# Kamaqi

A command line app for creating APIs with FastAPI, inspired in Artisan from Laravel and manage.py from Django.

## The key features are:

- Create a normal project and a project with `Docker`.
- Choose a different databases  `MySQL`, `PostgreSQL` and `SQLite`.
- Work as `Djando` creating apps.
- Every app created with Kamaqi, contains a minimal CRUD.

## Installation:

Install Kamaqi in the global environment

```bash 
pip install kamaqi
```
## Basic Usage:

### Init yout project:

Run
```bash
kamaqi init project you_project_name
```
Add choose the options, for setting your project.

### Run your project
Run 
```bash
cd your_project_name
```
```bash
kamaqi run project you_project_name
```
- Exploe your API documentation
- For default kamaqi use the port 8000
- Open in your browser http://localhost:8000/docs
### Add apps to your project
Run 
```bash
kamaqi add apps users products shops ... etc
```
### Create files for your apps
Run 
```bash
Kamaqi upgrade apps 
```
- Refresh your editor files.
- Refresh your API documentation

## Project Status
- The project currently is development and will be
bugs.

- Your can contribute to this project, repoting bugs, writing documentation, writing tests, with pull requests ... etc.

For more information visit [github repository](https://github.com/Mitchell-Mirano/kamaqi)






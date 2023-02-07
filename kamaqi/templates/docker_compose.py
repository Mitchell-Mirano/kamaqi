DOCKER_COMPOSE=\
"""
version: "3.8"
services:

  {{project_name}}_db:
    container_name: {{project_name}}_db
    {% if database_type=='PostgreSQL' %}
    image: postgres
    environment:
      POSTGRES_USER: {{project_name}}_user
      POSTGRES_PASSWORD: {{project_name}}_password
      POSTGRES_DB: {{project_name}}_db
    ports:
      - "5432:5432"
    volumes: 
      - ./db_volume:/var/lib/postgresql/data
    {% else %}
    image: mysql
    environment:
      MYSQL_USER: {{project_name}}_user
      MYSQL_PASSWORD: {{project_name}}_password
      MYSQL_ROOT_PASSWORD: {{project_name}}_password
      MYSQL_DATABASE: {{project_name}}_db
    ports:
      - "3306:3306"
    volumes: 
      - ./db_volume:/var/lib/mysql
    {% endif %}

  {{project_name}}:
    container_name: {{project_name}}_api
    image: {{project_name.lower()}}_image
    volumes:
      - ./src:/{{project_name}}
    ports:
      - "8000:80"
"""

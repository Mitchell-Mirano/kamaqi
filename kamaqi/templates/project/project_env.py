PROJECT_ENV=\
"""
#app settings
BACKEND_HOST=http://localhost:8000

#auth settings
SECRET_KEY={{secret_key}}
JMV_ALGORITHM=HS256
TIME_DELTA=2

#db config local
{% if database_type!= 'SQLite' %}
DATABASE_USER={{project_name}}_user
DATABASE_PASSWORD={{project_name}}_password
{% if project_type=='normal' %}
DATABASE_HOST=localhost
{% else %}
DATABASE_HOST={{project_name}}_db
{% endif %}
DATABASE_NAME={{project_name}}_db
{% if database_type == 'MySQL' %}
DATABASE_PORT=3306
{% endif %}
{% if database_type == 'PostgreSQL' %}
DATABASE_PORT=5432
{% endif %}
{% endif %}

#db config production
#DATABASE_USER=
#DATABASE_PASSWORD=
#DATABASE_HOST=
#DATABASE_NAME=
#DATABASE_PORT=

#email settings
#MAIL_USERNAME=
#MAIL_PASSWORD=
#MAIL_FROM=
#MAIL_FROM_NAME=
#MAIL_PORT=587
#MAIL_SERVER=smtp.gmail.com
#MAIL_TLS=True
#MAIL_SSL=False
#TEMPLATE_FOLDER=emails/templates 
"""
 
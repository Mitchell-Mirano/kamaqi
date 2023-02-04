ENV=\
"""
#app settings
BACKEND_HOST=http://localhost:8000

#auth settings
SECRET_KEY={{secret_key}}
JMV_ALGORITHM=HS256
TIME_DELTA=2

#db config local
DATABASE_USER={{project_name}}
DATABASE_PASSWORD={{project_name}}password
DATABASE_HOST={{project_name}}_db
DATABASE_NAME={{project_name}}_db
DATABASE_PORT=5432

#db config production
#DATABASE_USER=
#DATABASE_PASSWORD=
#DATABASE_HOST=
#DATABASE_NAME=
#DATABASE_PORT=5432

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
 
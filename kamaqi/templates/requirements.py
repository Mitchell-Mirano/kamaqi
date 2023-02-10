REQUIREMENTS=\
"""
rich
python-jose[cryptography]
{% if database_type=='MySQL'%}
pymysql
{% endif %}
{% if database_type=='PostgreSQL'%}
psycopg2-binary
{% endif %}
SQLAlchemy
passlib[bcrypt]
fastapi[all]
fastapi-mail
"""
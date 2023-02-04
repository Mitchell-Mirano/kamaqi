MODELS=\
"""
from sqlalchemy import Column, Integer
from database.database import Base


{% for app in apps %}

class {{app.capitalize()}}(Base):
    __tablename__="{{app}}"
    id = Column(Integer, primary_key=True, index=True)
    
{% endfor %}
"""

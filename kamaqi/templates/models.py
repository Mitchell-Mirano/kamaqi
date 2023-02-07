MODELS=\
"""
from sqlalchemy import Column, Integer,String
from database.database import Base


{% for app in apps %}

class {{app.capitalize()}}(Base):
    __tablename__="{{app}}s"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(50))
{% endfor %}
"""

MODEL=\
"""
class {{app.capitalize()}}(Base):
    __tablename__="{{app}}s"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(50))
"""
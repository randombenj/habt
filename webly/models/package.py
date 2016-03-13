from sqlalchemy import Column
from sqlalchemy import Integer, String

from webly.models.base import Base

class Package(Base):
    __tablename__ = 'package'
    id = Column(Integer, primary_key=True)
    name = Column(String)

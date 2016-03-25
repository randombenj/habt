from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from webly.models.database import Base

class Package(Base):
    __tablename__ = 'package'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    versions = relationship("PackageVersion", back_populates="package")

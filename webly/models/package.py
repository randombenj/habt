from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin

class Package(GetOrCreateMixin, Base):
    __tablename__ = 'package'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    versions = relationship("PackageVersion", back_populates="package")
    referenced_by = relationship("Dependency", back_populates="package")

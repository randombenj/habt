from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin

class PackageSection(GetOrCreateMixin, Base):
    __tablename__ = 'package_section'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    package_versions = relationship("PackageVersion", back_populates="section")

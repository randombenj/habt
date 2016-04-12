from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin

class DependencySection(GetOrCreateMixin, Base):
    __tablename__ = 'dependency_section'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dependencies = relationship("Dependency", back_populates="dependency_section")

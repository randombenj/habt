from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin


class Dependency(GetOrCreateMixin, Base):
    __tablename__ = 'dependency'
    id = Column(Integer, primary_key=True)
    version = Column(String)
    package_id = Column(Integer, ForeignKey('package.id'))
    package = relationship(
        "Package",
        back_populates="referenced_by"
    )
    package_version_id = Column(
        Integer,
        ForeignKey('package_version.id')
    )
    package_version = relationship(
        "PackageVersion",
        back_populates="dependencies")
    dependency_section_id = Column(
        Integer,
        ForeignKey('dependency_section.id')
    )
    dependency_section = relationship(
        "DependencySection",
        back_populates="dependencies"
    )

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from habt.database import Base, GetOrCreateMixin


class Dependency(GetOrCreateMixin, Base):
    """
        Represents a package dependency
    """

    __tablename__ = "dependency"
    """ Database table name """

    id = Column(Integer, primary_key=True)
    """ Unique id on the database """

    version = Column(String)
    """ Version of the referenced package if any """

    package_id = Column(Integer, ForeignKey("package.id"))
    """ Id of the package this dependency is for """
    package = relationship("Package", back_populates="referenced_by")
    """ Package this dependency is for """

    package_version_id = Column(Integer, ForeignKey("package_version.id"))
    """ Id of the package version referencing this dependency """
    package_version = relationship("PackageVersion", back_populates="dependencies")
    """ The package version referencing this dependency """

    dependency_section_id = Column(Integer, ForeignKey("dependency_section.id"))
    """ Id of the dependency section """
    dependency_section = relationship(
        "DependencySection", back_populates="dependencies"
    )
    """ The dependency section """

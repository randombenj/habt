from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin
from webly.models.installtarget import association_table


class PackageVersion(GetOrCreateMixin, Base):
    __tablename__ = 'package_version'
    id = Column(Integer, primary_key=True)
    version = Column(String)
    title = Column(String)
    description = Column(String)
    maintainer = Column(String)
    filename = Column(String)
    homepage = Column(String)
    vcs_browser = Column(String)
    package_id = Column(
        Integer,
        ForeignKey('package.id')
    )
    package = relationship(
        "Package",
        back_populates="versions"
    )
    section_id = Column(
        Integer,
        ForeignKey('package_section.id')
    )
    section = relationship(
        "PackageSection",
        back_populates="package_versions"
    )
    dependencies = relationship(
        "Dependency",
        back_populates="package_version"
    )
    installtargets = relationship(
        "InstallTarget",
        secondary=association_table,
        back_populates="package_versions"
    )

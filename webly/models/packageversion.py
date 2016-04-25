from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin
from webly.models.installtarget import association_table


class PackageVersion(GetOrCreateMixin, Base):
    __tablename__ = 'package_version'
    ''' Database table name '''

    id = Column(Integer, primary_key=True)
    ''' Unique id on the database '''

    version = Column(String)
    ''' Version of the packag '''

    title = Column(String)
    ''' Title of the package version '''

    description = Column(String)
    ''' A short description about the package version '''

    maintainer = Column(String)
    ''' The package version maintainer in the format "name <email>" '''

    filename = Column(String)
    ''' Path to the .deb file on the archive '''

    homepage = Column(String)
    ''' Homepage of the package version if any '''

    vcs_browser = Column(String)
    ''' Link to the sourcecode of the package version '''

    package_id = Column(
        Integer,
        ForeignKey('package.id')
    )
    ''' Id of the package this version belongs to '''
    package = relationship(
        "Package",
        back_populates="versions"
    )
    ''' Package this version belongs to '''

    section_id = Column(
        Integer,
        ForeignKey('package_section.id')
    )
    ''' Id of the section this package version is belonging to '''
    section = relationship(
        "PackageSection",
        back_populates="package_versions"
    )
    ''' Section this package version is belonging to '''

    dependencies = relationship(
        "Dependency",
        back_populates="package_version"
    )
    ''' All dependencies of this package version '''

    installtargets = relationship(
        "InstallTarget",
        secondary=association_table,
        back_populates="package_versions"
    )
    ''' Installtargets who deliver this version of a package version '''

from sqlalchemy import Column, Table
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from habt.database import Base, GetOrCreateMixin


association_table = Table(
    'package_version_instaltarget',
    Base.metadata,
    Column('packageversion_id', Integer, ForeignKey('package_version.id')),
    Column('installtareget_id', Integer, ForeignKey('installtarget.id'))
)


class InstallTarget(GetOrCreateMixin, Base):
    __tablename__ = 'installtarget'
    ''' Database table name '''

    id = Column(Integer, primary_key=True)
    ''' Unique id on the database '''

    package_versions = relationship(
        "PackageVersion",
        secondary=association_table,
        back_populates="installtargets"
    )
    ''' All package versions matching this installtarget '''

    archive_id = Column(
        Integer,
        ForeignKey('archive.id')
    )
    ''' Id of the package archive '''
    archive = relationship(
        "Archive",
        back_populates="installtargets"
    )
    ''' The package archive '''

    distribution_id = Column(
        Integer,
        ForeignKey('distribution.id')
    )
    ''' Id of the distribution '''
    distribution = relationship(
        "Distribution",
        back_populates="installtargets"
    )
    ''' The distribution '''

    part_id = Column(
        Integer,
        ForeignKey('part.id')
    )
    ''' Id of the part '''
    part = relationship(
        "Part",
        back_populates="installtargets"
    )
    ''' The part '''

    architecture_id = Column(
        Integer,
        ForeignKey('architecture.id')
    )
    ''' Id of the architecture '''
    architecture = relationship(
        "Architecture",
        back_populates="installtargets"
    )
    ''' The architecture '''

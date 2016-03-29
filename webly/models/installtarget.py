from sqlalchemy import Column, Table
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin

association_table = Table('package_version_instaltarget', Base.metadata,
    Column('packageversion_id', Integer, ForeignKey('package_version.id')),
    Column('installtareget_id', Integer, ForeignKey('installtarget.id'))
)

class InstallTarget(GetOrCreateMixin, Base):
    __tablename__ = 'installtarget'
    id = Column(Integer, primary_key=True)
    package_versions = relationship(
        "PackageVersion",
        secondary=association_table,
        back_populates="installtargets")

    archive_id = Column(Integer, ForeignKey('archive.id'))
    archive = relationship("Archive", back_populates="installtargets")

    distribution_id = Column(Integer, ForeignKey('distribution.id'))
    distribution = relationship("Distribution", back_populates="installtargets")

    part_id = Column(Integer, ForeignKey('part.id'))
    part = relationship("Part", back_populates="installtargets")

    architecture_id = Column(Integer, ForeignKey('architecture.id'))
    architecture = relationship("Architecture", back_populates="installtargets")

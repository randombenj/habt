from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from habt.database import Base, GetOrCreateMixin


class Package(GetOrCreateMixin, Base):
    '''
        Represents a debian package
    '''

    __tablename__ = 'package'
    ''' Database table name '''

    id = Column(Integer, primary_key=True)
    ''' Unique id on the database '''

    name = Column(String)
    ''' Name of the package '''

    versions = relationship(
        "PackageVersion",
        back_populates="package",
        order_by="desc(PackageVersion.version)"
    )
    ''' Available versions of this package '''

    referenced_by = relationship(
        "Dependency",
        back_populates="package"
    )
    ''' Packageversions referencing this package '''

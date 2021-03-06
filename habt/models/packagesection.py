from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from habt.database import Base, GetOrCreateMixin


class PackageSection(GetOrCreateMixin, Base):
    """
        Represents the package section grouping
        packages by what their purpose
    """

    __tablename__ = "package_section"
    """ Database table name """

    id = Column(Integer, primary_key=True)
    """ Unique id on the database """

    name = Column(String)
    """ Name of the package section """

    package_versions = relationship("PackageVersion", back_populates="section")
    """ Package versions in this section """

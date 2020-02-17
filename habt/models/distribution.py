from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from habt.database import Base, GetOrCreateMixin


class Distribution(GetOrCreateMixin, Base):
    """
        Represents the debian distribution
    """

    __tablename__ = "distribution"
    """ Database table name """

    id = Column(Integer, primary_key=True)
    """ Unique id on the database """

    name = Column(String)
    """ Distribution name """

    installtargets = relationship("InstallTarget", back_populates="distribution")
    """ Installtargets referencing this distribution """

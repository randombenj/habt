from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from habt.database import Base, GetOrCreateMixin


class Archive(GetOrCreateMixin, Base):
    """
        Represents a package archive where reopsitories
        are stored.
    """

    __tablename__ = "archive"
    """ Database table name """

    id = Column(Integer, primary_key=True)
    """ Unique id on the database """

    url = Column(String)
    """ Url of the archive """

    installtargets = relationship("InstallTarget", back_populates="archive")
    """ Installtargets referencing this archive """

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from habt.database import Base, GetOrCreateMixin


class Architecture(GetOrCreateMixin, Base):
    """
        Represents the hardware architecture
    """

    __tablename__ = "architecture"
    """ Database table name """

    id = Column(Integer, primary_key=True)
    """ Unique id on the database """

    name = Column(String)
    """ Architecture name """

    installtargets = relationship("InstallTarget", back_populates="architecture")
    """ Installtarget, referencing this architecture """

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from habt.database import Base, GetOrCreateMixin


class Part(GetOrCreateMixin, Base):
    __tablename__ = "part"
    """ Database table name """

    id = Column(Integer, primary_key=True)
    """ Unique id on the database """

    name = Column(String)
    """ Name of the part """

    installtargets = relationship("InstallTarget", back_populates="part")
    """ Installtargets referencing this part """

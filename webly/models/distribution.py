from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin


class Distribution(GetOrCreateMixin, Base):
    '''
        Represents the debian distribution
    '''

    __tablename__ = 'distribution'
    ''' Database table name '''

    id = Column(Integer, primary_key=True)
    ''' Unique id on the database '''

    name = Column(String)
    ''' Distribution name '''

    installtargets = relationship(
        "InstallTarget",
        back_populates="distribution"
    )
    ''' Installtargets referencing this distribution '''

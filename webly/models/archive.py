from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin


class Archive(GetOrCreateMixin, Base):
    '''
        Represents a package archive where reopsitories
        are stored.
    '''

    __tablename__ = 'archive'
    ''' Database table name '''

    id = Column(Integer, primary_key=True)
    ''' Unique id on the database '''

    url = Column(String)
    ''' Url of the archive '''

    installtargets = relationship(
        "InstallTarget",
        back_populates="archive"
    )
    ''' Installtargets referencing this archive '''

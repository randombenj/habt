from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin


class Architecture(GetOrCreateMixin, Base):
    '''
        Represents the hardware architecture
    '''

    __tablename__ = 'architecture'
    ''' Database table name '''

    id = Column(Integer, primary_key=True)
    ''' Unique id on the database '''

    name = Column(String)
    ''' Architecture name '''

    installtargets = relationship(
        "InstallTarget",
        back_populates="architecture"
    )
    ''' Installtarget, referencing this architecture '''

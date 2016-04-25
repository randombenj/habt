from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin


class Part(GetOrCreateMixin, Base):
    __tablename__ = 'part'
    ''' Database table name '''

    id = Column(Integer, primary_key=True)
    ''' Unique id on the database '''

    name = Column(String)
    ''' Name of the part '''

    installtargets = relationship(
        "InstallTarget",
        back_populates="part"
    )
    ''' Installtargets referencing this part '''

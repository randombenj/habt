from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin


class Distribution(GetOrCreateMixin, Base):
    __tablename__ = 'distribution'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    installtargets = relationship(
        "InstallTarget",
        back_populates="distribution"
    )

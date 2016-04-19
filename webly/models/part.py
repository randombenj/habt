from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin


class Part(GetOrCreateMixin, Base):
    __tablename__ = 'part'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    installtargets = relationship(
        "InstallTarget",
        back_populates="part"
    )

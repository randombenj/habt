from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin

class Archive(GetOrCreateMixin, Base):
    __tablename__ = 'archive'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    installtargets = relationship("InstallTarget", back_populates="archive")

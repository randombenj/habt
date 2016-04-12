from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin

class Architecture(GetOrCreateMixin, Base):
    __tablename__ = 'architecture'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    installtargets = relationship("InstallTarget", back_populates="architecture")

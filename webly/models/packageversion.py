from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin

class PackageVersion(GetOrCreateMixin, Base):
    __tablename__ = 'package_version'
    id = Column(Integer, primary_key=True)
    version = Column(String)
    description = Column(String)
    maintainer = Column(String)
    filename = Column(String)
    package_id = Column(Integer, ForeignKey('package.id'))
    package = relationship("Package", back_populates="versions")

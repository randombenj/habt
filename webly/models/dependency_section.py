from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from webly.database import Base, GetOrCreateMixin


class DependencySection(GetOrCreateMixin, Base):
    '''
        Represents a dependency section.
        The dependency section devides dependencies
        into one of the folowing sections:

            depends,
            pre-depends,
            recommends,
            suggests,
            breaks,
            conflicts,
            provides,
            replaces,
            enhances,
    '''

    __tablename__ = 'dependency_section'
    ''' Database table name '''

    id = Column(Integer, primary_key=True)
    ''' Unique id on the database '''

    name = Column(String)
    ''' Name of the dependency section '''

    dependencies = relationship(
        "Dependency",
        back_populates="dependency_section"
    )
    ''' The dependencies in this section '''

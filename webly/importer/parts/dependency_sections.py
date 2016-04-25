from webly.models import DependencySection
from webly.importer.helper import timeit
from webly.database import session

import logging

log = logging.getLogger(__name__)


class DependencySectionImporter():

    @timeit
    def run(self):
        '''
            Imports the dependency sections
        '''
        sections = [
            'depends',
            'pre-depends',
            'recommends',
            'suggests',
            'breaks',
            'conflicts',
            'provides',
            'replaces',
            'enhances'
        ]
        for section in sections:
            session.add(DependencySection(name=section))
        session.commit()

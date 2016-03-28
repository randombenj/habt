from webly.models import DependencySection
from webly.migrator.helper import timeit
from webly.database import session

import logging

log = logging.getLogger(__name__)

class DependencySectionMigrator():

    @timeit
    def run(self):
        '''
            Migrates the dependency sections
        '''
        sections = [
            'depends'
            'recommends'
            'suggests'
            'enhances'
        ]
        for section in sections:
            session.add(DependencySection(name=section))
        session.commit()

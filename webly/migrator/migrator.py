import os
import logging
from webly.migrator.source import Source

from webly.migrator.parts import (
    PackageMigrator,
    DependencySectionMigrator,
    InstallTargetMigrator
)

log = logging.getLogger(__name__)


class Migrator():
    def __init__(self):
        self._packages = Source(
            os.path.join(os.path.dirname(__file__), 'sources.list')
        ).packages

    def run(self):
        '''
            Runs all the migrators
        '''
        DependencySectionMigrator().run()
        InstallTargetMigrator().run(self._packages)
        PackageMigrator(self._packages).run()

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
    def __init__(self, source_list_file):
        '''
            Initializes the migrator

            source_list_file:
             The path to the source.list config file
        '''
        self._packages = Source(source_list_file).packages

    def run(self):
        '''
            Runs all the migrators
        '''
        DependencySectionMigrator().run()
        InstallTargetMigrator().run(self._packages)
        PackageMigrator(self._packages).run()

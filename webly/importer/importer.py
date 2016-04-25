import os
import logging
from webly.importer.source import Source

from webly.importer.parts import (
    PackageImporter,
    DependencySectionImporter,
    InstallTargetImporter
)

log = logging.getLogger(__name__)


class Importer():
    def __init__(self, source_list_file):
        '''
            Initializes the Importer

            source_list_file:
             The path to the source.list config file
        '''
        self._packages = Source(source_list_file).packages

    def run(self):
        '''
            Runs all the Importers
        '''
        DependencySectionImporter().run()
        InstallTargetImporter().run(self._packages)
        PackageImporter(self._packages).run()

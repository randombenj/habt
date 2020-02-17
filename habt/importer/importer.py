import logging

# fmt: off
from habt.importer.parts import DependencySectionImporter, InstallTargetImporter, PackageImporter
from habt.importer.source import Source

log = logging.getLogger(__name__)


class Importer:
    def __init__(self, source_list_file):
        """
            Initializes the Importer

            source_list_file:
             The path to the source.list config file
        """
        self._packages = Source(source_list_file).packages

    def run(self):
        """
            Runs all the Importers
        """
        DependencySectionImporter().run()
        InstallTargetImporter().run(self._packages)
        PackageImporter(self._packages).run()

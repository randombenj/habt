import logging

from habt.database import session
from habt.importer.helper import timeit
from habt.models import DependencySection

log = logging.getLogger(__name__)


class DependencySectionImporter:
    @timeit
    def run(self):
        """
            Imports the dependency sections
        """
        sections = [
            "depends",
            "pre-depends",
            "recommends",
            "suggests",
            "breaks",
            "conflicts",
            "provides",
            "replaces",
            "enhances",
        ]
        for section in sections:
            session.add(DependencySection(name=section))
        session.commit()

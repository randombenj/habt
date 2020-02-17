from habt.models import (
    InstallTarget,
    Architecture,
    Part,
    Distribution,
    Archive
)
from habt.importer.helper import timeit
from habt.database import session

import logging

log = logging.getLogger(__name__)


class InstallTargetImporter():

    @timeit
    def run(self, packages):
        '''
            Imports the install targets sections
        '''
        for entry in packages:
            source_list_entry = entry['Entry']
            archive = Archive.get_or_add(
                url=source_list_entry.archive
            )
            distribution = Distribution.get_or_add(
                name=source_list_entry.distribution
            )


            for part in source_list_entry.parts:
                db_part = Part.get_or_add(
                    name=part
                )

                for architecture in entry['Architectures']:
                    InstallTarget.get_or_add(
                        archive=archive,
                        distribution=distribution,
                        part=db_part,
                        architecture=Architecture.get_or_add(
                            name=architecture['Architecture']
                        )
                    )

                InstallTarget.get_or_add(
                    archive=archive,
                    distribution=distribution,
                    part=db_part,
                    architecture=Architecture.get_or_add(
                        name='all'
                    )
                )

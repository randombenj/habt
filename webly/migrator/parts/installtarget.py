from webly.models import (InstallTarget,
    Architecture,
    Part,
    Distribution,
    Archive)
from webly.migrator.helper import timeit
from webly.database import session

import logging

log = logging.getLogger(__name__)

class InstallTargetMigrator():

    @timeit
    def run(self, packages):
        '''
            Migrates the install targets sections
        '''
        for entry in packages:
            source_list_entry = entry['Entry']
            archive = Archive.get_or_create(
                url=source_list_entry.archive
            )
            distribution = Distribution.get_or_create(
                name=source_list_entry.distribution
            )

            for part in source_list_entry.parts:
                db_part = Part.get_or_create(
                    name=part
                )

                for architecture in entry['Architectures']:
                    session.add(InstallTarget(
                        archive=archive,
                        distribution=distribution,
                        part=db_part,
                        architecture=Architecture.get_or_create(
                            name=architecture['Architecture']
                        )
                    ))
                    session.commit()

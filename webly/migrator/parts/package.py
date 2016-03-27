from itertools import groupby
from webly.models import Package, PackageVersion
from webly.database import session

import logging

log = logging.getLogger(__name__)

class PackageMigrator():
    def __init__(self, packages):
        self._packages = packages

    def run(self):
        '''
            Runs all the migrator parts
        '''
        self.packages()

    def packages(self):
        '''
            Migrates the packages
        '''
        for source in self._packages:
            for architecture in source['Architectures']:
                # log.info(architecture)
                for key, packages in groupby(
                    architecture['Packages'],
                    lambda p: p['Package']
                ):
                    package = Package.get_or_create(name=key)
                    package_versions = []

                    for version in packages:
                        package_versions.append(
                            PackageVersion.get_or_create(
                                version=version['Version'],
                                description=version['Description'],
                                maintainer=version['Maintainer'],
                                filename=version['Filename']
                                #package=package
                            )
                        )

                    package.versions = package_versions
                    if package.id:
                        session.add(package)

                log.info('Commiting changes to the DB!')
                session.commit()

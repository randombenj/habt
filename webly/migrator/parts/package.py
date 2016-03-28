from itertools import groupby
from webly.models import Package, PackageVersion, PackageSection
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
            sources_list = list(source['Sources'])
            description_list = list(source['Descriptions'])
            for architecture in source['Architectures']:
                for key, packages in groupby(
                    architecture['Packages'],
                    lambda p: p['Package']
                ):
                    package = Package.get_or_create(name=key)
                    for version in packages:
                        # Get the source package for source code information
                        source_package = next(
                            s for s in sources_list
                            if package.name in s['Binary']
                        )
                        # Get the package description
                        description = next(
                            d for d in description_list
                            if package.name in d['Package']
                        )

                        package.versions.append(
                            PackageVersion.get_or_create(
                                version=version['Version'],
                                title=version['Description'],
                                description=description['Description-en'],
                                maintainer=version['Maintainer'],
                                filename=version['Filename'],
                                homepage=version.get('Homepage', default=''),
                                vcs_browser=source_package.get('Vcs-Browser', default=''),
                                section=PackageSection.get_or_create(name=version['Section'])
                            )
                        )

                    if package.id:
                        session.add(package)

                log.info('Commiting changes to the DB!')
                session.commit()

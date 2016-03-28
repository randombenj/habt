from itertools import groupby
from webly.models import Package, PackageVersion, PackageSection
from webly.migrator.helper import timeit
from webly.database import session

import logging

log = logging.getLogger(__name__)

class PackageMigrator():
    def __init__(self, packages):
        self._packages = packages

    @timeit
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
                        self._package_version(
                            package,
                            version,
                            sources_list,
                            description_list
                        )

                    if package.id:
                        session.add(package)

                log.info('Commiting changes to the DB!')
                session.commit()
                log.info('Added {0} debian Packages to the database'.format(
                    Package.query.count()
                ))

    def _package_version(self, package, version, source_packages, description_list):
        # Get the source package for source code information
        source_package = next(
            (s for s in source_packages
            if package.name in s['Binary']),
            {} # default value
        )
        # remove the old entry for performance reason
        if source_package and source_package['Binary'] == package.name:
            log.debug('Removing source: {0}'.format(source_package))
            source_packages.remove(source_package)

        # Get the package description
        description = next(
            (d for d in description_list
            if package.name in d['Package']),
            {} # default value
        )
        # remove the old entry for performance reason
        if description:
            log.debug('Removing description: {0}'.format(description))
            description_list.remove(description)

        package.versions.append(PackageVersion(
            version=version['Version'],
            title=version['Description'],
            description=description.get('Description-en', ''),
            maintainer=version['Maintainer'],
            filename=version['Filename'],
            homepage=version.get('Homepage', ''),
            vcs_browser=source_package.get('Vcs-Browser', ''),
            section=PackageSection.get_or_create(name=version['Section'])
        ))

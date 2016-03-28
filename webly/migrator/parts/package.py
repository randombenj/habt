from itertools import groupby
from webly.models import (Package,
    PackageVersion,
    PackageSection,
    DependencySection,
    Dependency)
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

                    # commiting once per package, no self refferences assumed
                    if not package.id:
                        session.add(package)
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

        package_section = PackageSection.get_or_create(name=version['Section'])
        if not package_section.id:
            # add the section if it is new
            session.add(package_section)

        package_version = PackageVersion(
            version=version['Version'],
            title=version['Description'],
            description=description.get('Description-en', ''),
            maintainer=version['Maintainer'],
            filename=version['Filename'],
            homepage=version.get('Homepage', ''),
            vcs_browser=source_package.get('Vcs-Browser', ''),
            section=package_section
        )
        self._package_dependencies(version, package_version)
        package.versions.append(package_version)

    def _package_dependencies(self, version, package_version):
        for section in version.relations:
            dependency_section = (DependencySection
                .query
                .filter(
                    DependencySection.name == section
                ).first())

            for relation in version.relations[section]:
                # TODO: define what to do with the OR relation
                relation = relation[0]
                package = Package.get_or_create(
                    # even though it's forbidden in the policy,
                    # there are some capital case names ...
                    name=relation['name'].lower()
                )
                if not package.id:
                    # add the package if it is new
                    session.add(package)

                session.add(Dependency(
                    # add the dependency version (if any)
                    version='({0} {1})'.format(
                        relation['version'][0],
                        relation['version'][1]
                    ) if relation['version'] else '',
                    package=package,
                    dependency_section=dependency_section,
                    package_version=package_version
                ))

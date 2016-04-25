from itertools import groupby
from webly.models import (
    Package,
    PackageVersion,
    PackageSection,
    DependencySection,
    Dependency
)
from webly.models import (
    InstallTarget,
    Architecture,
    Archive,
    Distribution,
    Part
)
from webly.importer.helper import timeit
from webly.database import session

import logging

log = logging.getLogger(__name__)


class PackageImporter():
    def __init__(self, packages):
        self._packages = packages

    @timeit
    def run(self):
        '''
            Runs all the Importer parts
        '''
        self.packages()

    def packages(self):
        '''
            Imports the packages
        '''
        for source in self._packages:

            sources_list = list(source['Sources'])
            description_list = list(source['Descriptions'])

            for architecture in source['Architectures']:
                source_list_entry = source['Entry']
                installtarget = (InstallTarget.query
                    .join(Archive)
                    .join(Distribution)
                    .join(Part)
                    .join(Architecture)
                    .filter(
                        (Archive.url == source_list_entry.archive) &
                        (Distribution.name == source_list_entry.distribution) &
                        # TODO: loop through parts in source.py
                        (Part.name == source_list_entry.parts[0]) &
                        (Architecture.name == architecture['Architecture'])
                    ).one()
                )

                # Load the 'all' installtarget separatly
                installtarget_all = (InstallTarget.query
                    .join(Archive)
                    .join(Distribution)
                    .join(Part)
                    .join(Architecture)
                    .filter(
                        (Archive.url == source_list_entry.archive) &
                        (Distribution.name == source_list_entry.distribution) &
                        # TODO: loop through parts in source.py
                        (Part.name == source_list_entry.parts[0]) &
                        (Architecture.name == 'all')
                    ).one()
                )

                if installtarget:
                    log.info('Installtarget: {0}'.format(installtarget))
                else:
                    log.warn('No Installtarget found!')

                for key, packages in groupby(
                    architecture['Packages'],
                    lambda p: p['Package']
                ):
                    package = Package.get_or_create(name=key)
                    for version in packages:
                        version_installtarget = installtarget
                        if version['Architecture'] == 'all':
                            version_installtarget = installtarget_all
                        self._package_version(
                            package,
                            version,
                            sources_list,
                            description_list,
                            installtarget
                        )

                    # commiting once per package, no self refferences assumed
                    if not package.id:
                        session.add(package)
                    session.commit()

                log.info('Added {0} debian Packages to the database'.format(
                    Package.query.count()
                ))

    def _package_version(
        self,
        package,
        version,
        source_packages,
        description_list,
        installtarget
    ):
        if package.id:
            db_version = (PackageVersion.query
                .filter(
                    PackageVersion.package_id == package.id,
                    PackageVersion.version == version['Version']
                ).first()
            )
            if db_version:
                db_version.installtargets.append(installtarget)
                log.info('Version allready exists {0} ({1})'.format(
                    version['Package'],
                    version['Version']
                ))
                return

        # Get the source package for source code information
        source_package = next(
            (s for s in source_packages
                if package.name in s['Binary']),
            {}  # default value
        )
        # remove the old entry for performance reason
        if source_package and source_package['Binary'] == package.name:
            log.debug('Removing source: {0}'.format(source_package))
            source_packages.remove(source_package)

        # Get the package description
        description = next(
            (d for d in description_list
                if package.name in d['Package']),
            {}  # default value
        )

        # assign default value
        title_text = version['Description']
        description_text = description.get('Description-en', '')

        # remove the old entry for performance reason
        if description:
            log.debug('Removing description: {0}'.format(description))
            description_list.remove(description)
        else:
            # if no description is given from the translations file, check if
            # the package description is multiline
            description_lines = version['Description'].splitlines()
            if len(description_lines) > 1:
                title_text = description_lines[0].strip()
                description_text = '\n'.join(description_lines[1:]).strip()

        package_section = PackageSection.get_or_create(name=version['Section'])
        if not package_section.id:
            # add the section if it is new
            session.add(package_section)

        package_version = PackageVersion(
            version=version['Version'],
            title=title_text,
            description=description_text,
            maintainer=version['Maintainer'],
            filename=version['Filename'],
            homepage=version.get('Homepage', ''),
            vcs_browser=source_package.get('Vcs-Browser', ''),
            section=package_section
        )
        package_version.installtargets.append(installtarget)
        self._package_dependencies(version, package_version)
        package.versions.append(package_version)

    def _package_dependencies(self, version, package_version):
        for section in version.relations:
            dependency_section = (DependencySection.query
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

import gzip
import requests
from deb822 import Packages, Release, Sources
import logging

log = logging.getLogger(__name__)

class Source():
    def __init__(self, filename):
        self._filename = filename
        self._source_list = SourceList(self._filename)

    @property
    def __parser(self):
        return {
            'Packages': Packages.iter_paragraphs,
            'Sources': Sources.iter_paragraphs,
            'Contents': lambda f: {}
        }

    @property
    def packages(self):
        packages = []

        for entry in self._source_list.entries:
            # get the sources file for requested entry
            response = requests.get(
                entry.build_uri(
                    entry.sources_file['Sources']['name']
                )
            )

            if response.ok:
                content = gzip.decompress(response.content)

            source_list_entry = {
                'Entry': entry,
                'Sources': self.__parser['Sources'](content),
                'Architectures': []
            }

            for architecture in entry.architectures:
                # get the binary and source files
                files = entry.get_files(architecture)

                architecture_entry = {
                    'Architecture': architecture
                }

                for f in files:
                    response = requests.get(
                        entry.build_uri(
                            files[f]['name']
                        )
                    )

                    if response.ok:
                        content = gzip.decompress(response.content).decode("utf-8")
                        log.info('Type: ' + str(type(content)))
                        architecture_entry.update({
                            f: self.__parser[f](content)
                        })

                source_list_entry['Architectures'].append(architecture_entry)
            packages.append(source_list_entry)

        # log.info(packages)
        return packages


class SourceList():
    def __init__(self, sources_list_file):
        self._current_index = 0 # index tracking for the current ge
        self._raw_sources_list = []

        with open(sources_list_file) as sources_list:
            # read the sources.list file, remove comments and empty lines
            self._raw_sources_list = [
                s.strip() for s in sources_list.readlines()
                if s.strip() and not s.startswith('#')
            ]


    @property
    def entries(self):
        return [SourceListEntry(f) for f in self._raw_sources_list]


class SourceListEntry():
    def __init__(self, source):
        '''
            Initializes a source.list entry
        '''
        self._source_list = source.split()
        self._architectures = []
        # the architectures don't have to be set
        has_defined_architectures = self._source_list[1].startswith('[')
        if has_defined_architectures:
            # removing the '[arch=' and ']' fron the architecture list
            self._architectures = self._source_list[1][6:-1].split(',')

        offset = 1 if has_defined_architectures else 0

        # load components of the sources list
        self._archive = self._source_list[1 + offset]
        self._distribution = self._source_list[2 + offset]
        # one source list can have multiple components (main, non-free ...)
        self._parts = self._source_list[3 + offset:]

        response = requests.get(
            '{0}/dists/{1}/Release'.format(self._archive, self._distribution)
        )

        if response.ok:
            release = next(Release.iter_paragraphs(response.text))
            # if no expicit arcitectures are defined, use all given in the release file
            if not self._architectures:
                self._architectures = release['Architectures'].split()

            # get only the files from the requested parts
            self._files = [
                f for f in release['SHA256']
                if (
                    # ignore udeb and debian-installer files
                    '-udeb' not in f['name'] and
                    'debian-installer' not in f['name'] and
                    # use only the gzip compressed files
                    '.gz' in f['name'] and
                    any([
                        # filter for the requested parts
                        p for p in self._parts
                        if p in f['name']]
                    ) and
                    any([
                        # filter for the requested architectures ignoring the source packages
                        a for a in self._architectures
                        if a in f['name'] or 'Sources' in f['name']
                    ])
                )
            ]

    @property
    def archive(self):
        '''
            returns:
             The origin of the package source
        '''
        return self._archive

    @property
    def distribution(self):
        '''
            returns:
             The distribution of the source list
        '''
        return self._distribution

    @property
    def parts(self):
        '''
            returns:
             The parts of the source list
        '''
        return self._parts

    @property
    def architectures(self):
        '''
            returns:
             The architectures of the sources list.

             If not specified in the source.list file all architectures
             in the release files are taken.
        '''
        return self._architectures

    def build_uri(self, requested_file):
        '''
            Builds the destination archive url to download the given file.
            This is done with the standard package repository format:
            $archive/dists/$distribution/$file

            returns:
             A built uri ready to download the given file
        '''
        return '{0}/dists/{1}/{2}'.format(
            self._archive,
            self._distribution,
            requested_file
        )

    @property
    def sources_file(self):
        '''
            returns:
             Sources file if any could be found
        '''
        return {'Sources': [
            f for f in self._files
            if 'Sources' in f['name']
        ][0]}

    def get_files(self, architecture):
        '''
            architecture:
             The given architecture e.g 'amd64' or 'armhf'

            returns:
             The listed files in the Release file matching the given
             Architecture
        '''
        if not architecture in self._architectures:
            return []

        # filter the files for a matching architecture
        architecture_files = [
            f for f in self._files
            if architecture in f['name']
        ]

        def file_filter(name):
            '''
                Filters files if they contain
                a given name.
            '''
            return [
                f for f in architecture_files
                if name in f['name']
            ]

        return {
            'Packages': file_filter('Packages')[0],
            'Contents': file_filter('Contents')[0]
        }

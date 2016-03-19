import gzip
import requests
from io import StringIO
from deb822 import Packages, Release
import logging

log = logging.getLogger(__name__)

class Source():
    def __init__(self, filename):
        self._filename = filename
        self._source_list = SourceList(self._filename)


    @property
    def packages(self):
        for entry in self._source_list.entries:
            log.info(entry.__dict__)
        # # removing the '[arch=' and ']' fron the architecture list
        # for architecture in entry_parts[1][6:-1].split(','):
        #     # one source list can have multiple components (main, non-free ...)
        #     for component in entry_parts[4:]:
        #         response = requests.get('{0}/dists/{1}/{2}/binary-{3}/Packages.gz'.format(
        #             entry_parts[2],
        #             entry_parts[3],
        #             component,
        #             architecture
        #         ))
        #
        #         if response.ok:
        #             content = gzip.GzipFile(
        #                 fileobj=StringIO(response.content)
        #             ).read()
        #
        #             sources.append({
        #                 'architecture': architecture,
        #                 'component': component,
        #                 'packages': Packages.iter_paragraphs(content)
        #             })
        #
        # return sources


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
                if any([p for p in self._parts if p in f['name']])
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
            retunrs:
             The architectures of the sources list.

             If not specified in the source.list file all architectures
             in the release files are taken.
        '''
        return self._architectures

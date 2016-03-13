import gzip
import deb822
import requests
from StringIO import StringIO

class Source():
    def __init__(self, filename):
        self._filename = filename
        self._source_file = open(self._filename, 'r')

    def __next__(self):
        return self.next()

    def next(self):

        sources = []

        entry = self._source_file.readline
        entry_parts = entry.split()

        # removing the '[arch=' and ']' fron the architecture list
        for architecture in entry_parts[1][6:-1].split(','):
            # one source list can have multiple components (main, non-free ...)
            for component in entry_parts[4:]:
                response = requests.get('{0}/dists/{1}/{2}/binary-{3}/Packages.gz'.format(
                    entry_parts[2],
                    entry_parts[3],
                    component,
                    architecture
                ))

                if response.ok:
                    content = gzip.GzipFile(
                        fileobj=StringIO(response.content)
                    ).read()

                    sources.append({
                        'architecture': architecture,
                        'component': component,
                        'packages': deb822.Packages.iter_paragraphs(content)
                    })

        return sources

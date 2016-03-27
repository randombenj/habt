from deb822 import Deb822

class Descriptions(Deb822):
    """Represent a translated description list"""

    def __init__(self, *args, **kwargs):
        Deb822.__init__(self, *args, **kwargs)

    @classmethod
    def iter_paragraphs(cls, sequence, fields=None, use_apt_pkg=True,
                        shared_storage=False, encoding="utf-8"):
        """Generator that yields a Deb822 object for each paragraph in Packages.

        Note that this overloaded form of the generator uses apt_pkg (a strict
        but fast parser) by default.

        See the Deb822.iter_paragraphs function for details.
        """
        return super(Descriptions, cls).iter_paragraphs(sequence, fields,
                                    use_apt_pkg, shared_storage, encoding)

class Contents():
    """Represent the binary packages file contents list"""

    @staticmethod
    def get_contents(content):
        contents = []
        found_beginning=False
        for line in content.splitlines():
            if found_beginning:
                line_content = line.split()
                contents.append({
                    'file': line_content[0],
                    'packages': line_content[1].split(',')
                })
            # begin after headings
            if 'FILE' in line and 'LOCATION' in line:
                found_beginning = True

        return contents

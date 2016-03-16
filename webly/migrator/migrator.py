import os
from webly.migrator.source import Source

class Migrator():
    def __init__(self):
        for source in Source(os.path.join(os.path.dirname(__file__), 'sources.list')).packages:
            print(source)

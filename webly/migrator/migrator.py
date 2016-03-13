from webly.migrator.source import Source

class Migrator():
    def __init__(self):
        for source in Source('sources.list'):
            print(source)

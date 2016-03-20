import os
import logging
from webly.models import Package
from webly.migrator.source import Source

log = logging.getLogger(__name__)

class Migrator():
    def __init__(self, session):
        for source in Source(os.path.join(os.path.dirname(__file__), 'sources.list')).packages:
            for architecture in source['Architectures']:
                # log.info(architecture)
                for package in architecture['Packages']:
                    log.info('Adding Packet:\n\n')
                    log.info(package['Package'])

                    package = Package(name=package['Package'])

                    session.add(package)

                log.info('Commiting changes to the DB!')
                session.commit()

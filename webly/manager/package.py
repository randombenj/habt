from sqlalchemy.orm import joinedload

from webly.database import session
from webly.models import Package

class PackageManager():
    def search_packages(self, query):
        '''
            query:
             The given search query to search for in
             the database

            returns:
             A json serializable results dictionary with
             the search results as a list from the database

             { "results": [ ... ] }
        '''
        results = (Package.query
            .filter(
                # filter for the name
                Package.name.like("%{0}%".format(query)) |
                # also allow regular expressions
                Package.name.op('~')(query)
            ).all())
        return { 'results': results }

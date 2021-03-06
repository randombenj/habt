from sqlalchemy.orm import joinedload

from habt.models import Package, PackageVersion


class PackageManager:
    def search_packages(self, query):
        """
            query:
             The given search query to search for in
             the database

            returns:
             A json serializable results dictionary with
             the search results as a list from the database

             { "results": [ ... ] }
        """
        results = (
            Package.query.filter(
                # filter for the name
                Package.name.like("%{0}%".format(query))
                |
                # also allow regular expressions
                Package.name.op("REGEXP")(query)
            )
            # load all available versions
            .options(joinedload("versions").load_only("version"))
            .order_by(Package.name)
            .limit(50)
            .all()
        )
        return {"results": results}

    def get_package(self, package_name):
        """
            package_name:
             The Package to search for in the Database

            returns:
             A json serializable results dictionary
             with the loaded package
        """
        package = {
            "package": (
                Package.query.filter(Package.name == package_name)
                # options to load the required joined data
                .options(
                    # load all versions of the package
                    joinedload("versions"),
                    # load the part the installtarget
                    joinedload("versions")
                    .joinedload("installtargets")
                    .joinedload("part"),
                    # load the distribution the installtarget
                    joinedload("versions")
                    .joinedload("installtargets")
                    .joinedload("distribution"),
                    # load all the packages depending on this package
                    joinedload("referenced_by")
                    .joinedload("package_version")
                    .joinedload("package"),
                    # load all the dependency sections of the packages,
                    # depending on this package
                    joinedload("referenced_by").joinedload("dependency_section"),
                )
            ).first()
        }

        package["package"].referenced_by.sort(key=lambda d: d.dependency_section.name)
        return package

    def get_package_version(self, package_name, version=None):
        """
            package_name:
             The Package to search for in the Database

            version:
             If a version is given, then Information about
             this version will also be loaded from the
             Database.
             If no version is given, then the latest will
             be included in the search result.

            returns:
             A json serializable results dictionary
             with the loaded package and version if any is given
        """
        version = (
            PackageVersion.query.join(Package)
            .filter(Package.name == package_name, PackageVersion.version == version)
            .options(
                # load the dependencies and packages
                joinedload("dependencies").joinedload("package"),
                # load the dependency sections
                joinedload("dependencies").joinedload("dependency_section"),
                # load the part the installtarget
                joinedload("installtargets").joinedload("part"),
                # load the distribution the installtarget
                joinedload("installtargets").joinedload("distribution"),
                # load the archive the installtarget
                joinedload("installtargets").joinedload("archive"),
                # load the architecture the installtarget
                joinedload("installtargets").joinedload("architecture"),
            )
            .first()
        ).__json__()

        # sort the dependencies by their section
        version["dependencies"].sort(key=lambda d: d.dependency_section.name)

        return {"version": version}

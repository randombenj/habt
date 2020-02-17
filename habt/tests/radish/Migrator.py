from radish import given, when, then, arg_expr

from habt.database import drop, create, session
from habt.importer import Importer
from habt.models import Package


# setup the source list argument parser
@arg_expr("list", r".*.list")
def source_list_argument_expression(text):
    """
        Return the source.list

        test:
         The parsed sources.list path
    """
    return text


@given("The database is set up and clean")
def have_numbers(step):
    session.remove()
    drop()
    create()


@when("I run an import for {source_list:list}")
def sum_numbers(step, source_list):
    Importer(source_list).run()


@then("I expect there top be packages in the database")
def expect_result(step):
    real_package_count = Package.query.count()
    assert real_package_count > 0

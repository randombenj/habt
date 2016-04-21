from radish import given, when, then

from webly.manager import PackageManager
from webly.models import Package


@given("The PackageManager is set up")
def have_numbers(step):
    step.context.manager = PackageManager()


@when("I search for {query:w}")
def search_package(step, query):
    step.context.result = step.context.manager.search_packages(query)


@when("I request the {package_name} package")
def get_package(step, package_name):
    step.context.package = step.context.manager.get_package(package_name)


@when("I request the version {version} of the {package_name:w} package")
def get_package_version(step, version, package_name):
    package_version = step.context.manager .get_package_version(
        package_name,
        version
    )
    step.context.version = package_version


@then("I expect {result:w} to be in the results list")
def expect_result(step, result):
    assert result in [r.name for r in step.context.result['results']]


@then("I expect {count:g} packages to be found")
def expect_result_count(step, count):
    assert len(step.context.result['results']) == count


@then("I expect the package {package:w}")
def expect_package(step, package):
    assert step.context.package['package'].name == package


@then("I don't expect there to be any package")
def expect_no_package(step):
    assert step.context.package['package'] is None


@then("I expect the version {version} of the {package_name:w} package")
def expect_package_version(step, version, package_name):
    # TODO fix context error
    package_version = step.context.manager.get_package_version(
        package_name,
        version
    )
    package = (Package.query
        .filter(
            Package.id == package_version['version']['package_id']
        )
        .one()
    )
    assert (
        package_version['version']['version'] == version and
        package.name == package_name
    )

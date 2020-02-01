import json
from habt.api import app

from radish import given, when, then, before

from habt.database import drop, create, session
from habt.importer import Importer
from habt.manager import PackageManager
from habt.models import Package

import logging

def _dict_response(response):
    '''
        Converts the json response string to a dictionary
    '''
    return json.loads(next(response.response).decode("utf-8"))


@before.each_feature
def import_database(scenario):
    session.remove()
    drop()
    create()
    Importer('sources.list').run()


@given("The api is ready")
def have_numbers(step):
    app.testing = True
    step.context.client = app.test_client()


@when("I search for {query:w}")
def search_package(step, query):
    response = step.context.client.get(
        '/search/{0}'.format(query)
    )
    assert response.status_code == 200
    step.context.result = _dict_response(response)


@when("I request the {package_name} package")
def get_package(step, package_name):
    response = step.context.client.get(
        '/package/{0}'.format(package_name)
    )
    assert response.status_code == 200
    step.context.package = _dict_response(response)


@when("I request the version {version} of the {package_name:w} package")
def get_package_version(step, version, package_name):
    response = step.context.client.get(
        '/package/{0}/version/{1}'.format(
            package_name,
            version
        )
    )
    assert response.status_code == 200
    step.context.version = _dict_response(response)


@then("I expect {result:w} to be in the results list")
def expect_result(step, result):
    assert result in [
        r['name'] for r in
        step.context.result['results']
    ]


@then("I expect {count:g} packages to be found")
def expect_result_count(step, count):
    assert len(step.context.result['results']) == count


@then("I expect the package {package:w}")
def expect_package(step, package):
    assert step.context.package['package']['name'] == package


@then("I don't expect there to be any package")
def expect_no_package(step):
    assert step.context.package['package'] is None


@then("I expect the version {version} of the {package_name:w} package")
def expect_package_version(step, version, package_name):
    # TODO fix context error
    # print(step.context.__dict__)
    package_version = _dict_response(step.context.client.get(
        '/package/{0}/version/{1}'.format(
            package_name,
            version
        )
    ))
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

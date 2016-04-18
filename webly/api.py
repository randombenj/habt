from flask import Flask, jsonify
from flask.ext.jsontools import jsonapi, DynamicJSONEncoder
from flask.ext.cors import cross_origin
from flask_swagger import swagger

from webly.database import session
from webly.manager import PackageManager

# setup the configuration for the application
from webly.config import Config

import logging

# Configure the logger
config = Config()
config.setup_logger()
log = logging.getLogger(__name__)

app = Flask(__name__)
app.debug = config.debug
# uses the <obj>.__json__() method to encode json
app.json_encoder = DynamicJSONEncoder

@app.teardown_appcontext
def shutdown_session(exception=None):
    """
        Destroy the Database session at the end of a request
    """
    session.remove()

@app.route("/spec")
@cross_origin()
def spec():
    """
        returns:
         Api specification
    """
    swag = swagger(app)
    swag['info']['version'] = "0.0.0"
    swag['info']['title'] = "Webly API"
    return jsonify(swag)

@app.route("/search/<string:query>")
@jsonapi
def search(query):
    """
       Searches debian packages
       ---
       tags:
         - [search, debian, packages]
       parameters:
         - query:
            The search query to search for in the database
       responses:
           200:
               description: Search successfully completed
    """
    return PackageManager().search_packages(query)


@app.route("/package/<string:name>")
@jsonapi
def package(name):
    """
       Returns the details of a debian package
       ---
       tags:
         - [details, debian, packages]
       parameters:
         - name:
             Debian package name
       responses:
           200:
               description: Datail successfully loaded
    """
    return PackageManager().get_package(name)

@app.route("/package/<string:name>/version/<string:version>")
@jsonapi
def version(name, version):
    """
       Returns the details of a debian package
       ---
       tags:
         - [details, debian, packages]
       parameters:
         - name:
             Debian package name
         - version:
             Version of the package
       responses:
           200:
               description: Datail successfully loaded
    """
    return PackageManager().get_package_version(name, version)

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000)

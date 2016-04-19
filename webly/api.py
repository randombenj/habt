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
    # api information
    swag['info']['version'] = "0.0.0"
    swag['info']['title'] = "Webly API"
    # api prefix
    swag['basePath'] = "/api"
    return jsonify(swag)

@app.route("/search/<string:query>")
@cross_origin()
@jsonapi
def search(query):
    """
         Returns the details of a debian package
        ---
        tags:
          - search

        parameters:
          - name: query
            description: Search query
            in: path
            type: string

        responses:
          200:
            description: Search was successful
        """
    return PackageManager().search_packages(query)


@app.route("/package/<string:name>")
@cross_origin()
@jsonapi
def package(name):
    """
       Returns the details of a debian package
       ---
       tags:
         - package
       parameters:
         - name: name
           description: Debian package name
           in: path
           type: string
       responses:
           200:
               description: Datail successfully loaded
    """
    return PackageManager().get_package(name)

@app.route("/package/<string:name>/version/<string:version>")
@cross_origin()
@jsonapi
def version(name, version):
    """
       Returns the details of a debian package version
       ---
       tags:
         - version
       parameters:
        - name: name
          description: Debian package name
          in: path
          type: string
        - name: version
          description: Package version
          in: path
          type: string
       responses:
           200:
               description: Datail successfully loaded
    """
    return PackageManager().get_package_version(name, version)

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000)

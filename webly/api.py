from flask import Flask, jsonify
from flask.ext.jsontools import jsonapi, DynamicJSONEncoder
from sqlalchemy.orm import joinedload

from webly.database import session

from webly.models import Package
from webly.config import Config

import logging

config = Config()
config.setup_logger()
log = logging.getLogger(__name__)

app = Flask(__name__)
app.debug = config.debug
# uses the <obj>.__json__() method to encode json
app.json_encoder = DynamicJSONEncoder

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()

@app.route("/")
@jsonapi
def hello():
    packages = (Package.query
        .options(
            joinedload('versions')
                .joinedload('section')
        )
        .all())

    return {'packages': packages}

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000)

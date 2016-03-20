from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from webly.models import Package
from webly.config import Config

import logging

config = Config()
config.setup_logger()
log = logging.getLogger(__name__)

app = Flask(__name__)
app.debug = config.debug
app.config['SQLALCHEMY_DATABASE_URI'] = config.connection_string
db = SQLAlchemy(app)


@app.route("/")
def hello():
    packages = [{'name': p.name} for p in Package.query.all()]
    log.info(packages)
    return jsonify({'asdf': packages})

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)

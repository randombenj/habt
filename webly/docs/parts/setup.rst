
Setup
=====

Docker Environement
-------------------

.. note::
   To run the docker environment you have to `install docker <https://docs.docker.com/engine/installation/>`_
   and `docker-compos <https://docs.docker.com/compose/install/>`_  first.

After installing the docker environment you have to create a ``.env`` file
in the root folder of the project.
This file contains the database connection information and might look
something like this:

.. code-block:: bash

  DEBUG=True
  DB_NAME=postgres
  DB_USER=postgres
  DB_PASS=postgres
  DB_SERVICE=postgres
  DB_PORT=5432

This example configuration file works out of the box for the default
docker configuration, but it's not recommended because of security reasons.

After the ``.env`` file is created you first build the docker containers
and the run them.

.. code-block:: bash

  docker-compose build
  docker-compose up [-d]


The first command ``docker-compose build`` will build two docker container,
according to the ``docker-compose.yml`` file. The python applicationserver
container and the nginx container.

The python applicationserver is based on ``python:3.4`` and installs
all files in the requirements.txt.

The nginx webserver configures the routes for the static mapping in
``/www/webly`` and the reverse proxy for the applicationserver.
Additionaly nginx also installs the bower dependencies for the
angular application.

Build this documentation
------------------------

.. note::
   To build the documentation in a docker container,
   you can start a shell in the container by running: ``docker exec -it webly_web_1 bash``

To build this documentation run pip install with the ``requirements.txt`` file
located in the ``webly/docs/`` folder.

.. code-block:: bash

  pip install -r webly/docs/requirements.txt

After the requirements to generate the documentation are installed,
you can run ``make help`` to view all possible documentation types.

.. note::
   To generate the documentation from the sourcecode using
   `autodoc <http://www.sphinx-doc.org/en/stable/ext/autodoc.html>`_
   you have to install all requirements of the
   projects located in the ``requirements.txt`` file in the root directory.

Then to generate for example the html help page run:

.. code-block:: bash

  make html

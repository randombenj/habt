
Testing
=======

Execute the Jasmine Tests
-------------------------

To run the Jasmine tests first change in to the ``web`` directory in the root
of the project. Then install all required packages to run Karma and the
Jasmine tests:

.. code-block:: bash

  npm install

After this, the thests can be executed by running:

.. code-block:: bash

  npm test

The tests in the ``web/tests`` folder will be executed automaticaly, only
the chrome browser ist configured to run the tests at the moment.

All html coverage reports will be generated when the tests are run and
are located in the folder ``web/.coverage``.

Execute the Radish Tests
-------------------------

.. note::
   To execute the radish tests in a docker container,
   you can start a shell in the container by running: ``docker exec -it habt_web_1 bash``

In order to run the radish tests you first have to install the required
packges. To do this run pip with the ``requirements.txt`` located
in the ``habt/tests`` folder:

.. code-block:: bash

  pip install -r habt/tests/requirements.txt

After this you can change in to the ``habt`` directory and
run the radish tests with:

.. code-block:: bash

  radish -b tests/radish tests/

To create the code coverage report run radish with the
`coverage <https://coverage.readthedocs.org/en/coverage-4.0.3/>`_ tool:

.. code-block:: bash

  coverage run --source=. /usr/local/bin/radish -b tests/radish/ tests/

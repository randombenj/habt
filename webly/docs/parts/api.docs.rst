
Api Documentation
=================

Because `flask-swagger <https://github.com/gangverk/flask-swagger>`_
was used to generate the api specification using docstrings.
The swagger api specification can be loaded via the
route ``/api/spec``.

This api specificaiton can be displayed with swagger-ui.
Simply download the `github repository <https://github.com/swagger-api/swagger-ui>`_
and `build and run the docker image <https://github.com/swagger-api/swagger-ui#build-using-docker>`_.

Then point the browser to `http://localhost:8080 <http://localhost:8080>`_
and add the api specification url.

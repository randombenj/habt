![habt](docs/assets/habt-logo.png)

**Find your debian packages.**

**habt** (/hʌbt/) is a simple web frontend for debian repositories.

It can be configured with [sources list](https://wiki.debian.org/SourcesList#sources.list_format)
entries. Based on this configurations it will create a cache where you can
browse the packages in a fancy web ui.

## Getting started

To run habt, you must first create a `.env` file, for the
database to connect to:

```sh
DEBUG=True
DB_NAME=postgres
DB_USER=postgres
DB_PASS=postgres
DB_SERVICE=postgres
DB_PORT=5432
```

After configuring the database you can start the application
with [docker-compose](https://docs.docker.com/compose/):

```sh
docker-compose build
docker-compose up [-d]
```

For more details, have a look at the [setup guide](habt/docs/parts/setup.rst).

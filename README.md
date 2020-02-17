![habt](docs/assets/habt-logo.png)

**Find your debian packages.**

**habt** (/hʌbt/) is a simple web frontend for debian repositories.

It can be configured with [sources list](https://wiki.debian.org/SourcesList#sources.list_format)
entries. Based on this configurations it will create a cache where you can
browse the packages in a fancy web ui.

## Getting started

The simplest way to run the application is to run it in
a docker container. The container will create an
sqlite database.

```sh
docker build -t habt .
docker run -p 80:8000 habt
```

![habt](web/src/assets/logo.png)

**Find your debian packages.**

[![build](https://github.com/randombenj/habt/workflows/habt%20ci/badge.svg)](https://github.com/randombenj/habt/actions)

**habt** (/hʌbt/) is a simple web frontend for debian repositories.

It can be configured with [sources list](https://wiki.debian.org/SourcesList#sources.list_format)
entries. Based on this configurations it will create a cache where you can
browse the packages in a fancy web ui.

## Getting started

The simplest way to run the application is to run it in
a docker container:

```sh
docker build -t habt .
docker run -p 80:8000 habt
```

## How does it look like

Here is a screenshot of how debian packages are shown:

![habt screenshot](docs/assets/screenshot.png)

---
Thanks [@lueschem](https://github.com/lueschem) for the idea!

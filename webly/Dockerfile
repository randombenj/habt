FROM python:3.4

RUN mkdir -p /usr/src/webly
WORKDIR /usr/src/webly

COPY requirements.txt /usr/src/webly/
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH /usr/src

COPY . /usr/src/webly/

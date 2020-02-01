FROM python:3.8

RUN mkdir -p /usr/src/habt
WORKDIR /usr/src/habt

COPY requirements.txt /usr/src/habt/
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH /usr/src

COPY . /usr/src/habt/

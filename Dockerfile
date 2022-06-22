FROM ubuntu:18.04
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install python3 python3-pip libpq-dev git -y \
    && ln -s $(which python3) /usr/bin/python

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /code
COPY . /code
RUN pytest

